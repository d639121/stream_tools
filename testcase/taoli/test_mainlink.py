#!/usr/bin/python 
# -*- coding: utf-8 -*-
# @Time    : 2020/5/20 11:13
# @Author  : LOUIE

from utils.operation_json import OperationJson as Opt_json
from common.common_tools import CommonTools as cotool
from common.http_requests import httprequest
from common.config_log import log
from stream_tools.config.constant import GLOBAL_VAR
from utils import generator
from utils.operation_yaml import OperationYAML
from utils import tools
import pytest
import time
import allure


data = OperationYAML().rafactor_data("mainlink.yaml")


allure.feature("【平台】全链路流程测试")
class TestMainLink():

    def setup_class(self):
        GLOBAL_VAR["title"] = str("python测试%s" % generator.random_ean8())
        GLOBAL_VAR["phoneNumber"] = str(generator.random_phone_number())
        GLOBAL_VAR["transNo"] = str(generator.timestamp())

    def setup(self):
        time.sleep(1)
        pass

    def teardown_class(self):
        Opt_json("mainlink.json").write_to_res_json(GLOBAL_VAR)

    @pytest.mark.parametrize("caseid, desc, precondition, parameterize, url, method, header, data, shared, check", data)
    def test_mainlink(self, caseid, desc, precondition, parameterize, url, method, header, data, shared, check):
        log.info("CaseId: <- {} ->".format(caseid))
        log.info("Desc: {}".format(desc))
        if str(caseid) == "10022":
            time.sleep(30)
        header = cotool().set_header(header)
        params = cotool().set_params(parameterize, data)
        res = httprequest(url, method, header, params)
        if shared:
            cotool.extract_variable(res, shared)
        if check:
            cotool().assert_res(res, check)
        if str(caseid)  == "10017":
            tools.create_qr_code(GLOBAL_VAR["creativityCode"])
            time.sleep(180)
        allure.dynamic.story("CaseID: < {} > - {}".format(caseid, desc))


if __name__ == '__main__':
    pytest.main(["-sxl", "--reruns", "2", "--reruns-delay", "2", "test_mainlink.py"])

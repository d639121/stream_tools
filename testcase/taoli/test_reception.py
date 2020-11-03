#!/usr/bin/python 
# -*- coding: utf-8 -*-
# @Time    : 2020/4/27 12:13
# @Author  : LOUIE

from utils.operation_json import OperationJson as Opt_json
from common.common_tools import CommonTools as cotool
from common.http_requests import httprequest
from common.config_log import log
from stream_tools.config.constant import GLOBAL_VAR
from utils import generator
from utils.operation_yaml import OperationYAML
import pytest
import allure
import time


data = OperationYAML().rafactor_data("/taoli/reception.yaml")


allure.feature("【桃李系统】入学接待流程")
class TestRefund():

    def setup(self):
        time.sleep(1)

    def setup_class(self):
        GLOBAL_VAR["title"] = str("python测试%s" % generator.random_ean8())
        GLOBAL_VAR["phoneNumber"] = str(generator.random_phone_number())
        GLOBAL_VAR["transNo"] = str(generator.timestamp())

    def teardown_class(self):
        Opt_json("reception.json").write_to_res_json(GLOBAL_VAR)

    @pytest.mark.parametrize("caseid, desc, precondition, parameterize, url, method, header, data, shared, check", data)
    def test_refund(self, caseid, desc, precondition, parameterize, url, method, header, data, shared, check):
        log.info("CaseId: <- {} ->".format(caseid))
        log.info("Desc: {}".format(desc))
        header = cotool().set_header(header)
        params = cotool().set_params(parameterize, data)
        res = httprequest(url, method, header, params)
        if shared:
            cotool.extract_variable(res, shared)
        cotool().assert_res(res, check)
        allure.dynamic.story("CaseID: < {} > - {}".format(caseid, desc))


if __name__ == '__main__':
    pytest.main(["-sx", "--reruns", "2",  "test_reception.py"])

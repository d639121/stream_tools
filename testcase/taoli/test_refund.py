#!/usr/bin/python 
# -*- coding: utf-8 -*-
# @Time    : 2020/5/29 14:59
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


data = OperationYAML().rafactor_data("/taoli/refund.yaml")


allure.feature("【桃李系统】投诉退款流程")
class TestRefund():

    def setup_class(self):
        GLOBAL_VAR["title"] = str("python测试%s" % generator.random_ean8())
        GLOBAL_VAR["phoneNumber"] = str(generator.random_phone_number())
        GLOBAL_VAR["transNo"] = str(generator.timestamp())

    def setup(self):
        time.sleep(1)

    def teardown_class(self):
        Opt_json("refund.json").write_to_res_json(GLOBAL_VAR)

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
    pytest.main(["-sx",  "test_refund.py"])
#!/usr/bin/python 
# -*- coding: utf-8 -*-
# @Time    : 2020/6/1 14:40
# @Author  : LOUIE

from utils.operation_json import OperationJson as Opt_json
from common.common_tools import CommonTools as cotool
from common.http_requests import httprequest
from common.config_log import log
from stream_tools.config.constant import GLOBAL_VAR
from utils.operation_yaml import OperationYAML
import pytest
import allure
import time


taoli_query_data = OperationYAML().rafactor_data("/platform/taoli_query.yaml")
crm_query_data = OperationYAML().rafactor_data("/platform/crm_query.yaml")
milky_way_query_data = OperationYAML().rafactor_data("/platform/milky_way_query.yaml")
haichuan_query_data = OperationYAML().rafactor_data("/platform/haichuan_query.yaml")
shishuo_query_data = OperationYAML().rafactor_data("/platform/shishuo_query.yaml")
xiaoka_query_data = OperationYAML().rafactor_data("/platform/xiaoka_query.yaml")
client_query_data = OperationYAML().rafactor_data("/platform/client_query.yaml")
operating_system_data = OperationYAML().rafactor_data("/platform/operating_system.yaml")
mobile_class_data = OperationYAML().rafactor_data("/platform/mobile_class.yaml")
all_data = []

for i in taoli_query_data:
    all_data.append(i)
for i in crm_query_data:
    all_data.append(i)
for i in milky_way_query_data:
    all_data.append(i)
for i in haichuan_query_data:
    all_data.append(i)
for i in shishuo_query_data:
    all_data.append(i)
for i in xiaoka_query_data:
    all_data.append(i)
for i in client_query_data:
    all_data.append(i)
# for i in mobile_class_data:
#     all_data.append(i)


allure.feature("【平台】查询接口测试")
class TestQuery():

    def setup(self):
        time.sleep(1)

    def teardown_class(self):
        Opt_json("query.json").write_to_res_json(GLOBAL_VAR)

    @pytest.mark.parametrize("caseid, desc, precondition, parameterize, url, method, header, data, shared, check", all_data)
    def test_mainlink(self, caseid, desc, precondition, parameterize, url, method, header, data, shared, check):
        log.info("CaseId: <- {} ->".format(caseid))
        log.info("Desc: {}".format(desc))
        header = cotool().set_header(header)
        params = cotool().set_params(parameterize, data)
        res = httprequest(url, method, header, params)
        if shared:
            cotool.extract_variable(res, shared)
        if check:
            cotool().assert_res(res, check)
        allure.dynamic.story("CaseID: < {} > - {}".format(caseid, desc))


if __name__ == '__main__':
    pytest.main(["-sl", __file__])

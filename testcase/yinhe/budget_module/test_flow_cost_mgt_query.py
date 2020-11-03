#!/usr/bin/python 
# @Time  : 2020/8/18 16:47
# @Author: Fold
# @Desc  : 流量成本管理
import allure
import pytest

from common.config_log import logger
from stream_tools.config.read_config import rc
from control.base.login import login
from control.yinhe.budget_module.flow_cost_mgt import FlowCostMgt


class TestFlowCostMgtPageList:

    def setup(self):
        if rc.get_env() == 'pre':
            login.login_action('t0322511032', '123456')
        else:
            login.login_action('t0384223793', '123456')
        self._fcm = FlowCostMgt()

    @logger('case')
    @allure.step('流量成本管理模块查询接口-无条件查询/重置')
    def test_flow_cost_list_blank(self):
        with allure.step('无条件查询/重置'):
            self._fcm.flow_cost_mgt_page_list()

    @logger('case')
    @allure.step('流量成本管理模块查询接口-翻页')
    def test_flow_cost_list_blank(self):
        with allure.step('无条件查询/翻页'):
            self._fcm.flow_cost_mgt_page_list(pageIndex=2)


    @logger('case')
    @allure.step('流量成本管理模块查询接口-成本月份查询')
    def test_flow_cost_list_month(self):
        with allure.step('成本月份查询'):
            self._fcm.flow_cost_mgt_page_list(startCostMonth=1593532800000, endCostMonth=1598889599999)

    @logger('case')
    @allure.step('流量成本管理模块查询接口-推广组织查询')
    def test_flow_cost_list_dept(self):
        with allure.step('推广组织查询'):
            self._fcm.flow_cost_mgt_page_list(promotionerDeptIdChain='1001-8006-8007-8008-8009')

    @logger('case')
    @allure.step('流量成本管理模块查询接口-科目id查询')
    def test_flow_cost_list_subject(self):
        with allure.step('科目查询'):
            self._fcm.flow_cost_mgt_page_list(subjectId=277)

    @logger('case')
    @allure.step('流量成本管理模块查询接口-渠道查询')
    def test_flow_cost_list_channel(self):
        with allure.step('渠道查询'):
            self._fcm.flow_cost_mgt_page_list(channelId=3)

    @logger('case')
    @allure.step('流量成本管理模块查询接口-投放模式查询')
    def test_flow_cost_list_mode(self):
        with allure.step('投放模式查询'):
            self._fcm.flow_cost_mgt_page_list(putMode=1)

    @logger('case')
    @allure.step('流量成本管理模块查询接口-获客方式查询')
    def test_flow_cost_list_gather(self):
        with allure.step('获客方式查询'):
            self._fcm.flow_cost_mgt_page_list(gatherType=1)

    @logger('case')
    @allure.step('流量成本管理模块查询接口-创建人查询')
    def test_flow_cost_list_creator(self):
        with allure.step('创建人查询'):
            self._fcm.flow_cost_mgt_page_list(creatorName='日常的阿魏')

    @logger('case')
    @allure.step('流量成本管理模块查询接口-创建时间查询')
    def test_flow_cost_list_time(self):
        with allure.step('创建时间查询'):
            self._fcm.flow_cost_mgt_page_list(startCreateTime=1596211200000, endCreateTime=1597766399999)

if __name__ == '__main__':
    # pytest.main(["-sl", __file__])
    pytest.main(["-sl",  "test_flow_cost_mgt_query.py"])

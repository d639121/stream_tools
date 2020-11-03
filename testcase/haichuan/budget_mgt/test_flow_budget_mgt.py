#!/usr/bin/python 
# @Time  : 2020/9/3 17:18
# @Author: Fold
# @Desc  : 流量预算管理
import datetime
import time
import allure

from common.config_log import logger
from control.base.login import login
from control.haichuan.budget_mgt.flow_budget_mgt import FlowBudgetMgt



class TestFlowBudgetMgt:

    def setup_class(self):
        login.login_action('t0385252771', '123456')

    def setup(self):
        self._fbm = FlowBudgetMgt()

    @logger('case')
    @allure.step('新增流量预算')
    def test_add_flow_budget(self):
        with allure.step('新增流量预算'):
            self._fbm.add_flow_budget()

    @logger('case')
    @allure.step('新增流量预算')
    def test_chk_flow_budget(self):
        with allure.step('查询未审核的流量预算'):
            self._fbm.qry_flow_budget()
        with allure.step('审核流量预算'):
            self._fbm.chk_flow_budget()
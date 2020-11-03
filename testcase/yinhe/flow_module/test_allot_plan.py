#!/usr/bin/python
# @Time   : 2020/8/12 11:35
# @Author : Jones
# @Desc   : 分配计划

from allure_commons._allure import step
from common.config_log import logger
from stream_tools.config.read_config import rc
from control.base.login import login
from control.yinhe.flow_module.allot_plan import AllotPlan


class TestAllotPlan:

    def setup(self):
        self.ap = AllotPlan()

    @step('查询-当日-分配计划')
    @logger('case')
    def test_query_allot_plan(self):
        self.ap.query_allot_plan()

    @step('查询-全部-分配计划')
    @logger('case')
    def test_query_allot_plan_all(self):
        res = self.ap.query_allot_plan(all=1)
        assert res['data']['totalItem'] > 10

    @step('查询-分配计划-无数据权限')
    @logger('case')
    def test_query_allot_plan_all(self):
        if rc.get_env() == 'pre':
            login.login_action('t0322511032')
        else:
            login.login_action('t0385252771')
        self.ap.query_allot_plan(all=1)

    @step('查询-投放计划')
    @logger('case')
    def test_query_put_plan(self):
        self.ap.query_put_plan()

    @step('导出-分配计划')
    @logger('case')
    def test_export_allot_plan(self):
        if rc.get_env() == 'pre':
            login.login_action('t0322511032')
        else:
            login.login_action('t0383212689')
        self.ap.export_allot_plan()

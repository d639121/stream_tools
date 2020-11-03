#!/usr/bin/python
# @Time   : 2020/8/18 15:00
# @Author : Jones
# @Desc   : 部门分配统计

from allure_commons._allure import step
from common.config_log import logger
from stream_tools.config.read_config import rc
from control.base.login import login
from control.yinhe.data_module.dept_allot_statistics import DeptAllotStatistics


class TestDeptAllotStatistical:

    def setup(self):
        self._das = DeptAllotStatistics()

    @step('数据/数据统计/部门分配统计-管理员查询')
    @logger('case')
    def test_query_dept_allot_for_admin(self):
        if rc.get_env() == 'pre':
            login.login_action('t0396753586')
        else:
            login.login_action('t0373492024')
        self._das.query_dept_allot_data()

    @step('数据/数据统计/部门分配统计-售前查询')
    @logger('case')
    def test_query_dept_allot_for_salary(self):
        if rc.get_env() == 'pre':
            login.login_action('t0322511032')
        else:
            login.login_action('t0385252771')
        self._das.query_dept_allot_data()

    @step('数据/数据统计/部门分配统计-翻页查询')
    @logger('case')
    def test_turn_page_query_dept_allot(self):
        if rc.get_env() == 'pre':
            login.login_action('t0322511032')
        else:
            login.login_action('t0373492024')
        self._das.query_dept_allot_data(pageIndex=2)

    @step('数据/数据统计/部门分配统计-导出')
    @logger('case')
    def test_export_dept_allot(self):
        if rc.get_env() == 'pre':
            login.login_action('t0322511032')
        else:
            login.login_action('t0373492024')
        self._das.export_dept_allot_data()

    # @step('数据/数据统计/部门分配统计-预约导出')
    # @logger('case')
    # 目前数据不足5000
    # def test_prepare_export_query_dept_allot(self):
    #     login.login_action('t0373492024')
    #     self._das.export_dept_allot_data()

    @step('数据/数据统计/部门分配统计-微信CPC-管理员查询')
    @logger('case')
    def test_query_wx_dept_allot_for_admin(self):
        if rc.get_env() == 'pre':
            login.login_action('t0391689807')
        else:
            login.login_action('t0373492024')
        self._das.query_wx_dept_allot_data()
        # assert int(GLOBAL_VAR['totalItem']) > 0

    @step('数据/数据统计/部门分配统计-微信CPC-售前查询')
    @logger('case')
    def test_query_wx_dept_allot_for_salary(self):
        if rc.get_env() == 'pre':
            login.login_action('t0322511032')
        else:
            login.login_action('t0385252771')
        self._das.query_wx_dept_allot_data()

    @step('数据/数据统计/部门分配统计-微信CPC-翻页查询')
    @logger('case')
    def test_turn_page_wx_query_dept_allot(self):
        if rc.get_env() == 'pre':
            login.login_action('t0322511032')
        else:
            login.login_action('t0373492024')
        self._das.query_wx_dept_allot_data(pageIndex=2)

    @step('数据/数据统计/部门分配统计-微信CPC-导出')
    @logger('case')
    def test_export_wx_dept_allot(self):
        if rc.get_env() == 'pre':
            login.login_action('t0322511032')
        else:
            login.login_action('t0373492024')
        self._das.export_wx_dept_allot_data()

    # @step('数据/数据统计/部门分配统计-微信CPC-预约导出')
    # @logger('case')
    # 目前数据不足5000
    # def test_prepare_wx_export_query_dept_allot(self):
    #     login.login_action('t0373492024')
    #     self._das.export_wx_dept_allot_data()
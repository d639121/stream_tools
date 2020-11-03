#!/usr/bin/python
# @Time   : 2020/8/18 15:00
# @Author : Jones
# @Desc   : 部门成单统计

from allure_commons._allure import step
from common.config_log import logger
from stream_tools.config.read_config import rc
from control.base.login import login
from control.yinhe.data_module.dept_order_statistics import DeptOrderStatistics


class TestDeptOrderStatistical:

    def setup(self):
        self._dos = DeptOrderStatistics()

    @step('数据/数据统计/部门成单统计-管理员查询')
    @logger('case')
    def test_query_dept_order_for_admin(self):
        if rc.get_env() == 'pre':
            login.login_action('t0391689807')
        else:
            login.login_action('t0373492024')
        self._dos.query_dept_order_data()

    @step('数据/数据统计/部门成单统计-售前查询')
    @logger('case')
    def test_query_dept_order_for_sales(self):
        if rc.get_env() == 'pre':
            login.login_action('t0322511032')
        else:
            login.login_action('t0385252771')
        self._dos.query_dept_order_data()

    @step('数据/数据统计/部门成单统计-翻页查询')
    @logger('case')
    def test_turn_page_query_dept_order(self):
        if rc.get_env() == 'pre':
            login.login_action('t0322511032')
        else:
            login.login_action('t0373492024')
        self._dos.query_dept_order_data(pageIndex=2)

    @step('数据/数据统计/部门成单统计-导出')
    @logger('case')
    def test_export_dept_order_data(self):
        if rc.get_env() == 'pre':
            login.login_action('t0322511032')
        else:
            login.login_action('t0373492024')
        self._dos.export_dept_order_data()

    # @step('数据/数据统计/部门成单统计-预约导出')
    # @logger('case')
    # 目前数据需要超过5000才能进行预约导出
    # def test_prepare_export_dept_order_data(self):
    #     login.login_action('t0373492024')
    #     local_time = GLOBAL_VAR['yesterday']
    #     self._dos.export_dept_order_data(queryParams='{"来源日期":"2019-07-01 至 %s"}' % local_time)

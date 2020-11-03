#!/usr/bin/python
# @Time   : 2020/8/18 15:00
# @Author : Jones
# @Desc   : 流量分配统计

from allure_commons._allure import step
from common.config_log import logger
from stream_tools.config.constant import GLOBAL_VAR
from stream_tools.config.read_config import rc
from control.base.login import login
from control.yinhe.data_module.flow_allot_statistics import FlowAllotStatistics


class TestFlowAllotStatistical:

    def setup(self):
        self._fas = FlowAllotStatistics()

    @step('数据/数据统计/流量分配统计-管理员查询')
    @logger('case')
    def test_query_flow_allot_for_admin(self):
        if rc.get_env() == 'pre':
            login.login_action('t0396753586')
        else:
            login.login_action('t0373492024')
        self._fas.query_flow_allot_data()
        assert int(GLOBAL_VAR['totalItem']) > 0

    @step('数据/数据统计/流量分配统计-售前查询')
    @logger('case')
    def test_query_flow_allot_for_sales(self):
        if rc.get_env() == 'pre':
            login.login_action('t0322511032')
        else:
            login.login_action('t0385252771')
        self._fas.query_flow_allot_data()
        # 目前该查询有结果返回，已通知相关业务人员，确认该问题暂时不用解决

    @step('数据/数据统计/流量分配统计-管理员翻页查询')
    @logger('case')
    def test_query_flow_allot_for_admin_turn_page(self):
        if rc.get_env() == 'pre':
            login.login_action('t0322511032')
        else:
            login.login_action('t0373492024')
        self._fas.query_flow_allot_data(pageIndex=2)
        assert int(GLOBAL_VAR['totalItem']) > 0

    @step('数据/数据统计/流量分配统计-导出')
    @logger('case')
    def test_export_flow_allot(self):
        if rc.get_env() == 'pre':
            login.login_action('t0322511032')
        else:
            login.login_action('t0373492024')
        self._fas.export_flow_allot_data()

    # @step('数据/数据统计/流量分配统计-预约导出')
    # @logger('case')
    # 数据需要5000条才能执行预约导出，目前数据不足
    # def test_prepare_export_flow_allot(self):
    #     login.login_action('t0373492024')
    #     self._fas.export_flow_allot_data()

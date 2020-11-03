#!/usr/bin/python
# @Time   : 2020/8/12 11:35
# @Author : Jones
# @Desc   : 流量申请记录

from allure_commons._allure import step
from common.config_log import logger
from control.yinhe.flow_module.flow_apply_record import FlowApplyRecord


class TestFlowApplyRecord:

    def setup(self):
        self._far = FlowApplyRecord()

    @step('查询-流量申请记录')
    @logger('case')
    def test_flow_apply_record_query(self):
        self._far.flow_apply_record_query()

    @step('导出-流量申请记录')
    @logger('case')
    def test_export_flow_apply_record(self):
        self._far.export_flow_apply_record()

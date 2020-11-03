#!/usr/bin/python
# @Time  : 2020/8/31 16:26
# @Author: Fold
# @Desc  : 流量成本管理-导出

import allure
from common.config_log import logger
from stream_tools.config.read_config import rc
from control.base.login import login
from control.yinhe.budget_module.flow_cost_mgt import FlowCostMgt


class TestFlowCostMgtExport:

    def setup_class(self):
        if rc.get_env() == 'pre':
            login.login_action('t0322511032', '123456')
        else:
            login.login_action('t0384223793', '123456')

    def setup(self):
        self._fcm = FlowCostMgt()

    @logger('case')
    @allure.step('流量成本管理-流量成本导出，导出默认的所有文件（小于5000条数据）')
    def test_flow_cost_mgt_export_all(self):
        with allure.step('导出excel文件'):
            self._fcm.flow_cost_mgt_export()

    @logger('case')
    @allure.step('流量成本管理-流量成本导出，导出符合查询条件的文件（小于5000条数据）')
    def test_flow_cost_mgt_export_eligible(self):
        with allure.step('导出符合条件excel文件'):
            self._fcm.flow_cost_mgt_export(startCostMonth=1598889600000, endCostMonth=1601481599999)


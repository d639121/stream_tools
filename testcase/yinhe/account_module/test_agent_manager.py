#!/usr/bin/python 
# @Time  : 2020/8/27 18:18
# @Author: LOUIE
# @Desc  : 代理商管理

from common.config_log import logger
from stream_tools.config.read_config import rc
from control.base.login import login
from control.yinhe.account_module.agent_manager import AgentManager
import allure


@allure.feature('代理商管理')
class TestAgentManager:

    def setup_class(self):
        if rc.get_env() == 'pre':
            login.login_action('t0396753586')
        else:
            login.login_action('t0373492024')
        self.am = AgentManager()

    @logger('case')
    @allure.step('查询代理商列表')
    def test_agent_pagelist(self):
        self.am.agent_pageList(channelId=6)

    @logger('case')
    @allure.step('查询返点列表')
    def test_rebate_pagelist(self):
        self.am.rebate_pageList()

    @logger('case')
    @allure.step('导出代理商列表')
    def test_export_agent_record(self):
        self.am.export_record()

    @logger('case')
    @allure.step('导出返点列表')
    def test_export_rebate_record(self):
        self.am.export_rebate_record()



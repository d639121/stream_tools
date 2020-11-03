#!/usr/bin/python 
# @Time  : 2020/8/27 18:18
# @Author: LOUIE
# @Desc  : 投放账户管理

from common.config_log import logger
from stream_tools.config.read_config import rc
from control.base.login import login
from control.yinhe.account_module.put_account_manager import PutAccountManager
import allure


@allure.feature('投放账户管理')
class TestPutAccountManager:

    def setup_class(self):
        if rc.get_env() == 'pre':
            login.login_action('t0322511032')
        else:
            login.login_action('t0373492024')
        self.pam = PutAccountManager()

    @logger('case')
    @allure.step('查询 账户信息列表')
    def test_account_pagelist(self):
        self.pam.account_pagelist()

    @logger('case')
    @allure.step('查询 使用信息列表')
    def test_useage_pagelist(self):
        self.pam.useage_pagelist()

    @logger('case')
    @allure.step('导出 账户信息列表')
    def test_export_account_pagelist(self):
        res = self.pam.export_account_pagelist()
        assert res.status_code == 200

    @logger('case')
    @allure.step('导出 使用信息列表')
    def test_export_useage_pagelist(self):
        res = self.pam.export_useage_pagelist()
        assert res.status_code == 200



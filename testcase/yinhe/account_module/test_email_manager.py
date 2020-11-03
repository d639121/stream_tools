#!/usr/bin/python 
# @Time  : 2020/10/23 17:22
# @Author: LOUIE
# @Desc  : 邮件管理

from common.config_log import logger
from control.base.login import login
from control.yinhe.account_module.email_manager import EmailManager
import allure


@allure.feature('邮件管理')
class TestAgentManager:

    def setup_class(self):
        login.login_action('t0373492024')
        self.em = EmailManager()

    @logger('case')
    @allure.step('查询邮件管理列表-微信渠道-状态未发送')
    def test_mail_pagelist(self):
        self.em.mail_pagelist()

    @logger('case')
    @allure.step('查询列表-渠道哔哩哔哩-状态已发送')
    def test_mail_pagelist(self):
        self.em.mail_pagelist(channelId=3, state='1')
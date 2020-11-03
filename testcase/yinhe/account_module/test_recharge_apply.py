#!/usr/bin/python 
# @Time  : 2020/8/4 16:06
# @Author: LOUIE
# @Desc  : 测试投放账户充值申请
from allure_commons._allure import step

from common.config_log import logger
from stream_tools.config.constant import GLOBAL_VAR, const
from control.base.login import login
from control.yinhe.account_module.agent_manager import AgentManager
from control.yinhe.account_module.put_account_manager import PutAccountManager
from control.yinhe.account_module.recharge_apply_record import RechargeApplyRecord
import allure
import pytest

from control.yinhe.account_module.recharge_transfer_record import RechargeTransferRecord


@allure.feature('测试投放账户充值申请')
class TestRechargeApply:
    
    def setup_class(self):   
        self.pam = PutAccountManager()
        self.rar = RechargeApplyRecord()
        self.am = AgentManager()
        self.rtr = RechargeTransferRecord()
        GLOBAL_VAR['RandomChinese'] = const.random_chinese
        GLOBAL_VAR['transNo'] = const.transNo

    @pytest.mark.skip
    @allure.step('测试充值申请')
    @logger('case')
    def test_recharge_apply(self):
        login.login_action('t0395392291')
        self.pam.recharge_application()
        self.rar.apply_list()
        login.login_action('t0383212689')
        self.rar.rejected_apply()
        login.login_action('t0395392291')
        self.rar.updated_apply()
        login.login_action('t0383212689')
        self.rar.passed_apply()
        login.login_action('t0373492024')
        self.rar.passed_apply()
        self.rar.processed_apply()
        login.login_action('t0395392291')
        self.rar.received_affirm()
        login.login_action('t0383212689')
        self.rtr.recharge_pageList(channelId=6)
        self.rtr.principal_received_affirm()
        login.login_action('t0373492024')
        self.em.mail_pagelist()
        self.em.send_mail()

    @allure.step('导出充值申请记录列表')
    @logger('case')
    def test_export_record(self):
        self.rar.export_record()

    @allure.step('测试充值退款')
    @logger('case')
    def test_recharge_refund(self):
        with step('充值申请'):
            login.login_action('t0395392291')
            self.pam.recharge_application(id=229)
            self.rar.apply_list(accountCode='1111111122')
        with step('负责人通过审批'):
            login.login_action('t0383212689')
            self.rar.passed_apply()
            login.login_action('t0373492024')
            self.rar.passed_apply()
        with step('生成邮件'):
            login.login_action('t0373492024')
            self.rar.send_email()
        with step('小伙伴确认到账'):
            login.login_action('t0395392291')
            self.rar.received_affirm()
        with step('负责人确认到账'):
            login.login_action('t0383212689')
            self.rtr.recharge_pageList(rechargeApplyRecordId=GLOBAL_VAR['applyId'])
            self.rtr.principal_received_affirm()
        with step('充值退款'):
            self.am.qry_channel_agency(agencyShortName='大佬')
            self.pam.account_pagelist(agencyShortName='大佬')
            login.login_action('t0373492024')
            self.rtr.recharge_refund()



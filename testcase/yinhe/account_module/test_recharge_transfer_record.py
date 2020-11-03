#!/usr/bin/python 
# @Time  : 2020/8/27 18:04
# @Author: LOUIE
# @Desc  : 充值转账记录

from common.config_log import logger
from stream_tools.config.read_config import rc
from control.base.login import login
from control.yinhe.account_module.recharge_transfer_record import RechargeTransferRecord
import allure


@allure.feature('充值转账记录')
class TestRechargeTransferRecord:

    def setup_class(self):
        if rc.get_env() == 'pre':
            login.login_action('t0322511032')
        else:
            login.login_action('t0373492024')
        self.rtr = RechargeTransferRecord()

    @logger('case')
    @allure.step('查询充值记录')
    def test_recharge_pageList(self):
        self.rtr.recharge_pageList()

    @logger('case')
    @allure.step('查询转账记录')
    def test_transfer_pagelist(self):
        self.rtr.transfer_pageList()

    # 由于新版本引起的异常
    @logger('case')
    @allure.step('导出充值记录')
    def test_export_recharge_pageList(self):
        res = self.rtr.export_recharge_pageList()
        assert res.status_code == 200

    @logger('case')
    @allure.step('导出转账记录')
    def test_export_transfer_pageList(self):
        res = self.rtr.export_transfer_pageList()
        assert res.status_code == 200

#!/usr/bin/python 
# @Time  : 2020/8/1 17:53
# @Author: LOUIE
# @Desc  : 充值申请记录

from utils.get_api_data import get_data
from common.common_tools import cotool
from common.config_log import logger
import allure


class RechargeApplyRecord:

    def __init__(self):
        self._data = get_data.get_yinhe_data('account_module/recharge_apply_record.yaml')

    @allure.step('充值申请记录列表')
    @logger()
    def apply_list(self, **kwargs):
        data = self._data['apply_list']
        cotool.quick_request(data, **kwargs)

    @allure.step('负责人/SOP 通过充值申请')
    @logger()
    def passed_apply(self):
        data = get_data.get_yinhe_data('account_module/recharge_apply_record.yaml')
        data = data['passed_apply']
        cotool.quick_request(data)

    @allure.step('修改充值申请')
    @logger()
    def updated_apply(self):
        data = self._data['updated_apply']
        cotool.quick_request(data)

    @allure.step('负责人驳回充值申请')
    @logger()
    def rejected_apply(self):
        data = self._data['rejected_apply']
        cotool.quick_request(data)

    @allure.step('SOP管理员打款')
    @logger()
    def processed_apply(self):
        data = self._data['processed_apply']
        cotool.quick_request(data)

    @allure.step('小伙伴到账确认')
    @logger()
    def recharge_confirm(self):
        data = self._data['recharge_confirm']
        cotool.quick_request(data)

    @allure.step('小伙伴到账确认-带邮件')
    @logger()
    def received_affirm(self):
        data = self._data['received_affirm']
        cotool.quick_request(data)

    @allure.step('导出充值申请记录')
    @logger()
    def export_record(self):
        data = self._data['export_record']
        cotool.quick_request(data)

    @allure.step('生成邮件')
    @logger()
    def send_email(self):
        data = self._data['send_email']
        cotool.quick_request(data)


if __name__ == '__main__':
    from control.base.login import login
    from control.yinhe.account_module.put_account_manager import PutAccountManager
    from control.yinhe.account_module.email_manager import EmailManager
    from control.yinhe.account_module.recharge_transfer_record import RechargeTransferRecord
    pam = PutAccountManager()
    rar = RechargeApplyRecord()
    em = EmailManager()
    rtr = RechargeTransferRecord()
    login.login_action('t0395392291')
    pam.recharge_application()
    rar.apply_list()
    login.login_action('t0383212689')
    rar.rejected_apply()
    login.login_action('t0376248125')
    rar.updated_apply()
    login.login_action('t0383212689')
    rar.passed_apply()
    login.login_action('t0373492024')
    rar.passed_apply()
    # rar.processed_apply()
    em.generate_mail()
    login.login_action('t0395392291')
    rar.received_affirm()
    login.login_action('t0383212689')
    rtr.recharge_pageList(channelId=6)
    rtr.principal_received_affirm()


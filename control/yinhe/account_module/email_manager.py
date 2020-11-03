#!/usr/bin/python 
# @Time  : 2020/10/23 15:09
# @Author: LOUIE
# @Desc  : 邮件管理

from utils.get_api_data import get_data
from common.common_tools import cotool
from common.config_log import logger


class EmailManager:

    def __init__(self):
        self._data = get_data.get_yinhe_data('account_module/email_manager.yaml')

    @logger()
    def mail_pagelist(self, **kwargs):
        '''
        邮件管理列表
        :param channelId: 渠道: 6.微信  3.哔哩哔哩
        :param state: 状态: 0.未发送  1.已发送
        :return:
        '''
        data = self._data['mail_pagelist']
        cotool.quick_request(data, **kwargs)

    @logger()
    def generate_mail(self, **kwargs):
        '''
        生成邮件，此按钮在充值申请记录页面
        :param ids: 充值申请ID
        :return:
        '''
        data = self._data['generate_mail']
        cotool.quick_request(data, **kwargs)

    @logger()
    def generate_email(self, **kwargs):
        '''
        生成邮件，此按钮在充值申请记录页面
        :param ids: 充值申请ID
        :return:
        '''
        data = self._data['generate_mail']
        res = cotool.quick_rqt(data, **kwargs)
        return res

    @logger()
    def send_mail(self, **kwargs):
        '''
        发送邮件
        :param ids: 充值申请ID
        :return:
        '''
        data = self._data['send_mail']
        cotool.quick_request(data, **kwargs)

    @logger()
    def send_email(self, **kwargs):
        '''
        发送邮件
        :param ids: 充值申请ID
        :return:
        '''
        data = self._data['send_mail']
        res = cotool.quick_rqt(data, **kwargs)
        return res
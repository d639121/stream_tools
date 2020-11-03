#!/usr/bin/python 
# @Time  : 2020/8/1 17:53
# @Author: LOUIE
# @Desc  : 充值转账记录

from utils.get_api_data import get_data
from common.common_tools import cotool
from common.config_log import logger


class RechargeTransferRecord:

    def __init__(self):
        self._data = get_data.get_yinhe_data('account_module/recharge_transfer_record.yaml')

    @logger()
    def recharge_pageList(self, **kwargs):
        '''
        充值记录
        :param channelId: 渠道ID： 3.哔哩哔哩
        '''
        data = self._data['recharge_pageList']
        cotool.quick_request(data, **kwargs)

    @logger()
    def transfer_pageList(self, **kwargs):
        '''
        转账记录
        :param channelId: 渠道ID： 3.哔哩哔哩
        '''
        data = self._data['transfer_pageList']
        cotool.quick_request(data, **kwargs)

    @logger()
    def principal_received_affirm(self, **kwargs):
        '''
        负责人到账确认
        '''
        data = self._data['principal_received_affirm']
        cotool.quick_request(data, **kwargs)

    @logger()
    def export_recharge_pageList(self, **kwargs):
        '''
        导出充值记录
        :param channelId: 渠道ID： 3.哔哩哔哩
        '''
        data = self._data['export_recharge_pageList']
        res = cotool.quick_request(data, **kwargs)
        return res

    @logger()
    def export_transfer_pageList(self, **kwargs):
        '''
        导出转账记录
        :param channelId: 渠道ID： 3.哔哩哔哩
        '''
        data = self._data['export_transfer_pageList']
        res = cotool.quick_request(data, **kwargs)
        return res

    @logger()
    def recharge_refund(self, **kwargs):
        '''
        充值退款
        :param
        '''
        data = self._data['recharge_refund']
        res = cotool.quick_request(data, **kwargs)
        return res

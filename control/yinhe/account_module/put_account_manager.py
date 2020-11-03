#!/usr/bin/python 
# @Time : 2020/8/1 17:53
# @Author : LOUIE
# @Desc : 投放账户管理

from utils.get_api_data import get_data
from common.common_tools import cotool
from common.config_log import logger


class PutAccountManager:

    def __init__(self):
        self._data = get_data.get_yinhe_data('account_module/put_account_manager.yaml')

    @logger()
    def recharge_application(self, **kwargs):
        '''
        充值申请
        :param kwargs:
        :return:
        '''
        data = self._data['recharge_application']
        cotool.quick_request(data, **kwargs)

    @logger()
    def account_pagelist(self, **kwargs):
        '''
        账户信息列表
        :param channelId: 渠道编号： 1.广点通
        :return:
        '''
        data = self._data['account_pagelist']
        cotool.quick_request(data, **kwargs)

    @logger()
    def useage_pagelist(self, **kwargs):
        '''
        使用信息列表
        :param channelId: 渠道编号： 1.广点通
        :return:
        '''
        data = self._data['useage_pagelist']
        cotool.quick_request(data, **kwargs)

    @logger()
    def export_account_pagelist(self, **kwargs):
        '''
        导出 账户信息列表
        :param channelId: 渠道编号： 1.广点通
        :return:
        '''
        data = self._data['export_account_pagelist']
        res = cotool.quick_request(data, **kwargs)
        return res

    @logger()
    def export_useage_pagelist(self, **kwargs):
        '''
        导出 使用信息列表
        :param channelId: 渠道编号： 1.广点通
        :return:
        '''
        data = self._data['export_useage_pagelist']
        res = cotool.quick_request(data, **kwargs)
        return res

    @logger()
    def add_account(self, **kwargs):
        '''
        新增投放账户
        :return:
        '''
        data = self._data['add_put_account']
        res = cotool.quick_request(data, **kwargs)
        return res

    @logger()
    def associated_promoter(self, **kwargs):
        '''
        关联推广人(该方法需要传部门id相关参数，建议使用该方法时先明确所在院的相关参数)
        :return:
        '''
        data = self._data['associated_promoter']
        res = cotool.quick_request(data, **kwargs)
        return res

    @logger()
    def add_acc(self, **kwargs):
        '''
        新增投放账户
        :return:
        '''
        data = self._data['add_account']
        res = cotool.quick_rqt(data, **kwargs)
        return res

    @logger()
    def associated_pt(self, **kwargs):
        '''
        关联推广人(该方法需要传部门id相关参数，建议使用该方法时先明确所在院的相关参数)
        :return:
        '''
        data = self._data['associated_promoter']
        res = cotool.quick_rqt(data, **kwargs)
        return res
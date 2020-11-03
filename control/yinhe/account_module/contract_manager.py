#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File Name  : contract_manager.py
# Description : 合同管理
# @Time       : 2020/10/22 16:05
# @Author     : Jones
from common.common_tools import cotool
from common.config_log import logger
from utils.get_api_data import get_data


class ContractManager:
    def __init__(self):
        self._data = get_data.get_yinhe_data('account_module/contract_manager.yaml')

    @logger()
    def create_contract(self, **kwargs):
        '''
        新建合同
        :return:
        '''
        data = self._data['create_contract']
        cotool.quick_rqt(data, **kwargs)

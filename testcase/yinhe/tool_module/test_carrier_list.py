#!/usr/bin/python 
# @Time  : 2020/8/7 17:53
# @Author: Fold
# @Desc  : 载体管理
import allure
import pytest

from common.config_log import logger
from control.yinhe.tool_module.carrier_mgt import CarrierMgt


class Testcarrierlist:

    def setup(self):
        self._cm = CarrierMgt()

    @logger('case')
    @allure.step('载体查询')
    def test_carrier_list(self):
        with allure.step('载体查询'):
            self._cm.carrier_list(followNick='KIMI的售前院负责人')



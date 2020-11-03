#!/usr/bin/python 
# @Time  : 2020/8/3 17:47
# @Author: LOUIE
# @Desc  : 载体管理-新增载体

from control.yinhe.tool_module.carrier_mgt import CarrierMgt
from stream_tools.config.constant import const
from common.config_log import logger
import allure
import pytest


class TestAddCarrier:

    def setup(self):
        self.qq = const.qq
        self.mobile = const.phoneNumber
        self.carrier_mgt = CarrierMgt()

    def teardown(self):
        pass

    @logger('case')
    @allure.step('新增个人微信载体')
    def test_add_wechat_carrier(self):
        self.carrier_mgt.add_carrier(type=1, carrierNo=self.mobile)

    @logger('case')
    @allure.step('新增QQ群载体')
    def test_add_qq_group_carrier(self):
        self.carrier_mgt.add_carrier(type=2, carrierNo=self.qq)

    @pytest.mark.skip()
    @logger('case')
    @allure.step('新增企业微信载体')
    def test_add_enterprise_wechat_carrier(self):
        self.carrier_mgt.add_carrier(type=3)




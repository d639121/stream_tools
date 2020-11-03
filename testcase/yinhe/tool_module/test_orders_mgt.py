#!/usr/bin/python 
# @Time  : 2020/8/10 20:36
# @Author: Fold
# @Desc  : 订单管理查询

import allure
from common.config_log import logger
from control.yinhe.tool_module.order_mgt import OrderMgt


class TestOrdersMgt:

    def setup(self):
        self._om = OrderMgt()

    @logger('case')
    @allure.step('订单查询')
    def test_orders_manage(self):
        with allure.step('载体查询'):
            self._om.orders_manage(isCreateWorksheet=1)


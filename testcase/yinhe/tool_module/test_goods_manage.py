#!/usr/bin/python
# @Time  : 2020/8/10 20:09
# @Author: Fold
# @Desc  : 商品管理查询

import allure
import pytest

from common.config_log import logger
from control.yinhe.tool_module.goods_manage import GoodsManage


class TestGoodsMange:

    def setup(self):
        self._gm = GoodsManage()

    @logger('case')
    @allure.step('商品查询')
    def test_good_manage(self):
        with allure.step('商品查询'):
            self._gm.goods_manage(teachingMethod='8010')


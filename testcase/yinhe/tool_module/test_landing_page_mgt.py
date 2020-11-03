#!/usr/bin/python 
# @Time  : 2020/8/11 18:22
# @Author: LOUIE
# @Desc  : 测试落地页管理

from control.yinhe.tool_module.landing_page_mgt import LandingPageMgt
from common.config_log import logger
import allure


class TestLandingPageMgt:

    def setup(self):
        self.lpm = LandingPageMgt()

    @logger('case')
    @allure.step('查询落地管理列表')
    def test_page_list(self):
        self.lpm.page_list(name=None)



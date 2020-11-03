#!/usr/bin/python 
# @Time  : 2020/8/7 17:31
# @Author: Fold
# @Desc  : 落地页数据测试用例

import allure
import pytest
from common.config_log import logger
from control.yinhe.tool_module.website_link_data import WebsiteLinkData


class TestWebsiteLinkData:
    def setup(self):
        self._wsd = WebsiteLinkData()

    @logger('case')
    @allure.step('落地页数据查询')
    def test_list_creativity(self):
        with allure.step('落地页数据查询'):
            self._wsd.list_creativity(submitStartTime='2020-08-07 00:00:00', submitEndTime='2020-08-07 23:59:59')


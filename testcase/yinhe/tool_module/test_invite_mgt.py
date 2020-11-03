#!/usr/bin/python 
# @Time  : 2020/8/7 15:26
# @Author: Fold
# @Desc  : 邀课引流管理查询
import allure
import pytest

from common.config_log import logger
from control.yinhe.tool_module.invite_mgt import InvitationMgt


class TestInviteMgt:

    def setup(self):
        self._im = InvitationMgt()

    @logger('case')
    @allure.step('邀课引流管理查询')
    def test_invited_management_query(self):
        with allure.step('邀课引流管理查询'):
            self._im.diversion_list(status = 1)


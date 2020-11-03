#!/usr/bin/python 
# @Time  : 2020/8/7 16:22
# @Author: Fold
# @Desc  : 邀课引流统计查询
import allure
import pytest

from common.config_log import logger
from control.yinhe.tool_module.invite_statistics import InvitationStatistics


class TestInviteStatistics:

    def setup(self):
        self._is = InvitationStatistics()

    @logger('case')
    @allure.step('邀课引流统计查询')
    def test_invite_statistics(self):
        with allure.step('邀课引流统计查询'):
            self._is.free_statistics(roleType = 2)


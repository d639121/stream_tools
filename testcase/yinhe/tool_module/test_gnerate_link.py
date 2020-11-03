#!/usr/bin/python 
# @Time  : 2020/8/3 17:14
# @Author: LOUIE
# @Desc  : 邀课引流管理

from control.yinhe.tool_module.invite_mgt import InvitationMgt
import allure
from common.config_log import logger


class TestGnerateLink:

    def setup_class(self):
        self.invitation_mgt = InvitationMgt()

    @allure.step('测试生成二维码链接')
    @logger('case')
    def test_gnerate_link(self):
        self.invitation_mgt.generate_link()


if __name__ == '__main__':
    import pytest
    pytest.main([__file__])
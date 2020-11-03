#!/usr/bin/python 
# @Time  : 2020/8/7 16:40
# @Author: Fold
# @Desc  : 兼职工具

from common.config_log import logger
from stream_tools.config.constant import const, GLOBAL_VAR
from control.yinhe.tool_module.part_time_tool import PartTimeTool
from control.tzkt.base.login_tzkt import LoginTZKT
from control.base.login import login
from control.yinhe.flow_module.student_input import StudentInput
import allure


class TestPartTimeTool:

    def setup(self):
        GLOBAL_VAR['phoneNumber'] = const.phoneNumber
        self._ptt = PartTimeTool()
        self.tzkt = LoginTZKT()

    @logger('case')
    @allure.step('兼职工具列表查询')
    def test_part_time_pagelist(self):
        with allure.step('邀课引流管理查询'):
            res = self._ptt.part_time_pagelist(nick='普通兼职')
            assert res['data']['totalItem'] >= 2

    @logger('case')
    @allure.step('新增普通兼职')
    def test_add_gneral_employee(self):
        with allure.step('注册潭州课堂账号'):
            self.tzkt.register_tzkt()
        with allure.step('新增普通兼职'):
            self._ptt.add_employee(type=11)

    @logger('case')
    @allure.step('新增高级兼职')
    def test_add_high_employee(self):
        with allure.step('注册潭州课堂账号'):
            self.tzkt.register_tzkt()
        with allure.step('新增高级兼职'):
            self._ptt.add_employee(type=12)

    @logger('case')
    @allure.step('新增超级兼职')
    def test_add_super_employee(self):
        with allure.step('注册潭州课堂账号'):
            self.tzkt.register_tzkt()
        with allure.step('新增超级兼职'):
            self._ptt.add_employee(type=13)

    @logger('case')
    @allure.step('调动兼职员工')
    def test_move_employee(self):
        with allure.step('调动兼职员工'):
            self._ptt.move_employee()

    @logger('case')
    @allure.step('禁用兼职员工')
    def test_forbid_employee(self):
        with allure.step('禁用兼职员工'):
            self._ptt.forbid_employee()

    @logger('case')
    @allure.step('启用兼职员工')
    def test_forbid_employee(self):
        with allure.step('启用兼职员工'):
            self._ptt.forbid_employee(status=1)

    @logger('case')
    @allure.step('编辑兼职员工')
    def test_edit_employee(self):
        with allure.step('编辑兼职员工'):
            self._ptt.edit_employee()

    @logger('case')
    @allure.step('普通兼职员工导入流量-无数据权限')
    def test_edit_employee(self):
        token = login.login_action('testuser1608', password='888888')
        StudentInput().import_wx_flow_free(token=token, type=2)
    @logger('case')
    @allure.step('高级兼职员工导入流量-无数据权限')
    def test_edit_employee(self):
        token = login.login_action('testuser1608', password='888888')
        StudentInput().import_wx_flow_free(token=token, type=2)

    @logger('case')
    @allure.step('超级兼职员工导入流量-无数据权限')
    def test_edit_employee(self):
        token = login.login_action('testuser1608', password='888888')
        StudentInput().import_wx_flow_free(token=token, type=2)
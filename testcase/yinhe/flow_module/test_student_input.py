#!/usr/bin/python
# @Time    : 2020/7/28 10:30
# @Author  : Jones
# @Desc : 学员录入--录入，导入

from allure_commons._allure import step
from stream_tools.config.constant import GLOBAL_VAR, const
from control.yinhe.flow_module.student_input import StudentInput
from common.config_log import logger
import time


class TestStudentInput:
    def setup_class(self):
        self._si = StudentInput()

    def setup(self):
        GLOBAL_VAR['qq'] = const.qq
        GLOBAL_VAR['phoneNumber'] = const.phoneNumber

    def teardown(self):
        time.sleep(1)

    @logger('case')
    @step('学员录入--录入（手机流量）--拥有【免费流量组】')
    def test_input_phone_flow_free(self):
        self._si.add_student(type=1, token=1)

    @logger('case')
    @step('学员录入--录入（手机流量）--未拥有【免费流量组】')
    def test_input_phone_flow_not_free(self):
        self._si.add_student(type=1, token=2)

    @logger('case')
    @step('【学员录入】--录入（QQ流量）--拥有【免费流量组】')
    def test_input_qq_flow_free(self):
        self._si.add_student(type=2, token=1)

    @logger('case')
    @step('【学员录入】--录入（QQ流量）未拥有【免费流量组】')
    def test_input_qq_flow_not_free(self):
        self._si.add_student(type=2, token=2)

    @logger('case')
    @step('【学员录入】--录入（微信流量）--拥有【免费流量组】')
    def test_input_wx_flow_free(self):
        self._si.add_student(type=3, token=1)

    @logger('case')
    @step('【学员录入】--录入（微信流量）--未拥有【免费流量组】')
    def test_input_wx_flow_not_free(self):
        self._si.add_student(type=3, token=2)

    @logger('case')
    @step('学员录入--导入（手机流量）--未拥有【免费流量组】')
    def test_import_phone_flow_not_free(self):
        self._si.import_phone_flow_not_free()

    @logger('case')
    @step('学员录入--导入（手机流量）--拥有【免费流量组】')
    def test_import_phone_flow_free(self):
        self._si.import_phone_flow_free()

    @logger('case')
    @step('学员录入--导入（QQ流量）--拥有【免费流量组】')
    def test_import_qq_flow_free(self):
        self._si.import_qq_flow_free()

    @logger('case')
    @step('学员录入--导入（QQ流量）--未拥有【免费流量组】')
    def test_import_qq_flow_not_free(self):
        self._si.import_qq_flow_not_free()

    @logger('case')
    @step('学员录入--导入（微信流量）--未拥有【免费流量组】')
    def test_import_wx_flow_not_free(self):
        self._si.import_wx_flow_not_free()

    @logger('case')
    @step('学员录入--导入（微信流量）--拥有【免费流量组】')
    def test_import_wx_flow_free(self):
        self._si.import_wx_flow_free()

    @logger('case')
    @step('学员录入--查询')
    def test_query(self):
        self._si.student_input_query()

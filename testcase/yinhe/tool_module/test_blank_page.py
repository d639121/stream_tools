#!/usr/bin/python 
# @Time  : 2020/8/11 14:15
# @Author: Fold
# @Desc  : API获取广告模式-空白落地页（仅提交）流程用例，分为需要验证码，不需要验证码；分配方式：计划、手动、直线

from common.config_log import logger
from stream_tools.config.constant import GLOBAL_VAR, const
from control.yinhe.flow_module.check_mobile_success import Check
from control.yinhe.tool_module.website import Website
import allure
import pytest


class TestBlankPage:

    def setup(self):
        self._ws = Website()
        self._cmv = Check()
        GLOBAL_VAR['projectName'] = const.projectName
        GLOBAL_VAR['ideaName'] = const.ideaName
        GLOBAL_VAR['websiteName'] = const.websiteName

    @pytest.mark.manual
    @logger('case')
    @allure.step('不需要验证码的空白落地页流程-计划分配')
    def test_website_NotneedCaptch_plan(self):
        with allure.step('新建空白落地页'):
            self._ws.create_website_NotneedCaptch(adCreateType=2, version=2.13)
        with allure.step('发布落地页'):
            self._ws.publish_website()
        with allure.step('生成链接-计划分配'):
            self._ws.association_creativity_api(allocInstType=1)
        with allure.step("落地页数据查询"):
            self._cmv.check_one_submit(1)

    @pytest.mark.manual
    @logger('case')
    @allure.step('不需要验证码的空白落地页流程-手动分配')
    def test_website_NotneedCaptch_manual(self):
        with allure.step('新建空白落地页'):
            self._ws.create_website_NotneedCaptch(adCreateType=2, version=2.13)
        with allure.step('发布落地页'):
            self._ws.publish_website()
        with allure.step('生成链接-手动分配'):
            self._ws.association_creativity_api(allocInstType=2,isTest=0) #不是测试，isTest=1,是测试
        with allure.step("落地页数据查询"):
            self._cmv.check_one_submit(1)

    @pytest.mark.manual
    @logger('case')
    @allure.step('不需要验证码的空白落地页流程-直线下发')
    def test_website_NotneedCaptch_straight(self):
        with allure.step('新建空白落地页'):
            self._ws.create_website_NotneedCaptch(adCreateType=2, version=2.13)
        with allure.step('发布落地页'):
            self._ws.publish_website()
        with allure.step('生成链接-直线下发'):
            self._ws.association_creativity_api(allocInstType=2, isTest=0, receiveDeptId=4572,
                                                receiveDeptIdChain='1001-2001-4569-4570-4571-4572',
                                                receiveDeptName='rm一院')  # 不是测试，isTest=1,是测试
        with allure.step("落地页数据查询"):
            self._cmv.check_one_submit(1)


    @pytest.mark.manual
    @logger('case')
    @allure.step('需要验证码的空白落地页流程-计划分配')
    def test_website_plan(self):
        with allure.step('新建空白落地页'):
            self._ws.create_website_NeedCaptch(adCreateType=2, version=2.13)
        with allure.step('发布落地页'):
            self._ws.publish_website()
        with allure.step('生成链接-计划分配'):
            self._ws.association_creativity_api(allocInstType=1)
        with allure.step("落地页数据查询"):
            self._cmv.check_one_submit(1)

    @pytest.mark.manual
    @logger('case')
    @allure.step('需要验证码的空白落地页流程-手动分配')
    def test_website_manual(self):
        with allure.step('新建空白落地页'):
            self._ws.create_website_NeedCaptch(adCreateType=2, version=2.13)
        with allure.step('发布落地页'):
            self._ws.publish_website()
        with allure.step('生成链接-手动分配'):
            self._ws.association_creativity_api(allocInstType=2, isTest=0)  # 不是测试，isTest=1,是测试
        with allure.step("落地页数据查询"):
            self._cmv.check_one_submit(1)

    @pytest.mark.manual
    @logger('case')
    @allure.step('需要验证码的空白落地页流程-直线下发')
    def test_website_straight(self):
        with allure.step('新建空白落地页'):
            self._ws.create_website_NeedCaptch(adCreateType=2, version=2.13)
        with allure.step('发布落地页'):
            self._ws.publish_website()
        with allure.step('生成链接-直线下发'):
            self._ws.association_creativity_api(allocInstType=2, isTest=0, receiveDeptId=4572,
                                                receiveDeptIdChain='1001-2001-4569-4570-4571-4572',
                                                receiveDeptName='rm一院')  # 不是测试，isTest=1,是测试
        with allure.step("落地页数据查询"):
            self._cmv.check_one_submit(1)

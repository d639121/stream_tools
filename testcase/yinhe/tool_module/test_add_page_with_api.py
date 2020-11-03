#!/usr/bin/python 
# @Time  : 2020/8/11 16:12
# @Author: LOUIE
# @Desc  : 测试新建落地页-API模式

from common.config_log import logger
from control.yinhe.ad_module.ad_idea.create_ad_idea import CreateAdIdea
from control.yinhe.flow_module.put_record_query import PutRecordQuery
from control.yinhe.tool_module.create_qr_code import CreateQrCode as CQC
from control.yinhe.tool_module.landing_page_with_api import LandingPageWithApi as LPWA
from stream_tools.config.constant import GLOBAL_VAR, const
from control.yinhe.tool_module.landing_page_mgt import LandingPageMgt
import allure


class TestAddPageWithApi:

    def setup(self):
        GLOBAL_VAR['landingPageName'] = const.landingPageName
        self.lpwa = LPWA()
        self.cqc = CQC()
        self.lpm = LandingPageMgt()
        self.cwai = CreateAdIdea()
        self.prq = PutRecordQuery()

    @logger('case')
    @allure.step('企业微信模式-不带商品')
    def test_add_page_with_api_no_goods(self):
        with allure.step('新建落地页'):
            self.lpwa = LPWA()
            self.lpwa.save_page(type=1)
            self.cqc.publish_website()
            self.lpwa.association_creativity()
        # with allure.step('生成二维码'):
        #     tools.create_code()
        with allure.step('查询落地页管理列表'):
            self.lpm.page_list()

    @logger('case')
    @allure.step('企业微信模式-带商品')
    def test_add_page_with_api_take_goods(self):
        with allure.step('新建落地页'):
            self.lpwa = LPWA()
            self.lpwa.save_page(type=2)
            self.cqc.publish_website()
            self.lpwa.association_creativity()
        # with allure.step('生成二维码'):
        #     tools.create_code()
        with allure.step('查询落地页管理列表'):
            self.lpm.page_list()

    @logger('case')
    @allure.step('一键提交模式-手动分配')
    def test_add_page_with_api_1(self):
        with allure.step(''):
            self.lpwa.save_page(type=3)
            self.cqc.publish_website()
            self.lpwa.association_creativity(type=2)
        # with allure.step('生成二维码'):
        #     tools.create_code()
        with allure.step('查询落地页管理列表'):
            self.lpm.page_list()

    @logger('case')
    @allure.step('一键提交模式-直线下发')
    def test_add_page_with_api_2(self):
        with allure.step('新建落地页'):
            self.lpwa.save_page(type=3)
            self.cqc.publish_website()
            self.lpwa.association_creativity(type=3)
        # with allure.step('生成二维码'):
        #     tools.create_code()
        with allure.step('查询落地页管理列表'):
            self.lpm.page_list()



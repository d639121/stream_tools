#!/usr/bin/python
#@Time : 2020/7/22 15:21
#@Author: Fold
#@File : test_only_submit.py

import allure
import pytest
from common.config_log import logger
from stream_tools.config.constant import GLOBAL_VAR, const
from control.yinhe.ad_module.ad_idea.create_ad_idea import CreateAdIdea
from control.yinhe.ad_module.ad_plan.create_ad_plan import CreateAdPlan
from control.yinhe.flow_module.check_mobile_success import Check
from control.yinhe.tool_module.website import Website


class TestAdPlanNormal():
    def setup(self):
        mobile = '18774925933'
        goods_id = 416
        # sql = "delete from mz_mediasystemdb.t_order where mobile = %s and goods_id  = %s; "
        params = [mobile, goods_id]
        # db.execute_sql(sql, params)
        self._cma = CreateAdPlan()
        self._cmc = CreateAdIdea()
        self._cmw = Website()
        self._cmv = Check()
        GLOBAL_VAR['projectName'] = const.projectName
        GLOBAL_VAR['ideaName'] = const.ideaName
        GLOBAL_VAR['websiteName'] = const.websiteName

    @pytest.mark.manual
    @logger('case')
    @allure.step('一键支付模式，计划分配-普通投放模式，默认需要验证码')
    def test_ad_plan_normal(self):
        with allure.step('新建广告计划-计划分配-普通'):
            self._cma.ad_plan(putMode=1, allocInstType=1)
        with allure.step("新建创意-需要验证码"):
            self._cmc.create_creativity(isNeedCaptch=1)
        with allure.step("新建落地页，发布落地页，生成链接，生成二维码"):
            self._cmw.landing_page_create(0, 1)
        with allure.step("落地页数据查询"):
            self._cmv.check_one_submit(0)

    @pytest.mark.manual
    @logger('case')
    @allure.step('一键支付模式，计划分配-小咖投放模式，默认需要验证码')
    def test_manual_xiaoka(self):
        with allure.step('新建广告计划-计划分配-小咖'):
            self._cma.ad_plan(putMode=5, allocInstType=2)  # 创建广告计划
        with allure.step("新建创意-需要验证码"):
            self._cmc.create_creativity(isNeedCaptch=1)
        with allure.step("新建落地页，发布落地页，生成链接，生成二维码"):
            self._cmw.landing_page_create(0, 1)
        with allure.step("用户支付"):
            pass
        # with allure.step("休眠5分钟"):
        #     time.sleep(310)
        with allure.step("落地页数据查询"):
            self._cmv.check_one_submit(0)
        # with allure.step("入库记录查询页面校验相关字段，数据库查看分配状态、不可分配原因"):
        #     result = self._cmv.customer_LeaningRepeat_query()
        #     print(result)
        # with allure.step("订单管理查看是否已自动提单"):
        #     self._cmv.order_manager_list()

    @pytest.mark.manual
    @logger('case')
    @allure.step('一键支付模式，手动分配-高转VIP投放模式，默认需要验证码')
    def test_manual_high(self):
        with allure.step('新建广告计划-计划分配-小咖'):
            self._cma.ad_plan(putMode=3, allocInstType=2)  # 创建广告计划
        with allure.step("新建创意-需要验证码"):
            self._cmc.create_creativity(isNeedCaptch=1)
        with allure.step("新建落地页，发布落地页，生成链接，生成二维码"):
            self._cmw.landing_page_create(0, 1)
        with allure.step("用户支付"):
            pass
        # with allure.step("休眠5分钟"):
        #     time.sleep(310)
        with allure.step("落地页数据查询"):
            self._cmv.check_one_submit(0)
        # with allure.step("入库记录查询页面校验相关字段，数据库查看分配状态、不可分配原因"):
        #     result = self._cmv.customer_LeaningRepeat_query()
        #     print(result)
        # with allure.step("订单管理查看是否已自动提单"):
        #     self._cmv.order_manager_list()

    @pytest.mark.manual
    @logger('case')
    @allure.step('一键支付模式，手动分配-普通投放模式，默认需要验证码')
    def test_manual_normal(self):
        with allure.step('新建广告计划-计划分配-小咖'):
            self._cma.ad_plan(putMode=1, allocInstType=2)  # 创建广告计划
        with allure.step("新建创意-需要验证码"):
            self._cmc.create_creativity(isNeedCaptch=1)
        with allure.step("新建落地页，发布落地页，生成链接，生成二维码"):
            self._cmw.landing_page_create(0, 1)
        with allure.step("用户支付"):
            pass
        # with allure.step("休眠5分钟"):
        #     time.sleep(310)
        with allure.step("落地页数据查询"):
            self._cmv.check_one_submit(0)
        # with allure.step("入库记录查询页面校验相关字段，数据库查看分配状态、不可分配原因"):
        #     result = self._cmv.customer_LeaningRepeat_query()
        #     print(result)
        # with allure.step("订单管理查看是否已自动提单"):
        #     self._cmv.order_manager_list()

    @pytest.mark.manual
    @logger('case')
    @allure.step('一键支付模式，直线下发-普通投放模式，默认需要验证码')
    def test_direct_normal(self):
        with allure.step('新建广告计划-直线下发-普通'):
            self._cma.ad_plan_direct(putMode=1, allocInstType=3)  # 直线下发-普通投放模式
        with allure.step("新建创意-需要验证码"):
            self._cmc.create_creativity_direct(isNeedCaptch=1)
        with allure.step("新建落地页，发布落地页，生成链接，生成二维码"):
            self._cmw.landing_page_create(0, 1)
        with allure.step("用户支付"):
            pass
        # with allure.step("休眠5分钟"):
        #     time.sleep(310)
        with allure.step("落地页数据查询"):
            self._cmv.check_one_submit(0)
        # with allure.step("入库记录查询页面校验相关字段，数据库查看分配状态、不可分配原因"):
        #     result = self._cmv.customer_LeaningRepeat_query()
        #     print(result)
        # with allure.step("订单管理查看是否已自动提单"):
        #     self._cmv.order_manager_list()

    @pytest.mark.manual
    @logger('case')
    @allure.step('一键支付模式，直线下发-高转VIP投放模式，默认需要验证码')
    def test_direct_highl(self):
        with allure.step('新建广告计划-直线下发-高转VIP'):
            self._cma.ad_plan_direct(putMode=3, allocInstType=3)  # 直线下发-高转VIP投放模式
        with allure.step("新建创意-需要验证码"):
            self._cmc.create_creativity_direct(isNeedCaptch=1)
        with allure.step("新建落地页，发布落地页，生成链接，生成二维码"):
            self._cmw.landing_page_create(0, 1)
        with allure.step("用户支付"):
            pass
        # with allure.step("休眠5分钟"):
        #     time.sleep(310)
        with allure.step("落地页数据查询"):
            self._cmv.check_one_submit(0)
        # with allure.step("入库记录查询页面校验相关字段，数据库查看分配状态、不可分配原因"):
        #     result = self._cmv.customer_LeaningRepeat_query()
        #     print(result)
        # with allure.step("订单管理查看是否已自动提单"):
        #     self._cmv.order_manager_list()



if __name__ == '__main__':
    pytest.main(["-sl",  "test_one_submit.py"])
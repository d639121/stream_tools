#!/usr/bin/python 
# @Time   : 2020/7/18 14:45
# @Author : LOUIE
# @Desc   : 入库记录查询-个人微信场景用例

from control.yinhe.ad_module.ad_idea.create_ad_idea import CreateAdIdea
from control.yinhe.ad_module.ad_plan.create_ad_plan import CreateAdPlan
from control.yinhe.flow_module.put_record_query import PutRecordQuery
from control.yinhe.tool_module.create_qr_code import CreateQrCode
from stream_tools.config.constant import const, GLOBAL_VAR
from common.config_log import logger
import allure


class TestPersonalWechatScenario():

    def setup(self):
        self._cwap = CreateAdPlan()
        self._cwai = CreateAdIdea()
        self._cqc = CreateQrCode()
        self._prq = PutRecordQuery()
        GLOBAL_VAR['projectName'] = const.projectName

    @logger('case')
    @allure.step('个人微信流量入库_直线下发，普通投放模式')
    def test_linear_distributed_of_general(self):
        with allure.step('新建广告计划-微信'):
            self._cwap = CreateAdPlan()
            self._cwap.create_ad_plan()
        with allure.step('创建微信广告创意'):
            self._cwap.get_plan_id()
            self._cwai = CreateAdIdea()
            self._cwai.create_personal_wechat_ad_ideas()
            self._cwai.get_idea_id()
        with allure.step('新建落地页'):
            self._cqc = CreateQrCode()
            self._cqc.add_personal_code()
            self._cqc.publish_website()
            self._cqc.create_link(accountId="wx359bdedd5d18907a", releaseChannel=3)
            # tools.create_code()
        with allure.step('落地页数据列表统计查询'):
            self._cqc.ldy_list_data_query()
        with allure.step('入库记录流量数据查询'):
            self._prq.put_record_query()
        with allure.step('广告创意流量数据查询'):
            self._cwai.ad_idea_flow_data_query()

    @logger('case')
    @allure.step('个人微信流量入库_手动分配，普通投放模式')
    def test_manual_allocation_of_general(self):
        with allure.step('新建广告计划-微信'):
            self._cwap.create_wc_ad_plan_for_hand()
        with allure.step('创建微信广告创意'):
            self._cwap.get_plan_id()
            self._cwai.create_personal_wechat_ad_ideas()
            self._cwai.get_idea_id()
        with allure.step('新建落地页'):
            self._cqc.add_personal_code()
            self._cqc.publish_website()
            self._cqc.create_link(accountId="wx359bdedd5d18907a", releaseChannel=3)
            #tools.create_code()
        with allure.step('落地页数据列表统计查询'):
            self._cqc.ldy_list_data_query()
        with allure.step('入库记录流量数据查询'):
            self._prq.put_record_query()
        with allure.step('广告创意流量数据查询'):
            self._cwai.ad_idea_flow_data_query()

    @logger('case')
    @allure.step('个人微信流量入库_直线下发，接待投放模式')
    def test_linear_distributed_of_reception(self):
        with allure.step('新建广告计划-微信'):
            self._cwap.create_wc_ad_plan_for_reception()
        with allure.step('创建微信广告创意'):
            self._cwap.get_plan_id()
            self._cwai = CreateAdIdea()
            self._cwai.create_personal_wechat_ad_ideas()
            self._cwai.get_idea_id()
        with allure.step('新建落地页'):
            self._cqc.add_personal_code()
            self._cqc.publish_website()
            self._cqc.create_link(accountId="wx359bdedd5d18907a", releaseChannel=3)
            #tools.create_code()
        with allure.step('落地页数据列表统计查询'):
            self._cqc.ldy_list_data_query()
        with allure.step('入库记录流量数据查询'):
            self._prq.put_record_query()
        with allure.step('广告创意流量数据查询'):
            self._cwai.ad_idea_flow_data_query()

    @logger('case')
    @allure.step('个人微信流量入库_直线下发，高转vip课投放模式')
    def test_linear_distributed_of_vip(self):
        with allure.step('新建广告计划-微信'):
            self._cwap.create_ad_plan(putMode=3)
        with allure.step('创建微信广告创意'):
            self._cwap.get_plan_id()
            self._cwai = CreateAdIdea()
            self._cwai.create_personal_wechat_ad_ideas()
            self._cwai.get_idea_id()
        with allure.step('新建落地页'):
            self._cqc.add_personal_code()
            self._cqc.publish_website()
            self._cqc.create_link(accountId="wx359bdedd5d18907a", releaseChannel=3)
            #tools.create_code()
        with allure.step('落地页数据列表统计查询'):
            self._cqc.ldy_list_data_query()
        with allure.step('入库记录流量数据查询'):
            self._prq.put_record_query()
        with allure.step('广告创意流量数据查询'):
            self._cwai.ad_idea_flow_data_query()

    @logger('case')
    @allure.step('个人微信流量入库_微信流量手动分配，小咖投放模式')
    def test_linear_distributed_of_small_cafe(self):
        with allure.step('新建广告计划-微信'):
            self._cwap.create_wc_xiaoka_ad_plan()
        with allure.step('创建微信广告创意'):
            self._cwap.get_plan_id()
            self._cwai = CreateAdIdea()
            self._cwai.create_personal_wechat_ad_ideas()
            self._cwai.get_idea_id()
        with allure.step('新建落地页'):
            self._cqc.add_personal_code()
            self._cqc.publish_website()
            self._cqc.create_link(accountId="wx359bdedd5d18907a", releaseChannel=3)
            #tools.create_code()
        with allure.step('落地页数据列表统计查询'):
            self._cqc.ldy_list_data_query()
        with allure.step('入库记录流量数据查询'):
            self._prq.put_record_query()
        with allure.step('广告创意流量数据查询'):
            self._cwai.ad_idea_flow_data_query()



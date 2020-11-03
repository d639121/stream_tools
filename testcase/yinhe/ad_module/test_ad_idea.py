#!/usr/bin/python
# @Time   : 2020/8/19 19:58
# @Author : Jones
# @Desc   : 广告计划

from allure_commons._allure import step
from common.config_log import logger
from stream_tools.config.constant import const, GLOBAL_VAR
from control.yinhe.ad_module.ad_idea.create_ad_idea import CreateAdIdea
from control.yinhe.ad_module.ad_idea.editor_idea_flow import EditorIdeaFlow
from control.yinhe.ad_module.ad_idea.export_idea_flow import ExportIdeaFlow
from control.yinhe.ad_module.ad_plan.create_ad_plan import CreateAdPlan
from utils.generator import random_ean8


class TestAdIdea:

    def setup(self):
        self._cwp = CreateAdPlan()
        self._cwai = CreateAdIdea()
        self._cap = CreateAdPlan()
        self._eif = ExportIdeaFlow()
        GLOBAL_VAR['projectName'] = const.projectName
        GLOBAL_VAR['ideaName'] = const.ideaName

    @step('广告创意-手机流量-广告消费修改')
    @logger('case')
    def test_phone_flow_cons_change(self):
        with step('创建手机广告计划'):
            self._cap.ad_plan(gatherType=1)
        with step('创建手机广告创意'):
            self._cwp.get_plan_id(gatherType=1)
            self._cwai.create_ad_idea()
            self._cwai.get_idea_id(gatherType=1)
        with step('新增广告数据'):
            self._cwai.add_ad_data()
            self._cwai.get_ad_data_id()
            self._cwai.change_ad_data(noExposure=2, noClicks=2, cost=2, rebates=1.3)
        with step('验证修改结果'):
            self._cwai.get_ad_data_id()
            assert int(GLOBAL_VAR['noExposure']) == 2
            assert int(GLOBAL_VAR['noClicks']) == 2
            assert GLOBAL_VAR['cost'] == '2.0'
            assert GLOBAL_VAR['rebates'] == '1.3'

    @step('广告创意-手机流量-广告消费删除')
    @logger('case')
    def test_phone_flow_del_cons(self):
        with step('创建手机广告计划'):
            self._cap.ad_plan(gatherType=1)
        with step('创建手机广告创意'):
            self._cwp.get_plan_id(gatherType=1)
            self._cwai.create_ad_idea()
            self._cwai.get_idea_id(gatherType=1)
        with step('新增广告数据'):
            self._cwai.add_ad_data()
            self._cwai.get_ad_data_id()
            self._cwai.del_ad_data()

    @step('广告创意-微信流量-导出')
    def test_export_idea_wechat_flow(self):
        self._eif.export_idea_flow(gather_type=3)

    @step('广告创意-QQ流量-导出')
    def test_export_idea_qq_flow(self):
        self._eif.export_idea_flow(gather_type=2)

    @step('广告创意-手机流量-导出')
    def test_export_idea_phone_flow(self):
        self._eif.export_idea_flow(gather_type=1)

    @step('广告创意-手机流量-编辑')
    @logger('case')
    def test_phone_flow_editor(self):
        new_name = random_ean8()
        eif = EditorIdeaFlow()
        with step('创建手机广告计划'):
            self._cap.ad_plan(gatherType=1)
        with step('创建手机广告创意'):
            self._cwp.get_plan_id(gatherType=1)
            self._cwai.create_ad_idea()
            self._cwai.get_idea_id(gatherType=1)
            eif.editor_idea_flow(name=new_name, position='12345', remark='123')
            self._cwai.get_idea_id(gatherType=1)
            assert GLOBAL_VAR['newName'] == new_name
            assert GLOBAL_VAR['remark'] == '123'
            assert GLOBAL_VAR['position'] == '12345'

    @step('广告创意-QQ流量-编辑')
    @logger('case')
    def test_qq_flow_editor(self):
        new_name = random_ean8()
        eif = EditorIdeaFlow()
        with step('创建QQ广告计划'):
            self._cap.ad_plan(gatherType=2, allocInstType=3)
        with step('创建QQ广告创意'):
            self._cwai.create_qq_idea()
            self._cwai.get_idea_id(gatherType=2)
            eif.editor_qq_idea_flow(name=new_name, remark='123', gather_type=2)
            self._cwai.get_idea_id(gatherType=2)
            assert GLOBAL_VAR['newName'] == new_name
            assert GLOBAL_VAR['remark'] == '123'

    @step('广告创意-微信流量-编辑')
    @logger('case')
    def test_wechat_flow_editor(self):
        new_name = random_ean8()
        eif = EditorIdeaFlow()
        with step('创建手机广告计划'):
            self._cap.ad_plan(gatherType=3)
        with step('创建手机广告创意'):
            self._cwp.get_plan_id(gatherType=3)
            self._cwai.create_person_wc_ad_idea()
            self._cwai.get_idea_id(gatherType=3)
            eif.editor_wechat_idea_flow(name=new_name, remark='123', gather_type=3)
            self._cwai.get_idea_id(gatherType=3)
            assert GLOBAL_VAR['newName'] == new_name
            assert GLOBAL_VAR['remark'] == '123'

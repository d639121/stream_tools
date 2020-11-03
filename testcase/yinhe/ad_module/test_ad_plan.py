#!/usr/bin/python
# @Time   : 2020/8/18 15:00
# @Author : Jones
# @Desc   : 广告计划

from allure_commons._allure import step
from common.config_log import logger
from stream_tools.config.constant import GLOBAL_VAR, const
from control.yinhe.ad_module.ad_plan.create_ad_plan import CreateAdPlan
from control.yinhe.ad_module.ad_plan.editor_flow import EditorFlow
from control.yinhe.ad_module.ad_plan.export_flow import ExportFlow
from utils.generator import random_ean8


class TestAdPlan:

    def setup(self):
        self._ef = ExportFlow()
        self._cap = CreateAdPlan()
        GLOBAL_VAR['projectName'] = const.projectName

    @step('广告计划--微信流量-导出')
    @logger('case')
    def test_wechat_flow_export(self):
        self._ef.export_flow(gather_type=3)

    @step('广告计划--QQ流量-导出')
    @logger('case')
    def test_qq_flow_export(self):
        self._ef.export_flow(gather_type=2)

    @step('广告计划--手机流量-导出')
    @logger('case')
    def test_phone_flow_export(self):
        self._ef.export_flow()

    @step('广告计划--手机流量-编辑')
    @logger('case')
    def test_phone_flow_editor(self):
        self.ef = EditorFlow()
        new_name = random_ean8()
        with step('创建手机流量广告计划，并保存id'):
            self._cap.ad_plan(gatherType=1)
        with step('修改“计划名称”，“投放渠道”，“广告类型”；“提交”'):
            self.ef.editor_flow(plan_name=new_name)
            self._cap.query_ad_plan(id=GLOBAL_VAR['adId'], gatherType=1)
            assert GLOBAL_VAR['newName'] == new_name

    @step('广告计划--QQ流量-编辑')
    @logger('case')
    def test_qq_flow_editor(self):
        self.ef = EditorFlow()
        new_name = random_ean8()
        with step('创建QQ流量广告计划，并保存id'):
            self._cap.ad_plan(gatherType=2)
        with step('修改“计划名称”，“投放渠道”，“广告类型”；“提交”'):
            self.ef.editor_flow(plan_name=new_name, gather_type=2)
            self._cap.query_ad_plan(id=GLOBAL_VAR['adId'], gatherType=2)
            assert GLOBAL_VAR['newName'] == new_name

    @step('广告计划--微信流量-编辑')
    @logger('case')
    def test_wechat_flow_editor(self):
        self.ef = EditorFlow()
        new_name = random_ean8()
        with step('创建微信流量广告计划，并保存id'):
            self._cap.ad_plan(gatherType=3)
        with step('修改“计划名称”，“投放渠道”，“广告类型”；“提交”'):
            self.ef.editor_flow(plan_name=new_name, gather_type=3)
            self._cap.query_ad_plan(id=GLOBAL_VAR['adId'], gatherType=3)
            assert GLOBAL_VAR['newName'] == new_name

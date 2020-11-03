#!/usr/bin/python
# @Time   : 2020/7/18 10:35
# @Author : Jones
# @Desc   : 企业微信流量入库用例

from allure_commons._allure import step
from common.config_log import logger
from stream_tools.config.constant import GLOBAL_VAR, const
from control.yinhe.ad_module.ad_idea.create_ad_idea import CreateAdIdea
from control.yinhe.ad_module.ad_plan.create_ad_plan import CreateAdPlan
from control.yinhe.flow_module.put_record_query import PutRecordQuery
from control.yinhe.tool_module.create_qr_code import CreateQrCode


class TestCompanyWcFlow:

    def setup(self):
        self._cwp = CreateAdPlan()
        self._cwai = CreateAdIdea()
        self._cqc = CreateQrCode()
        self._prq = PutRecordQuery()
        GLOBAL_VAR['projectName'] = const.projectName
        GLOBAL_VAR['ideaName'] = const.ideaName

    @step('企业微信流量入库_直线下发，普通投放模式')
    @logger('case')
    def test_line_common(self):
        with step('创建微信计划'):
            self._cwp.create_ad_plan()
        with step('创建微信广告创意'):
            self._cwp.get_plan_id()
            self._cwai = CreateAdIdea()
            self._cwai.create_wc_ad_idea()
            self._cwai.get_idea_id()
        with step('新建落地页'):
            self._cqc = CreateQrCode()
            self._cqc.create_qr_code()
            self._cqc.publish_website()
            self._cqc.create_link()
            #create_code()
        with step('落地页数据列表统计查询'):
            self._cqc.ldy_list_data_query()
        with step('入库记录流量数据查询'):
            self._prq = PutRecordQuery()
            self._prq.put_record_query()
        with step('广告创意流量数据查询'):
            self._cwai.ad_idea_flow_data_query()

    @step('企业微信流量入库_手动分配，普通投放模式')
    @logger('case')
    def test_manual_common(self):
        with step('创建微信计划'):
            self._cwp.create_wc_ad_plan_for_hand()
            self._cwp.get_plan_id()
        with step('创建微信广告创意'):
            self._cwai.create_wc_ad_idea()
            self._cwai.get_idea_id()
        with step('新建落地页'):
            self._cqc.create_qr_code()
            self._cqc.publish_website()
            self._cqc.create_link()
            #create_code()
        with step('落地页数据列表统计查询'):
            self._cqc.ldy_list_data_query()
        with step('入库记录流量数据查询'):
            self._prq.put_record_query()
        with step('广告创意流量数据查询'):
            self._cwai.ad_idea_flow_data_query()

    @step('企业微信流量入库_直线下发，接待投放模式')
    @logger('case')
    def test_reception_common(self):
        with step('创建微信计划'):
            self._cwp.create_wc_ad_plan_for_reception()
            self._cwp.get_plan_id()
        with step('创建微信广告创意'):
            self._cwai = CreateAdIdea()
            self._cwai.create_wc_ad_idea()
            self._cwai.get_idea_id()
        with step('新建落地页'):
            self._cqc = CreateQrCode()
            self._cqc.create_qr_code()
            self._cqc.publish_website()
            self._cqc.create_link()
            #create_code()
        with step('落地页数据列表统计查询'):
            self._cqc.ldy_list_data_query()
        with step('入库记录流量数据查询'):
            self._prq = PutRecordQuery()
            self._prq.put_record_query()
        with step('广告创意流量数据查询'):
            self._cwai.ad_idea_flow_data_query()

    @step('企业微信流量入库_直线下发，高转vip课投放模式')
    @logger('case')
    def test_line_vip(self):
        with step('创建微信计划'):
            self._cwp.create_wc_ad_plan_for_model(put_model=3)
            self._cwp.get_plan_id()
        with step('创建微信广告创意'):
            self._cwai = CreateAdIdea()
            self._cwai.create_wc_ad_idea()
            self._cwai.get_idea_id()
        with step('新建落地页'):
            self._cqc = CreateQrCode()
            self._cqc.create_pay_qr_code()
            self._cqc.publish_website()
            self._cqc.create_link()
            #create_code()
        with step('落地页数据列表统计查询'):
            self._cqc.ldy_list_data_query()
        with step('入库记录流量数据查询'):
            self._prq = PutRecordQuery()
            self._prq.put_record_query()
        with step('广告创意流量数据查询'):
            self._cwai.ad_idea_flow_data_query()

    @step('企业微信流量入库_微信流量手动分配，小咖投放模式')
    @logger('case')
    def test_manual_xk(self):
        with step('创建微信计划'):
            self._cwp.create_wc_ad_plan_for_model()
            self._cwp.get_plan_id()
        with step('创建微信广告创意'):
            self._cwai = CreateAdIdea()
            self._cwai.create_wc_ad_idea()
            self._cwai.get_idea_id()
        with step('新建落地页'):
            self._cqc = CreateQrCode()
            self._cqc.create_pay_qr_code()
            self._cqc.publish_website()
            self._cqc.create_link()
            #create_code()
        with step('落地页数据列表统计查询'):
            self._cqc.ldy_list_data_query()
        with step('入库记录流量数据查询'):
            self._prq = PutRecordQuery()
            self._prq.put_record_query()
        with step('广告创意流量数据查询'):
            self._cwai.ad_idea_flow_data_query()

# if __name__ == '__main__':
#     import pytest
#     pytest.main([__file__])
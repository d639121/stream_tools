#!/usr/bin/python
# @Time  : 2020/9/2 14:44
# @Author: LOUIE
# @Desc  : 测试海川系统申请流量

from allure_commons._allure import step
from common.config_log import logger
from stream_tools.config.read_config import rc
from control.base.login import login
from control.haichuan.flow_module.apply_flow import ApplyFlow
from control.yinhe.flow_module.flow_apply_record import FlowApplyRecord
import pytest


class TestApplyFlow:

    def setup(self):
        self.af = ApplyFlow()
        self.far = FlowApplyRecord()

    @step('申请手机流量')
    @logger('case')
    def test_apply_flow(self):
        if rc.get_env() == 'pre':
            login.login_action('t0322511032')
            self.af.apply_flow(promotionerDeptIdChain='1001-3003-12504-12505')
        else:
            login.login_action('t0383212689')
            self.af.apply_flow()

    @step('申请QQ流量')
    @logger('case')
    def test_apply_flow_with_QQ(self):
        if rc.get_env() == 'pre':
            login.login_action('t0322511032')
            self.af.apply_flow(gatherType=2, subjectName='日语中高级', subjectId=478, putMode=1,
                               promotionerDeptIdChain='1001-3003-12504-12505')
        else:
            login.login_action('t0383212689')
            self.af.apply_flow(gatherType=2, subjectName='日语中高级', subjectId=478, putMode=1)

    @step('申请微信流量')
    @logger('case')
    def test_apply_flow_with_wechat(self):
        if rc.get_env() == 'pre':
            login.login_action('t0322511032')
            self.af.apply_flow(gatherType=3, subjectName='软件测试', subjectId=381, putMode=1,
                               promotionerDeptIdChain='1001-3003-12504-12505')
        else:
            login.login_action('t0383212689')
            self.af.apply_flow(gatherType=3, subjectName='软件测试', subjectId=381, putMode=1)

    @pytest.mark.trylast
    @step('查询流量申请记录')
    @logger('case')
    def test_qry_apply_flow_record(self):
        if rc.get_env() == 'pre':
            login.login_action('t0396753586')
        else:
            login.login_action('t0383212689')
        res = self.far.flow_apply_record_query(applyDateValue=3)
        assert res['data']['totalItem'] != 0

    @step('查询流量申请记录-数据权限-无数据')
    @logger('case')
    def test_qry_apply_flow_record2(self):
        if rc.get_env() == 'pre':
            login.login_action('t0396753586')
        else:
            login.login_action('t0373080425')
        self.far.flow_apply_record_query_perssion(subjectId=381)

    @step('查询流量申请记录-条件查询')
    @logger('case')
    def test_qry_apply_flow_record3(self):
        if rc.get_env() == 'pre':
            login.login_action('t0322511032')
        else:
            login.login_action('t0383212689')
        res = self.far.flow_apply_record_query(subjectId=277, gatherType=1, applyDateValue=3)
        print(type(res['data']['totalItem']))
        assert res['data']['totalItem'] != 0

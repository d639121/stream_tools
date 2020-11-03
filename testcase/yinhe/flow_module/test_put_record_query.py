#!/usr/bin/python 
# @Time  : 2020/8/6 14:45
# @Author: LOUIE
# @Desc  : 测试入库记录查询
from stream_tools.config.read_config import rc
from control.yinhe.flow_module.put_record_query import PutRecordQuery
from common.config_log import logger
from control.base.login import login
import allure


class TestPutRecordQuery:

    def setup(self):
        self.prq = PutRecordQuery()

    @allure.step('查询全部入库记录')
    @logger('case')
    def test_put_record_list(self):
        if rc.get_env() == 'pre':
            login.login_action('t0322511032')
        else:
            login.login_action('t0373492024')
        self.prq.put_record_list(allocStatus=None, gatherTimeStart=1596211200000, channelId=3)

    @allure.step('查询暂无意向记录')
    @logger('case')
    def test_query_no_intention_list(self):
        self.prq.no_intention_list()

    @allure.step('分配流量到院')
    @logger('case')
    def test_allot_flow(self):
        if rc.get_env() == 'pre':
            login.login_action('t0322511032')
        else:
            login.login_action('t0373492024')
        self.prq.put_record_list(allocStatus=0, gatherTimeStart=1596211200000, gatherTimeEnd=1598889599000, putMode=1)
        self.prq.allot_flow()

    # @allure.step('批量分配流量到院-校验异常')
    # @logger('case')
    # def test_batch_allot_flow(self):
    #     self.prq.batch_allot_flow()

    @allure.step('流量-入库记录查询-查询')
    @logger('case')
    def test_query_allot_plan(self):
        self.prq.put_record_query()

    @allure.step('查询-未成年流量')
    @logger('case')
    def test_query_nonage_list(self):
        if rc.get_env() == 'pre':
            login.login_action('t0322511032')
        else:
            login.login_action('t0373492024')
        res = self.prq.put_record_list(isAdult=0)
        assert int(res['data']['totalItem']) > 0

    @allure.step('查询-成年流量')
    @logger('case')
    def test_query_adult_list(self):
        if rc.get_env() == 'pre':
            login.login_action('t0322511032')
        else:
            login.login_action('t0373492024')
        res = self.prq.put_record_list(gatherTimeStart=1596211200000, channelId=3)
        assert res['data']['totalItem'] > 0

    @allure.step('导出-成年流量')
    @logger('case')
    def test_export_adult_list(self):
        if rc.get_env() == 'pre':
            login.login_action('t0396753586')
        else:
            login.login_action('t0373492024')
        self.prq.export_adult_list()

    @allure.step('导出-未成年流量')
    @logger('case')
    def test_export_nonage_list(self):
        if rc.get_env() == 'pre':
            login.login_action('t0322511032')
        else:
            login.login_action('t0373492024')
        self.prq.export_nonage_list()

    @allure.step('新增-识别词')
    @logger('case')
    def test1_add_identify(self):
        if rc.get_env() == 'pre':
            login.login_action('t0396753586')
        else:
            login.login_action('t0373492024')
        self.prq.add_identify()

    @allure.step('编辑-识别词')
    @logger('case')
    def test2_edit_identify(self):
        if rc.get_env() == 'pre':
            login.login_action('t0396753586')
        else:
            login.login_action('t0373492024')
        self.prq.query_identify()
        self.prq.edit_identify()

    @allure.step('查询-识别词')
    @logger('case')
    def test3_query_identify(self):
        if rc.get_env() == 'pre':
            login.login_action('t0396753586')
        else:
            login.login_action('t0373492024')
        self.prq.query_identify(identifie='自动化测试-勿删')

    @allure.step('删除-识别词')
    @logger('case')
    def test4_delete_identify(self):
        if rc.get_env() == 'pre':
            login.login_action('t0396753586')
        else:
            login.login_action('t0373492024')
        self.prq.query_identify(identifie='自动化识别词Auto-Edit')
        self.prq.delete_identify()


#!/usr/bin/python 
# @Time  : 2020/9/10 11:23
# @Author: LOUIE
# @Desc  : 广告渠道管理
from stream_tools.config.read_config import rc
from control.yinhe.system_module.ad_channel_mgt import AdChannelMgt
from common.config_log import logger
from control.base.login import login
from stream_tools.config.constant import const, GLOBAL_VAR
import allure


class TestAdChannelMgt:

    def setup_class(self):
        if rc.get_env() == 'pre':
            login.login_action('t0396753586')
        else:
            login.login_action('t0373492024')

    def setup(self):
        self.acm = AdChannelMgt()
        GLOBAL_VAR['channelName'] = const.channelName

    @allure.step('查询-广告渠道列表-无条件')
    @logger('case')
    def test_query_channel_with_all(self):
        self.acm.query_channel()

    @allure.step('查询-广告渠道列表-渠道名称')
    @logger('case')
    def test_query_channel_with_name(self):
        self.acm.query_channel(name='自动化测试-勿删')

    @allure.step('查询-广告渠道列表-对接API')
    @logger('case')
    def test_query_channel_with_api(self):
        self.acm.query_channel(name='自动化API渠道-勿删', isApiAccess=1)

    @allure.step('查询-广告渠道列表-启用状态')
    @logger('case')
    def test_query_channel_with_state(self):
        self.acm.query_channel(state=1)

    @allure.step('新增-广告渠道-对接API-信息流')
    @logger('case')
    def test_add_channel_with_api(self):
        self.acm.add_channel(isApiAccess=1)

    @allure.step('新增-广告渠道-非对接API-信息流')
    @logger('case')
    def test_add_channel_with_noapi(self):
        self.acm.add_channel(isApiAccess=0)

    @allure.step('编辑-广告渠道')
    @logger('case')
    def test_edit_channel(self):
        self.acm.edit_channel(state=1)

    @allure.step('禁用-广告渠道')
    @logger('case')
    def test_forbid_channel(self):
        self.acm.forbid_channel(state=2)
        res = self.acm.query_channel(name='自动化测试-勿删')
        assert res['data']['list'][0]['state'] == 2

    @allure.step('启用-广告渠道')
    @logger('case')
    def test_open_channel(self):
        self.acm.forbid_channel(state=1)
        res = self.acm.query_channel(name='自动化测试-勿删')
        assert res['data']['list'][0]['state'] == 1
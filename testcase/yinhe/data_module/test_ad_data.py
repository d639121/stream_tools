#!/usr/bin/python
# @Time   : 2020/8/18 15:00
# @Author : Jones
# @Desc   : 广告数据

from allure_commons._allure import step
from common.config_log import logger
from stream_tools.config.constant import GLOBAL_VAR
from stream_tools.config.read_config import rc
from control.base.login import login
from control.yinhe.data_module.ad_data import AdData


class TestAdData:

    def setup(self):
        self._ad = AdData()

    @step('数据/数据统计/广告数据-管理员查询')
    @logger('case')
    def test_query_ad_data_for_admin(self):
        if rc.get_env() == 'pre':
            login.login_action('t0396753586')
        else:
            login.login_action('t0373492024')
        self._ad.query_ad_data()

    @step('数据/数据统计/广告数据-售前查询')
    @logger('case')
    def test_query_ad_data_for_sales(self):
        if rc.get_env() == 'pre':
            login.login_action('t0322511032')
        else:
            login.login_action('t0385252771')
        self._ad.query_ad_data()

    @step('数据/数据统计/广告数据-翻页')
    @logger('case')
    def test_turn_page_query_ad_data(self):
        if rc.get_env() == 'pre':
            login.login_action('t0322511032')
        else:
            login.login_action('t0373492024')
        with step('查询'):
            self._ad.query_ad_data()
        with step('翻页查询'):
            self._ad1 = AdData()
            self._ad1.query_ad_data(pageIndex=2)

    @step('数据/数据统计/广告数据-导出')
    @logger('case')
    def test_export_ad_data(self):
        if rc.get_env() == 'pre':
            login.login_action('t0322511032')
        else:
            login.login_action('t0373492024')
        self._ad.export_ad_data()

    @step('数据/数据统计/广告数据-预约导出')
    @logger('case')
    def test_prepare_export(self):
        if rc.get_env() == 'pre':
            login.login_action('t0322511032')
        else:
            login.login_action('t0373492024')
        local_time = GLOBAL_VAR['yesterday']
        self._ad.prepare_export_ad_data(queryParams='{"来源日期":"2019-07-01 至 %s"}' % local_time)
#!/usr/bin/python
# @Time   : 2020/7/31 10:35
# @Author : Fold
# @Desc   : 导入流量

import time
import allure
import pytest
from common.config_log import logger
from stream_tools.config.constant import GLOBAL_VAR, const
from control.base.login import login
from control.yinhe.ad_module.ad_idea.add_consumer_single import ConsumerSingle
from control.yinhe.ad_module.ad_idea.import_flow_batch import ifb
from control.yinhe.ad_module.ad_idea.import_flow_single import ipf
from control.yinhe.flow_module.import_flow_query import ImportFlowQuery


class TestImportFlow():

    def setup_class(self):
        login.login_action('t0383212689', '123456')

    def setup(self):
        self.consumer = ConsumerSingle()
        GLOBAL_VAR['projectName'] = const.projectName
        GLOBAL_VAR['ideaName'] = const.ideaName
        GLOBAL_VAR['gatherTimeStart'] = const.gatherTimeStart
        self._time = str(GLOBAL_VAR['todayTime'])
        self._qq = GLOBAL_VAR['qq']
        self._phone = const.phoneNumber
        self._phone1 = const.phoneNumber
        self._phone2 = const.phoneNumber
        self._wx = const.qq
        self._wx1 = const.qq
        self._wx2 = const.qq
        self._ifq = ImportFlowQuery()

    @logger('case')
    @allure.step('银河/广告/广告创意-批量导入广告消费数据')
    def test_import_consumer_batch(self):
        with allure.step('银河/广告/广告计划】创建广告计划'):
            self.consumer.add_ad_plan()
        with allure.step('银河/广告/广告计划】查询广告计划'):
            self.consumer.program_pageList()
        with allure.step('银河/广告/广告计划】创建广告创意'):
            self.consumer.creativity_save()
        with allure.step('银河/广告/广告计划】查询广告创意'):
            self.consumer.creativity_pageList()
        with allure.step('银河/广告/广告创意】批量导入广告消费数据'):
            self.crate_id = GLOBAL_VAR['creativityId']
            excel = {
                "1": ["投放日期（必填）", "曝光量（必填）", "点击量（必填）", "账面消费（必填）", "返点（必填）", "创意ID（必填）", "科目（必填）"],
                "2": [self._time, 100, 100, 10000, 1, self.crate_id, "Python"],
            }
            self.consumer.import_consumer_batch(excel)


    @logger('case')
    @allure.step('导入手机单个广告流量数据')
    def test_import_mobile_single(self):
        with allure.step('导入手机单个广告流量数据'):
            excel = {
                "1": ["客户昵称（姓名）", "手机号码（必填）", "QQ号码", "微信", "参考年龄", "流量来源时间（必填,三天内数据）", "地域（市级，非必填）", "流量备注"],
                "2": ["王五", self._phone, self._qq, self._qq, 17, self._time, "长沙市", "流量备注"],
                "3": ["李四", self._phone1, self._qq, self._qq, None, self._time, "长沙市", "流量备注"],
                "4": ["张三", self._phone2, self._qq, self._qq, 17, self._time, "长沙市", "流量备注"]
            }
            ipf.import_mobile_single(excel)

    @logger('case')
    @allure.step('导入qq单个广告流量数据')
    def test_import_qq_single(self):
        with allure.step('导入qq单个广告流量数据'):
            excel = {
                "1": ["QQ号码（必填）", "来源时间", "地域（市级，非必填）", "流量备注"],
                "2": [self._wx, self._time, "长沙市", "流量备注"],
                "3": [self._wx1, self._time, "长沙市", "流量备注"],
                "4": [self._wx2, self._time, "长沙市", "流量备注"]
            }
            ipf.import_qq_single(excel)

    @logger('case')
    @allure.step('导入微信单个广告流量数据')
    def test_import_wx_single(self):
        with allure.step('导入微信单个广告流量数据'):
            excel = {
                "1": ["微信号（必填）", "来源时间", "地域（市级，非必填）", "流量备注"],
                "2": [self._wx, self._time, "长沙市", "流量备注"],
                "3": [self._wx1, self._time, "长沙市", "流量备注"],
                "4": [self._wx2, self._time, "长沙市", "流量备注"]
            }
            ipf.import_wx_single(excel)

    @logger('case')
    @allure.step('从创建广告计划开始到创意，录入消费数据')
    def test_add_consumer_single(self):
        with allure.step('从创建广告计划开始到创意，录入消费数据'):
            self.consumer.add_consumer_single()

    @logger('case')
    @allure.step('批量导入手机广告流量数据,普通投放模式')
    def test_import_mobile_batch_normal(self):
        with allure.step('批量导入手机广告流量数据,普通投放模式'):
            excel = {
                "1": ["客户昵称（姓名）", "手机号码（必填）", "QQ号码", "微信", "参考年龄", "流量来源时间（必填,三天内数据）", "创意ID（必填）", "科目（必填）",
                      "地域（市级，非必填）", "流量备注"],
                "2": ["张三", self._phone, self._qq, self._qq, 17, self._time, "111743", "Python", "长沙市", "流量备注"],
                "3": ["李四", self._phone1, self._qq, self._qq, None, self._time, "111744", "C", "长沙市", "流量备注"],
                "4": ["王五", self._phone2, self._qq, self._qq, 28, self._time, "111743", "Python", "长沙市", "流量备注"]
            }
            ifb.import_mobile_batch_normal(excel)

    @logger('case')
    @allure.step('批量导入手机广告流量数据,高转VIP投放模式')
    def test_import_mobile_batch_vip(self):
        with allure.step('批量导入手机广告流量数据,高转VIP投放模式'):
            excel = {
                "1": ["客户昵称（姓名）", "手机号码（必填）", "QQ号码", "微信", "支付金额（必填）", "参考年龄", "流量来源时间（必填,三天内数据）", "创意ID（必填）",
                      "科目（必填）", "地域（市级，非必填）", "流量备注"],
                "2": ["张三", self._phone, self._qq, self._qq, 900, 17, self._time, "111746", "Python", "长沙市", "流量备注"],
                "3": ["李四", self._phone1, self._qq, self._qq, 900, None, self._time, "111747", "C", "长沙市", "流量备注"],
                "4": ["王五", self._phone2, self._qq, self._qq, 900, 28, self._time, "111746", "Python", "长沙市", "流量备注"]
            }
            ifb.import_mobile_batch_vip(excel)

    @logger('case')
    @allure.step('批量导入手机广告流量数据,app投放模式')
    def test_import_mobile_batch_app(self):
        with allure.step('批量导入手机广告流量数据,app投放模式'):
            excel = {
                "1": ["客户昵称（姓名）", "手机号码（必填）", "QQ号码", "微信", "参考年龄", "流量来源时间（必填,三天内数据）", "创意ID（必填）", "科目（必填）",
                      "地域（市级，非必填）", "流量备注"],
                "2": ["张三", self._phone, self._qq, self._qq, 17, self._time, "111750", "C", "长沙市", "流量备注"],
                "3": ["李四", self._phone1, self._qq, self._qq, None, self._time, "111749", "Python", "长沙市", "流量备注"],
                "4": ["王五", self._phone2, self._qq, self._qq, 28, self._time, "111750", "C", "长沙市", "流量备注"]
            }
            ifb.import_mobile_batch_app(excel)

    @logger('case')
    @allure.step('批量导入qq广告流量数据')
    def test_import_qq_batch(self):
        with allure.step('批量导入qq广告流量数据'):
            excel = {
                "1": ["QQ号码（必填）", "来源时间", "创意ID（必填）", "科目（必填）", "地域（市级，非必填）", "流量备注"],
                "2": [self._wx, self._time, "111745", "C", "长沙市", "流量备注"],
                "3": [self._wx1, self._time, "111201", "Python", "长沙市", "流量备注"],
                "4": [self._wx2, self._time, "111201", "Python", "长沙市", "流量备注"]
            }
            ifb.import_qq_batch(excel)

    @logger('case')
    @allure.step('批量导入微信广告流量数据,普通投放模式')
    def test_import_wx_batch_normal(self):
        with allure.step('批量导入微信广告流量数据,普通投放模式'):
            excel = {
                "1": ["微信号（必填）", "来源时间", "创意ID（必填）", "科目（必填）", "地域（市级，非必填）", "流量备注"],
                "2": [self._wx, self._time, "111202", "Python", "长沙市", "流量备注"],
                "3": [self._wx1, self._time, "111751", "C", "长沙市", "流量备注"],
                "4": [self._wx2, self._time, "111202", "Python", "长沙市", "流量备注"]
            }
            ifb.import_wx_batch_normal(excel)

    @logger('case')
    @allure.step('批量导入微信广告流量数据,接待投放模式')
    def test_import_wx_batch_reception(self):
        with allure.step('批量导入微信广告流量数据,接待投放模式'):
            excel = {
                "1": ["微信号（必填）", "来源时间", "创意ID（必填）", "科目（必填）", "地域（市级，非必填）", "流量备注", "流量载体（投放微信号，非必填）", "售前部门（必填）",
                      "跟进人（潭州账号，必填）"],
                "2": [self._wx, self._time, "111753", "Python", "长沙市", "流量备注", "1877492592mmm", "自动化测试院", "t0353655876"],
                "3": [self._wx1, self._time, "111754", "C", "长沙市", "流量备注", "1877492592mmm", "自动化测试院", "t0353655876"],
                "4": [self._wx2, self._time, "111753", "Python", "长沙市", "流量备注", "1877492592mmm", "自动化测试院", "t0353655876"]
            }
            ifb.import_wx_batch_reception(excel)

    @logger('case')
    @allure.step('批量导入微信广告流量数据,高转vip投放模式')
    def test_import_wx_batch_vip(self):
        with allure.step('批量导入微信广告流量数据,高转vip投放模式'):
            excel = {
                "1": ["微信号（必填）", "支付金额（必填）", "来源时间", "创意ID（必填）", "科目（必填）", "地域（市级，非必填）", "流量备注"],
                "2": [self._wx, 900, self._time, "111755", "Python", "长沙市", "流量备注"],
                "3": [self._wx1, 900, self._time, "111756", "C", "长沙市", "流量备注"],
                "4": [self._wx2, 900, self._time, "111755", "Python", "长沙市", "流量备注"]
            }
            ifb.import_wx_batch_vip(excel)


    @logger('case')
    @allure.step('导入流量查询')
    def test_import_flow_query(self):
        self._ifq.import_flow_query()

    def teardown(self):
        time.sleep(1)

if __name__ == '__main__':
    pytest.main(["-sl", __file__])
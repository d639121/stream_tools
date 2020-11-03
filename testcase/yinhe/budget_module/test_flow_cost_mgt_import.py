#!/usr/bin/python 
# @Time  : 2020/8/31 16:26
# @Author: Fold
# @Desc  : 流量成本管理-导入

import datetime
import allure
from common.config_log import logger
from stream_tools.config.read_config import rc
from control.base.login import login
from control.yinhe.budget_module.flow_cost_mgt import FlowCostMgt


class TestFlowCostMgtImport:

    def setup_class(self):
        if rc.get_env() == 'pre':
            login.login_action('t0322511032', '123456')
        else:
            login.login_action('t0384223793', '123456')
        self._time = datetime.datetime.now().strftime('%Y-%m-%d')
        i = datetime.datetime.now().day
        subject_list = ['PHP', 'C', 'C++', 'C#', 'Java', 'Python', 'Git', 'Boot', 'RFG', 'G', '基础英语', '雅思', '四六级',
                   '托福', '职场/行业用语', '意式英语', '同程翻译', '出国托福','出国雅思', 'SAT', '留学指导', '其他出国留学',
                   '其他英语应试', '英语四六级', '日语零基础', '日语中高级', '日语初级', '兴趣日语', '日语考试', '日本留学',
                   '韩语初级']
        self._sub = subject_list[i-1]

    def setup(self):
        self._fcm = FlowCostMgt()

    @logger('case')
    @allure.step('流量成本导入,导入doc文件')
    def test_import_flow_cost_mgt_doc(self):
        with allure.step('导入doc文件'):
            self._fcm.flow_cost_mgt_import_others(file_name='import_doc.doc', status='999999004', msg='文件类型错误。')

    @logger('case')
    @allure.step('流量成本导入，导入CSV文件')
    def test_import_flow_cost_mgt_csv(self):
        with allure.step('导入csv文件'):
            self._fcm.flow_cost_mgt_import_others(file_name='import_csv.csv', status='999999004', msg='文件类型错误。')

    @logger('case')
    @allure.step('流量成本导入，导入空白excel文件')
    def test_import_flow_cost_mgt_blank_excel(self):
        with allure.step('导入excel文件'):
            self._fcm.flow_cost_mgt_import_others(file_name='import_excel.xlsx', status='999999011', msg='文件解析失败，该文件无法解析。')

    @logger('case')
    @allure.step('流量成本导入，导入正确excel文件')
    def test_import_flow_cost_mgt_excel(self):
        with allure.step('导入excel文件'):
            excel = {
                "1": ["成本月份", "推广组织", "科目", "渠道", "获客方式", "投放模式", "上月投放人数", "上月现金消费",
                      "上月供量总数", "上月流量成本",	"上月日均供量", "预估当月日均供量", "预估当月日均增量", "预估当月成本",
                      "预估当月日消费", "预估当月月供量", "预估当月现金消费"],
                "2": [self._time, "潭州教育>自动化测试分公司--勿动>自动化测试群--勿动>自动化测试事业部>自动化测试院", self._sub,
                      "支付宝", "手机流量", "普通", 10, 10, 10, 1, 1, 1,	1, 1, 1, 1,	1]
            }
            self._fcm.flow_cost_mgt_import(excel=excel)


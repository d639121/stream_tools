#!/usr/bin/python
# @Time   : 2020/8/18 15:00
# @Author : Jones
# @Desc   : 投放预算管理-预算表

import random
from allure_commons._allure import step
from common.config_log import logger
from stream_tools.config.constant import GLOBAL_VAR
from stream_tools.config.read_config import rc
from control.base.login import login
from control.yinhe.budget_module.budget_mgt import BudgetMgt


class TestBudgetMgt:

    def setup(self):
        self._bm = BudgetMgt()

    @step('预算-投放预算管理-预算表-无条件查询')
    @logger('case')
    def test_query_budget_data_for_none(self):
        if rc.get_env() == 'pre':
            login.login_action('t0322511032')
        else:
            login.login_action('t0373492024')
        self._bm.query_budget_data()

    @step('预算-投放预算管理-预算表-预算月份查询查询')
    @logger('case')
    def test_query_budget_data_for_month(self):
        if rc.get_env() == 'pre':
            login.login_action('t0322511032')
        else:
            login.login_action('t0373492024')
        last_month = GLOBAL_VAR['monthAgoTimeStart']
        now_time = GLOBAL_VAR['gatherTimeEnd']
        self._bm.query_budget_data(startCostMonth=last_month, endCostMonth=now_time)

    @step('预算-投放预算管理-预算表-推广组织查询')
    @logger('case')
    def test_query_budget_data_for_tissue(self):
        if rc.get_env() == 'pre':
            login.login_action('t0322511032')
        else:
            login.login_action('t0373492024')
        self._bm.query_budget_data(promotionerDeptIdChain='1001-8006-8007-8008-8009')

    @step('预算-投放预算管理-预算表-售前组织查询')
    @logger('case')
    def test_query_budget_data_for_sales(self):
        if rc.get_env() == 'pre':
            login.login_action('t0322511032')
        else:
            login.login_action('t0373492024')
        self._bm.query_budget_data(receiveDeptIdChain='1001-8006-8007-8008-8009')

    @step('预算-投放预算管理-预算表-科目查询')
    @logger('case')
    def test_query_budget_data_for_subject(self):
        if rc.get_env() == 'pre':
            login.login_action('t0322511032')
        else:
            login.login_action('t0373492024')
        self._bm.query_budget_data(subjectId=277)

    @step('预算-投放预算管理-预算表-获客方式查询')
    @logger('case')
    def test_query_budget_data_for_gather_type(self):
        if rc.get_env() == 'pre':
            login.login_action('t0322511032')
        else:
            login.login_action('t0373492024')
        self._bm.query_budget_data(gatherType=1)

    @step('预算-投放预算管理-预算表-投放模式查询')
    @logger('case')
    def test_query_budget_data_for_put_model(self):
        if rc.get_env() == 'pre':
            login.login_action('t0322511032')
        else:
            login.login_action('t0373492024')
        self._bm.query_budget_data(putMode=1)

    @step('预算-投放预算管理-预算表-预算状态查询')
    @logger('case')
    def test_query_budget_data_for_apply_status(self):
        if rc.get_env() == 'pre':
            login.login_action('t0322511032')
        else:
            login.login_action('t0373492024')
        self._bm.query_budget_data(applyStauts=1)

    @step('预算-投放预算管理-预算表-录入方式查询')
    @logger('case')
    def test_query_budget_data_for_input_mode(self):
        if rc.get_env() == 'pre':
            login.login_action('t0322511032')
        else:
            login.login_action('t0373492024')
        self._bm.query_budget_data(inputMode=1)

    @step('预算-投放预算管理-预算表-重置')
    @logger('case')
    def test_query_budget_data_for_reset(self):
        if rc.get_env() == 'pre':
            login.login_action('t0322511032')
        else:
            login.login_action('t0373492024')
        self._bm.query_budget_data()

    @step('预算-投放预算管理-预算表-导入doc文件')
    @logger('case')
    def test_import_doc_budget_data(self):
        if rc.get_env() == 'pre':
            login.login_action('t0322511032')
        else:
            login.login_action('t0373492024')
        self._bm.import_budget_fail_data(file_name='import_doc.doc')

    @step('预算-投放预算管理-预算表-导入csv文件')
    @logger('case')
    def test_import_csv_budget_data(self):
        if rc.get_env() == 'pre':
            login.login_action('t0322511032')
        else:
            login.login_action('t0373492024')
        self._bm.import_budget_fail_data(file_name='import_csv.csv')

    @step('预算-投放预算管理-预算表-导入错误表头xlsx文件')
    @logger('case')
    def test_import_error_xlsx_budget_data(self):
        if rc.get_env() == 'pre':
            login.login_action('t0322511032')
        else:
            login.login_action('t0373492024')
        self._bm.import_budget_error_data(file_name='import_error_xlsx.xlsx')

    @step('预算-投放预算管理-预算表-导入xlsx文件')
    @logger('case')
    def test_import_xlsx_budget_data(self):
        month = random.randint(1, 7)
        year = GLOBAL_VAR['yearAndMonth']
        if rc.get_env() == 'pre':
            login.login_action('t0396753586')
            excel = {
                "1": ["预算月份", "推广组织", "售前组织", "科目", "获客方式", "投放模式", "周次", "工作日",
                      "入职1月内人数", "入职1月以上未转正人数", "已转正人数", "人均名片数", "预估转化率", "预估客单价", "申请备注（非必填）"],
                "2": [year, "潭州教育>华西三区>华西三区成都第二分公司>成二分流量第一事业部>成二分流量二院", "潭州教育>华西二区>华西二区哈尔滨分公司>哈尔滨综合第一事业部>哈尔滨插画一院", "Python", "手机流量",
                      "高转VIP课", month, 2, 10, 20, 30, 20, 0.07, 1000]
            }
        else:
            login.login_action('t0373492024')
            excel = {
                "1": ["预算月份", "推广组织", "售前组织", "科目", "获客方式", "投放模式", "周次", "工作日",
                      "入职1月内人数", "入职1月以上未转正人数", "已转正人数", "人均名片数", "预估转化率", "预估客单价", "申请备注（非必填）"],
                "2": [year, "潭州教育>熙悦测试分公司>熙悦测试事业部>熙悦测试院", "潭州教育>长沙分公司>潭州课堂>日语一院", "Python", "手机流量",
                      "高转VIP课", month, 2, 10, 20, 30, 20, 0.07, 1000]
            }

        self._bm.import_budget_data(excel)

    @step('预算-投放预算管理-预算表-导出')
    @logger('case')
    def test_export_budget_data(self):
        if rc.get_env() == 'pre':
            login.login_action('t0322511032')
        else:
            login.login_action('t0373492024')
        self._bm.export_budget_data()

    @step('预算-投放预算管理-预算表-查询条件后导出')
    @logger('case')
    def test_export_budget_data_by_type(self):
        if rc.get_env() == 'pre':
            login.login_action('t0322511032')
        else:
            login.login_action('t0373492024')
        self._bm.export_budget_data_by_type()

    @step('预算-投放预算管理-预算表-列表操作栏中的修改功能')
    @logger('case')
    def test_update_budget_data(self):
        if rc.get_env() == 'pre':
            login.login_action('t0396753586')
        else:
            login.login_action('t0373492024')
        with step('先查询获得历史数据'):
            self._bm.query_budget_data()
        with step('修改'):
            self._bm.update_budget_data(workDay=5, monthEntryNum=5, monthUnCorrectNum=5, monthCorrectNum=5,
                                        avgCardNum=5, conversionRate=0.17, customerPrice=777)
            self._bm = BudgetMgt()
            self._bm.query_budget_data()
            assert GLOBAL_VAR['workDay'] == '5' and GLOBAL_VAR['conversionRate'] == '0.17'

    @step('预算-投放预算管理-预算表-列表操作栏中的失效功能')
    @logger('case')
    def test_failure_budget_data(self):
        if rc.get_env() == 'pre':
            login.login_action('t0396753586')
        else:
            login.login_action('t0373492024')
        with step('先查询获得历史数据'):
            self._bm.query_budget_data()
            self._bm.failure_budget_data()

    @step('预算-投放预算管理-预算表-已失效预算的修改记录功能')
    @logger('case')
    def test_failure_update(self):
        if rc.get_env() == 'pre':
            login.login_action('t0396753586')
        else:
            login.login_action('t0373492024')
        with step('先查询获得历史数据,让该数据失效'):
            self._bm.query_budget_data()
            self._bm.failure_budget_data()
        with step('点击该已失效得修改功能'):
            self._bm.failure_update_record()

    @step('预算-投放预算管理-预算表-翻页')
    @logger('case')
    def test_turn_page_budget_data(self):
        if rc.get_env() == 'pre':
            login.login_action('t0322511032')
        else:
            login.login_action('t0373492024')
        self._bm.query_budget_data(pageIndex=2)
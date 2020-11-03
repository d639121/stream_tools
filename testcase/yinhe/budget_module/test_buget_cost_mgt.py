#!/usr/bin/python 
# @Time  : 2020/9/3 20:35
# @Author: Fold
# @Desc  : 预算-投放预算管理-申请记录

import allure

from common.config_log import logger
from stream_tools.config.constant import GLOBAL_VAR
from stream_tools.config.read_config import rc
from control.base.login import login
from control.haichuan.budget_mgt.flow_budget_mgt import FlowBudgetMgt
from control.yinhe.budget_module.budget_mgt import BudgetMgt


class TestBudgetCost:

    def setup(self):
        if rc.get_env() == 'pre':
            login.login_action('t0322511032', '123456')
        else:
            login.login_action('t0384223793', '123456')
        # login.login_action('t0384223793', '123456')
        self._tmf = GLOBAL_VAR['thisMonthFirst']
        self._nmf = GLOBAL_VAR['nextMonthFirst']
        self._nml = GLOBAL_VAR['nextMonthLast']
        self._bm = BudgetMgt()
        self._fbm = FlowBudgetMgt()

    @logger('case')
    @allure.step('查询投放预算管理申请记录-无条件查询')
    def test_qry_cost_apply_blank(self):
        with allure.step('查询投放预算管理申请记录-无条件查询'):
            self._bm.qry_cost_apply()

    @logger('case')
    @allure.step('查询投放预算管理申请记录-预算月份查询')
    def test_qry_cost_apply_month(self):
        with allure.step('查询投放预算管理申请记录-预算月份查询'):
            self._bm.qry_cost_apply(startCostMonth=self._nmf, endCostMonth=self._nml)

    @logger('case')
    @allure.step('查询投放预算管理申请记录-推广组织查询')
    def test_qry_cost_apply_promotion(self):
        with allure.step('查询投放预算管理申请记录-推广组织查询'):
            self._bm.qry_cost_apply(promotionerDeptIdChain='1001-8006-8007-8008-8009')

    @logger('case')
    @allure.step('查询投放预算管理申请记录-售前组织查询')
    def test_qry_cost_apply_receive(self):
        with allure.step('查询投放预算管理申请记录-售前组织查询'):
            self._bm.qry_cost_apply(receiveDeptIdChain='1001-8006-8007-8008-8009')

    @logger('case')
    @allure.step('查询投放预算管理申请记录-科目查询')
    def test_qry_cost_apply_cate(self):
        with allure.step('查询投放预算管理申请记录-科目查询'):
            self._bm.qry_cost_apply(subjectId=277)

    @logger('case')
    @allure.step('查询投放预算管理申请记录-获客方式查询')
    def test_qry_cost_apply_gather(self):
        with allure.step('查询投放预算管理申请记录-获客方式查询'):
            self._bm.qry_cost_apply(gatherType=1)

    @logger('case')
    @allure.step('查询投放预算管理申请记录-投放模式查询')
    def test_qry_cost_apply_mode(self):
        with allure.step('查询投放预算管理申请记录-投放模式查询'):
            self._bm.qry_cost_apply(putMode=1)

    @logger('case')
    @allure.step('查询投放预算管理申请记录-审核状态查询')
    def test_qry_cost_apply_state(self):
        with allure.step('查询投放预算管理申请记录-审核状态查询'):
            self._bm.qry_cost_apply(auditState=3)

    @logger('case')
    @allure.step('导出投放预算管理申请记录-小于5000条记录且无条件')
    def test_export_cost_apply_less5000(self):
        with allure.step('导出投放预算管理申请记录-小于5000条记录且无条件'):
            self._bm.export_cost_apply()

    @logger('case')
    @allure.step('导出投放预算管理申请记录-小于5000条记录且有条件限定')
    def test_export_cost_apply_more5000(self):
        with allure.step('导出投放预算管理申请记录-小于5000条记录且有条件限定'):
            self._bm.export_cost_apply(auditState=3)

    @logger('case')
    @allure.step('审核投放预算申请记录-审核通过')
    def test_chk_cost_apply(self):
        with allure.step('海川系统新增投放预算申请记录'):
            if rc.get_env() != 'pre':
                login.login_action('t0385252771', '123456')
            self._fbm.add_flow_budget(gather=1, mode=2)
        with allure.step('查询未审核的流量预算'):
            if rc.get_env() != 'pre':
                login.login_action('t0385252771', '123456')
            self._fbm.qry_flow_budget()
        with allure.step('售前数据中心审核流量预算'):
            if rc.get_env() != 'pre':
                login.login_action('t0385252771', '123456')
            self._fbm.chk_flow_budget()
        with allure.step('流量部门审核审核-通过'):
            if rc.get_env() != 'pre':
                login.login_action('t0384223793', '123456')
            self._bm.chk_cost_apply()

    @logger('case')
    @allure.step('审核投放预算申请记录-驳回')
    def test_chk_cost_apply_reject(self):
        with allure.step('海川系统新增投放预算申请记录'):
            if rc.get_env() != 'pre':
                login.login_action('t0385252771', '123456')
            self._fbm.add_flow_budget(gather=1, mode=1)
        with allure.step('查询未审核的流量预算'):
            if rc.get_env() != 'pre':
                login.login_action('t0385252771', '123456')
            self._fbm.qry_flow_budget()
        with allure.step('售前数据中心审核流量预算'):
            if rc.get_env() != 'pre':
                login.login_action('t0385252771', '123456')
            self._fbm.chk_flow_budget()
        with allure.step('流量部门审核审核-驳回'):
            if rc.get_env() != 'pre':
                login.login_action('t0384223793', '123456')
            self._bm.chk_cost_apply(auditState=0, auditRemark='拒绝')

    @logger('case')
    @allure.step('投放预算申请记录-查看操作记录')
    def test_record_cost_apply(self):
        with allure.step('查询投放预算申请记录'):
            if rc.get_env() != 'pre':
                login.login_action('t0384223793', '123456')
            self._bm.qry_cost_apply(auditState=4)
        with allure.step('查看未审核的投放预算申请记录的操作记录'):
            if rc.get_env() != 'pre':
                login.login_action('t0384223793', '123456')
            self._bm.record_cost_apply()

    @logger('case')
    @allure.step('审核投放预算申请记录-批量审核通过')
    def test_chk_cost_apply_batch_pass(self):
        with allure.step('海川系统新增投放预算申请记录'):
            if rc.get_env() != 'pre':
                login.login_action('t0385252771', '123456')
            self._fbm.add_flow_budget(gather=2, mode=2)
            self._fbm.add_flow_budget(gather=2, mode=3)
        with allure.step('查询未审核的流量预算'):
            if rc.get_env() != 'pre':
                login.login_action('t0385252771', '123456')
            self._fbm.qry_flow_budget()
        with allure.step('售前数据中心审核流量预算'):
            if rc.get_env() != 'pre':
                login.login_action('t0385252771', '123456')
            self._fbm.chk_flow_budget()
        with allure.step('查询投放预算申请记录'):
            if rc.get_env() != 'pre':
                login.login_action('t0384223793', '123456')
            res = self._bm.qry_cost_apply(auditState=3)
            rs = res['data']['list']
            id_list = []
            if len(rs):
                for i in range(len(rs)):
                    id = rs[i]['id']
                    id_list.append(id)
            ids = ','.join(str(i) for i in id_list)
        with allure.step('流量部门审核审核-通过'):
            if rc.get_env() != 'pre':
                login.login_action('t0384223793', '123456')
            self._bm.chk_cost_apply(ids=ids)

    @logger('case')
    @allure.step('审核投放预算申请记录-批量驳回')
    def test_chk_cost_apply_reject_batch(self):
        with allure.step('海川系统新增投放预算申请记录'):
            if rc.get_env() != 'pre':
                login.login_action('t0385252771', '123456')
            self._fbm.add_flow_budget(gather=3, mode=1)
            self._fbm.add_flow_budget(gather=3, mode=2)
        with allure.step('查询未审核的流量预算'):
            if rc.get_env() != 'pre':
                login.login_action('t0385252771', '123456')
            self._fbm.qry_flow_budget()
        with allure.step('售前数据中心审核流量预算'):
            if rc.get_env() != 'pre':
                login.login_action('t0385252771', '123456')
            self._fbm.chk_flow_budget()
        with allure.step('查询投放预算申请记录'):
            if rc.get_env() != 'pre':
                login.login_action('t0384223793', '123456')
            res = self._bm.qry_cost_apply(auditState=3)
            rs = res['data']['list']
            id_list = []
            if len(rs):
                for i in range(len(rs)):
                    id = rs[i]['id']
                    id_list.append(id)
            ids = ','.join(str(i) for i in id_list)
        with allure.step('流量部门审核审核-通过'):
            if rc.get_env() != 'pre':
                login.login_action('t0384223793', '123456')
            self._bm.chk_cost_apply(ids=ids, auditState=0, auditRemark='拒绝')

    @logger('case')
    @allure.step('查询投放预算管理申请记录-无条件查询-翻页')
    def test_qry_cost_apply_blank_turn_page(self):
        with allure.step('查询投放预算管理申请记录-无条件查询-翻页'):
            self._bm.qry_cost_apply(pageIndex=2)
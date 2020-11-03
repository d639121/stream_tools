#!/usr/bin/python 
# @Time  : 2020/8/5 11:31
# @Author: LOUIE
# @Desc  : 投放预算管理

from common.common_tools import cotool
from common.config_log import logger
from common.http_requests import httprequest
from utils.get_api_data import get_data
from utils.operation_excel import oe


class BudgetMgt:

    def __init__(self):
        self._data = get_data.get_yinhe_data('budget_module/put_budget_manage.yaml')

    @logger()
    def query_budget_data(self, **kwargs):
        '''
        查询投放预算数据
        '''
        data = self._data.get('query_budget_data')
        cotool.quick_request(data, **kwargs)

    @logger()
    def import_budget_data(self, file_name):
        '''
        查询投放预算数据
        '''
        data = self._data.get('import_budget_data')
        url, method, header, params, shared, check = cotool.deal_data(data)
        file_data, content_type, file_path = oe.send_others_file(file_name, params)
        header['content-type'] = content_type
        res = httprequest(url, method, header, file_data)
        cotool.extract_variable(res, shared)
        cotool.assert_res(res, check)

    @logger()
    def qry_cost_apply(self, **kwargs):
        '''
        查询投资预算申请记录
        '''
        data = self._data.get('qry_cost_apply')
        res = cotool.quick_request(data, **kwargs)
        return res

    @logger()
    def export_cost_apply(self, **kwargs):
        '''
        导出投资预算申请记录
        '''
        data = self._data.get('export_cost_apply')
        cotool.quick_request(data, **kwargs)

    @logger()
    def chk_cost_apply(self, **kwargs):
        '''
        审核投资预算申请记录
        '''
        data = self._data.get('chk_cost_apply')
        cotool.quick_request(data, **kwargs)

    @logger()
    def record_cost_apply(self, **kwargs):
        '''
        查看投资预算申请记录-操作记录
        '''
        data = self._data.get('record_cost_apply')
        cotool.quick_request(data, **kwargs)

    @logger()
    def import_budget_fail_data(self, file_name):
        '''
        导入错误格式投放预算数据
        '''
        data = self._data.get('import_budget_file_data')
        url, method, header, params, shared, check = cotool.deal_data(data)
        file_data, content_type, file_path = oe.send_others_file(file_name, params)
        header['content-type'] = content_type
        res = httprequest(url, method, header, file_data)
        cotool.extract_variable(res, shared)
        cotool.assert_res(res, check)

    @logger()
    def import_budget_error_data(self, file_name):
        '''
        导入异常投放预算数据
        '''
        data = self._data.get('import_budget_error_data')
        url, method, header, params, shared, check = cotool.deal_data(data)
        file_data, content_type, file_path = oe.send_others_file(file_name, params)
        header['content-type'] = content_type
        res = httprequest(url, method, header, file_data)
        cotool.extract_variable(res, shared)
        cotool.assert_res(res, check)

    @logger()
    def import_budget_data(self, excel):
        '''
        导入投放预算数据
        '''
        data = self._data.get('import_budget_data')
        url, method, header, params, shared, check = cotool.deal_data(data)
        file_data, content_type, file_path = oe.send_file(excel, params)
        header['content-type'] = content_type
        res = httprequest(url, method, header, file_data)
        cotool.extract_variable(res, shared)
        cotool.assert_res(res, check)
        oe.delete(file_path)

    @logger()
    def export_budget_data(self, **kwargs):
        '''
        导出
        '''
        data = self._data.get('export_budget_data')
        cotool.quick_request(data, **kwargs)

    @logger()
    def export_budget_data_by_type(self, **kwargs):
        '''
        通过条件筛选导出
        '''
        data = self._data.get('export_budget_data_for_type')
        cotool.quick_request(data, **kwargs)

    @logger()
    def update_budget_data(self, **kwargs):
        '''
        修改
        '''
        data = self._data.get('update_budget_data')
        cotool.quick_request(data, **kwargs)

    @logger()
    def failure_budget_data(self, **kwargs):
        '''
        失效
        '''
        data = self._data.get('failure_budget_data')
        cotool.quick_request(data, **kwargs)

    @logger()
    def failure_update_record(self, **kwargs):
        '''
        已失效预算的修改功能
        '''
        data = self._data.get('failure_update_record')
        cotool.quick_request(data, **kwargs)

#!/usr/bin/python 
# @Time  : 2020/8/17 14:22
# @Author: LOUIE
# @Desc  : 部门成单统计

from common.common_tools import cotool
from common.config_log import logger
from utils.get_api_data import get_data


class DeptOrderStatistics:

    def __init__(self):
        self._data = get_data.get_yinhe_data('data_module/dept_order_statistics.yaml')

    @logger()
    def query_dept_order_data(self, **kwargs):
        '''
        查询部门成单统计数据
        '''
        data = self._data.get('query_dept_order_data')
        cotool.quick_request(data, **kwargs)

    @logger()
    def export_dept_order_data(self, **kwargs):
        '''
        导出部门成单统计数据
        '''
        data = self._data.get('export_dept_order_data')
        cotool.quick_request(data, **kwargs)

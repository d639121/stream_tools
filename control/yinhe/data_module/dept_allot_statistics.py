#!/usr/bin/python 
# @Time  : 2020/8/17 14:20
# @Author: LOUIE
# @Desc  : 部门分配统计

from common.common_tools import cotool
from common.config_log import logger
from utils.get_api_data import get_data


class DeptAllotStatistics:

    def __init__(self):
        self._data = get_data.get_yinhe_data('data_module/dept_allot_statistics.yaml')

    @logger()
    def query_dept_allot_data(self, **kwargs):
        '''
        查询部门分配统计数据
        '''
        data = self._data.get('query_dept_allot_data')
        cotool.quick_request(data, **kwargs)

    @logger()
    def export_dept_allot_data(self, **kwargs):
        '''
        导出部门分配统计数据
        '''
        data = self._data.get('export_dept_allot_data')
        cotool.quick_request(data, **kwargs)

    @logger()
    def query_wx_dept_allot_data(self, **kwargs):
        '''
        查询微信CPC部门分配统计数据
        '''
        data = self._data.get('query_wx_dept_allot_data')
        cotool.quick_request(data, **kwargs)

    @logger()
    def export_wx_dept_allot_data(self, **kwargs):
        '''
        导出微信CPC部门分配统计数据
        '''
        data = self._data.get('export_wx_dept_allot_data')
        cotool.quick_request(data, **kwargs)

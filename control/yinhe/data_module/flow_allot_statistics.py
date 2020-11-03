#!/usr/bin/python 
# @Time  : 2020/8/17 14:20
# @Author: LOUIE
# @Desc  : 流量分配统计

from common.common_tools import cotool
from common.config_log import logger
from utils.get_api_data import get_data


class FlowAllotStatistics:

    def __init__(self):
        self._data = get_data.get_yinhe_data('data_module/flow_allot_statistical.yaml')

    @logger()
    def query_flow_allot_data(self, **kwargs):
        '''
        查询流量分配统计数据
        '''
        data = self._data.get('query_flow_allot')
        cotool.quick_request(data, **kwargs)

    @logger()
    def export_flow_allot_data(self, **kwargs):
        '''
        导出流量分配统计数据
        '''
        data = self._data.get('export_flow_allot')
        cotool.quick_request(data, **kwargs)
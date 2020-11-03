#!/usr/bin/python 
# @Time  : 2020/9/12 10:23
# @Author: Fold
# @Desc  : 工单列表，新增工单

from common.common_tools import cotool
from utils.get_api_data import get_data


class WorkSheet:
    def __init__(self):
        self._query_data = get_data.get_CRM_data('worksheet_mgt/add_worksheet.yaml')

    def add_worksheet(self, **kwargs):
        data = self._query_data.get('add_worksheet')
        cotool.quick_request(data, **kwargs)

    def qry_worksheet(self, **kwargs):
        data = self._query_data.get('qry_worksheet')
        cotool.quick_request(data, **kwargs)

    def chk_worksheet(self, **kwargs):
        data = self._query_data.get('chk_worksheet')
        cotool.quick_request(data, **kwargs)



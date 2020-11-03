#!/usr/bin/python 
# @Time  : 2020/8/5 11:23
# @Author: LOUIE
# @Desc  : 成单记录查询
from common.common_tools import cotool
from common.http_requests import httprequest
from utils.get_api_data import get_data
from utils.operation_excel import oe


class OrderRecord:
    def __init__(self):
        self._query_data = get_data.get_yinhe_data('flow_module/qry_order_record.yaml')

    def qry_order_record(self, **kwargs):
        data = self._query_data.get('qry_order_record')
        cotool.quick_request(data, **kwargs)

#!/usr/bin/python 
# @Time  : 2020/8/7 10:22
# @Author: LOUIE
# @Desc  : 分配记录查询

from common.common_tools import cotool
from utils.get_api_data import get_data


class AllotRecordQuery:
    def __init__(self):
        self._query_data = get_data.get_yinhe_data('flow_module/allot_record_query.yaml')

    def allot_record_query(self, **kwargs):
        """
        流量-分配记录查询
        :param kwargs:
        sourceStartTime: 来源开始时间（毫秒）
        sourceEndTime： 来源结束时间（毫秒）
        :return:
        """
        data = self._query_data.get('allot_record_query')
        cotool.quick_request(data, **kwargs)

    def export_record(self, **kwargs):
        """
        导出到院查询记录
        """
        data = self._query_data.get('export_record')
        res = cotool.quick_request(data, **kwargs)
        assert res.status_code == 200

    def export_person_record(self, **kwargs):
        """
        导出到人查询记录
        """
        data = self._query_data.get('export_person_record')
        res = cotool.quick_request(data, **kwargs)
        assert res.status_code == 200




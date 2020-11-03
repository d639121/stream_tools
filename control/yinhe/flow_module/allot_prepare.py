#!/usr/bin/python 
# @Time  : 2020/8/5 11:19
# @Author: LOUIE
# @Desc  : 流量-分配准备
from common.common_tools import cotool
from utils.get_api_data import get_data


class AllotPrepare:
    def __init__(self):
        self._query_data = get_data.get_yinhe_data('flow_module/allot_prepare.yaml')

    def allot_prepare_query(self, **kwargs):
        """
        流量-分配准备查询
        :param kwargs:
        channelId：来源渠道；1，广点通 ...
        :return:
        """
        data = self._query_data.get('query_allot_plan')
        cotool.quick_request(data, **kwargs)
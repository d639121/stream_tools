#!/usr/bin/python 
# @Time  : 2020/8/7 11:22
# @Author: LOUIE
# @Desc  : 导入流量查询

from common.common_tools import cotool
from utils.get_api_data import get_data


class ImportFlowQuery:
    def __init__(self):
        self._query_data = get_data.get_yinhe_data('flow_module/import_flow_query.yaml')

    def import_flow_query(self, **kwargs):
        """
        流量-导入流量查询
        :param kwargs:
        gatherTimeStart: 来源开始时间（毫秒）
        gatherTimeEnd： 来源结束时间（毫秒）
        adId: 创意id
        fileName：文件名
        creatorName：导入操作人
        batchNo：批次号
        processStatus：状态 1，入库成功 2，入库失败
        :return:
        """
        data = self._query_data.get('import_flow_query')
        cotool.quick_request(data, **kwargs)

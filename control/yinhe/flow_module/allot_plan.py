#!/usr/bin/python 
# @Time  : 2020/8/5 11:19
# @Author: LOUIE
# @Desc  : 流量-分配计划
from common.common_tools import cotool
from utils.get_api_data import get_data


class AllotPlan:
    def __init__(self):
        self._query_data = get_data.get_yinhe_data('flow_module/allot_plan.yaml')

    def query_allot_plan(self, **kwargs):
        """
        查询分配计划
        allocType：分配方式；1，混发 2，系统定向 3，手动定向
        subjectId：科目
        allocStatus：分配状态；0，等待分配 1，分配中 2，分配完成 3，分配异常 4，暂停分配
        :return:
        """
        data = self._query_data.get('query_allot_plan')
        res = cotool.quick_request(data, **kwargs)
        return res

    def query_put_plan(self, **kwargs):
        """
        查询投放计划
        """
        data = self._query_data.get('query_put_plan')
        cotool.quick_request(data, **kwargs)

    def export_allot_plan(self, **kwargs):
        """
        导出分配计划
        allocType：分配方式；1，混发 2，系统定向 3，手动定向
        subjectId：科目
        allocStatus：分配状态；0，等待分配 1，分配中 2，分配完成 3，分配异常 4，暂停分配
        :return:
        """
        data = self._query_data.get('export_allot_plan')
        res = cotool.quick_request(data, **kwargs)
        return res
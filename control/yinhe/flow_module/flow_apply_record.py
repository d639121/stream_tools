#!/usr/bin/python 
# @Time  : 2020/8/5 11:23
# @Author: LOUIE
# @Desc  : 流量申请记录

from common.common_tools import cotool
from utils.get_api_data import get_data


class FlowApplyRecord:
    def __init__(self):
        self._query_data = get_data.get_yinhe_data('flow_module/flow_apply_record_query.yaml')

    def flow_apply_record_query(self, **kwargs):
        """
        流量申请记录查询
        applyDateValue：数据申请日期；1，今日申请 2，昨日申请 3，全部
        allocType：分配方式；1，混发 2，系统定向 3，手动定向 4，手动分配 5，直线下发
        auditStatus：审核状态；0，流量部待审核 1，流量部通过... 4，事业部驳回
        subjectId：课程编号
        putMode: 投放模式；1，普通 2，接待 3，高转VIP 4，app 5，小咖
        gatherType：获客方式；1，手机流量 2，QQ流量 3，微信流量
        :return:
        """
        data = self._query_data.get('flow_apply_record_query')
        res = cotool.quick_request(data, **kwargs)
        return res

    def flow_apply_record_query_perssion(self, **kwargs):
        """
        流量申请记录查询
        applyDateValue：数据申请日期；1，今日申请 2，昨日申请 3，全部
        allocType：分配方式；1，混发 2，系统定向 3，手动定向 4，手动分配 5，直线下发
        auditStatus：审核状态；0，流量部待审核 1，流量部通过... 4，事业部驳回
        subjectId：课程编号
        putMode: 投放模式；1，普通 2，接待 3，高转VIP 4，app 5，小咖
        gatherType：获客方式；1，手机流量 2，QQ流量 3，微信流量
        :return:
        """
        data = self._query_data.get('flow_apply_record_query_perssion')
        res = cotool.quick_request(data, **kwargs)
        return res

    def export_flow_apply_record(self, **kwargs):
        """
        导出流量申请记录
        """
        data = self._query_data.get('export_flow_apply_record')
        res = cotool.quick_request(data, **kwargs)
        return res


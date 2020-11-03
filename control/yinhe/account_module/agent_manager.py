#!/usr/bin/python
# @Time : 2020/8/1 17:53
# @Author : LOUIE
# @Desc : 代理商管理

from utils.get_api_data import get_data
from common.common_tools import cotool
from common.config_log import logger


class AgentManager:

    def __init__(self):
        self._data = get_data.get_yinhe_data('account_module/agent_manager.yaml')

    @logger()
    def agent_pageList(self, **kwargs):
        '''
        代理商列表
        :param channelId: 渠道： 6.微信 30.抖音
        :return:
        '''
        data = self._data['agent_pageList']
        cotool.quick_request(data, **kwargs)

    @logger()
    def rebate_pageList(self, **kwargs):
        '''
        返点列表
        :param channelId: 渠道： 6.微信 30.抖音
        :param invalidDateBeginDate: 失效起始时间，invalidDateEndDate：失效截止时间，返点列表独有
        :return:
        '''
        data = self._data['rebate_pageList']
        cotool.quick_request(data, **kwargs)

    @logger()
    def export_record(self, **kwargs):
        '''
        导出代理商列表
        :param channelId: 渠道： 6.微信 30.抖音
        :return:
        '''
        data = self._data['export_record']
        res = cotool.quick_request(data, **kwargs)
        return res

    @logger()
    def export_rebate_record(self, **kwargs):
        '''
        导出返点列表
        :param channelId: 渠道： 6.微信 30.抖音
        :return:
        '''
        data = self._data['export_rebate_record']
        res = cotool.quick_request(data, **kwargs)
        return res

    @logger()
    def add_agent(self, **kwargs):
        data = self._data['add_agent']
        res = cotool.quick_rqt(data, **kwargs)
        return res

    @logger()
    def qry_channel_agency(self, **kwargs):
        data = self._data['qry_channel_agency']
        res = cotool.quick_rqt(data, **kwargs)
        return res

    @logger()
    def add_rebate(self, **kwargs):
        data = self._data['add_rebate']
        res = cotool.quick_rqt(data, **kwargs)
        return res

    @logger()
    def qry_channel_agency_rebate(self, **kwargs):
        data = self._data['qry_channel_agency_rebate']
        res = cotool.quick_rqt(data, **kwargs)
        return res

    @logger()
    def add_channel_agency(self, **kwargs):
        am = AgentManager()
        am.add_agent(self, **kwargs)
        res = am.qry_channel_agency()
        return res

    @logger()
    def add_channel_agency_rebate(self, **kwargs):
        am = AgentManager()
        am.add_rebate(self, **kwargs)
        res = am.qry_channel_agency_rebate()
        return res
#!/usr/bin/python 
# @Time  : 2020/8/17 13:58
# @Author: LOUIE
# @Desc  : 广告渠道管理

from utils.get_api_data import get_data
from common.common_tools import cotool
from common.config_log import logger


class AdChannelMgt:

    def __init__(self):
        self._data = get_data.get_yinhe_data('system_module/ad_channel_mgt.yaml')

    @logger()
    def query_channel(self, **kwargs):
        """
        查询 广告渠道列表
        :param name: 渠道名称
        :param isApiAccess: 是否对接API: 0.否 1.是
        :param state: 状态: 0.禁用 1.启用 None.全部
        """
        data = self._data.get('query_channel')
        res = cotool.quick_request(data, **kwargs)
        return res

    @logger()
    def add_channel(self, **kwargs):
        """
        新增 广告渠道
        :param types: 1.信息流 2.竞价
        :param isApiAccess: 是否对接API: 0.否 1.是
        :param types: 1.信息流 2.竞价
        """
        data = self._data.get('add_channel')
        cotool.quick_request(data, **kwargs)

    @logger()
    def forbid_channel(self, **kwargs):
        """
        启用/禁用 广告渠道
        :param id: 渠道ID
        """
        data = self._data.get('forbid_channel')
        cotool.quick_request(data, **kwargs)

    @logger()
    def edit_channel(self, **kwargs):
        """
        编辑 广告渠道
        :param id: 渠道ID
        :param identifie: 识别词
        """
        data = self._data.get('edit_channel')
        cotool.quick_request(data, **kwargs)


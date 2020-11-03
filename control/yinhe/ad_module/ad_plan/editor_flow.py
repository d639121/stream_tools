#!/usr/bin/python
# @Time    : 2020/8/17 17:16
# @Author  : Jones
# @Desc: 广告计划-流量编辑

from common.http_requests import httprequest
from stream_tools.config.constant import GLOBAL_VAR
from utils.get_api_data import get_data
from common.common_tools import cotool


class EditorFlow:

    def __init__(self):
        self._data = get_data.get_yinhe_data('ad_module/ad_plan.yaml')

    def editor_flow(self, plan_name=None, gather_type=1, ad_type=1, channel_id=4, channel_name='知乎'):
        """
        广告计划--流量-编辑 (需要一个没有创建创意的计划才能编辑)
        :param plan_name: 计划名称
        :param channel_name: 投放渠道名称，要与下面channel_ID对应
        :param channel_id: 投放渠道 1，广点通 2，今日头条 3，哔哩哔哩 4，知乎 5，微博...
        :param ad_type: 广告类型，1，信息流 2，竞价
        :param gather_type: 1,手机流量 2，qq流量 3，微信流量
        :return:
        """
        data = self._data.get('editor_flow')
        url, method, header, params, shared, check = cotool.deal_data(data)
        params['name'] = plan_name
        params['id'] = GLOBAL_VAR['adId']
        params['gatherType'] = gather_type
        params['channelId'] = channel_id
        params['type'] = ad_type
        params['channelName'] = channel_name
        res = httprequest(url, method, header, params)
        cotool.extract_variable(res, shared)
        cotool.assert_res(res, check)
        return res

#!/usr/bin/python
# @Time    : 2020/8/21 11:16
# @Author  : Jones
# @Desc: 广告创意-流量编辑

from common.http_requests import httprequest
from utils.get_api_data import get_data
from common.common_tools import cotool


class EditorIdeaFlow:

    def __init__(self):
        self._data = get_data.get_yinhe_data('ad_module/ad_idea.yaml')

    def editor_idea_flow(self, name=None, gather_type=1, position=None, remark=None):
        """
        广告创意--流量-编辑 (需要一个没有消费记录的创意才能编辑)
        :param remark: 备注
        :param position: 投放位置
        :param name: 计划名称
        :param gather_type: 1,手机流量 2，qq流量 3，微信流量
        :return:
        """
        data = self._data.get('editor_idea_flow')
        url, method, header, params, shared, check = cotool.deal_data(data)
        params['name'] = name
        params['remark'] = remark
        params['gatherType'] = gather_type
        params['position'] = position
        res = httprequest(url, method, header, params)
        cotool.extract_variable(res, shared)
        cotool.assert_res(res, check)
        return res

    def editor_qq_idea_flow(self, name=None, gather_type=2, position=None, remark=None):
        """
        广告创意--qq流量-编辑 (需要一个没有消费记录的创意才能编辑)
        :param remark: 备注
        :param position: 投放位置
        :param name: 计划名称
        :param gather_type: 1,手机流量 2，qq流量 3，微信流量
        :return:
        """
        data = self._data.get('editor_qq_idea_flow')
        url, method, header, params, shared, check = cotool.deal_data(data)
        params['name'] = name
        params['remark'] = remark
        params['gatherType'] = gather_type
        res = httprequest(url, method, header, params)
        cotool.extract_variable(res, shared)
        cotool.assert_res(res, check)
        return res

    def editor_wechat_idea_flow(self, name=None, gather_type=3, remark=None):
        """
        广告创意--微信流量-编辑 (需要一个没有消费记录的创意才能编辑)
        :param remark: 备注
        :param name: 计划名称
        :param gather_type: 1,手机流量 2，qq流量 3，微信流量
        :return:
        """
        data = self._data.get('editor_wechat_idea_flow')
        url, method, header, params, shared, check = cotool.deal_data(data)
        params['name'] = name
        params['remark'] = remark
        params['gatherType'] = gather_type
        res = httprequest(url, method, header, params)
        cotool.extract_variable(res, shared)
        cotool.assert_res(res, check)
        return res
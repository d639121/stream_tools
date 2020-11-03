#!/usr/bin/python
# @Time    : 2020/8/20 17:33
# @Author  : Jones
# @Desc: 导出创意流量
from common.config_log import logger
from common.http_requests import httprequest
from utils.get_api_data import get_data
from common.common_tools import cotool


class ExportIdeaFlow:

    def __init__(self):
        self._data = get_data.get_yinhe_data('ad_module/ad_idea.yaml')

    def export_idea_flow(self, gather_type=1):
        """
        广告计划--流量-导出
        :param gather_type: 1,手机流量 2，qq流量 3，微信流量
        :return:
        """
        data = self._data.get('export_idea_flow')
        url, method, header, params, shared, check = cotool.deal_data(data)
        params['gatherType'] = gather_type
        res = httprequest(url, method, header, params)
        cotool.extract_variable(res, shared)
        cotool.assert_res(res, check)
        return res
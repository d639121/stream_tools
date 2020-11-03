#!/usr/bin/python
# @Time    : 2020/7/17 14:36
# @Author  : Jones
# @desc: 创建二维码

from common.http_requests import httprequest
from utils.get_api_data import get_data
from common.common_tools import cotool


class CreateQrCode:

    def __init__(self):
        self._data = get_data.get_yinhe_data('tool_module/landing_page_tool.yaml')

    def publish_website(self):
        """
        发布落地页
        """
        data = self._data.get('publish_website')
        url, method, header, params, shared, check = cotool.deal_data(data)
        res = httprequest(url, method, header, params)
        cotool.extract_variable(res, shared)
        cotool.assert_res(res, check)
        return res

    def publish_web(self):
        """
        发布落地页
        """
        data = self._data.get('publish_website')
        url, method, header, params, shared, check = cotool.deal_data(data)
        res = httprequest(url, method, header, params)
        cotool.extract_variable(res, shared)
        return res

    def create_qr_code(self):
        """
        生成企业微信二维码，发布
        """
        data = self._data.get('create_qr_code')
        url, method, header, params, shared, check = cotool.deal_data(data)
        res = httprequest(url, method, header, params)
        cotool.extract_variable(res, shared)
        cotool.assert_res(res, check)
        return res

    def add_personal_code(self):
        """
        生成个人微信二维码，发布
        """
        data = self._data.get('add_personal_code')
        url, method, header, params, shared, check = cotool.deal_data(data)
        res = httprequest(url, method, header, params)
        cotool.extract_variable(res, shared)
        cotool.assert_res(res, check)
        return res

    def create_pay_qr_code(self):
        """
        生成带支付组件的二维码
        """
        data = self._data.get('create_pay_qr_code')
        url, method, header, params, shared, check = cotool.deal_data(data)
        res = httprequest(url, method, header, params)
        cotool.extract_variable(res, shared)
        cotool.assert_res(res, check)
        return res

    def create_link(self, **kwargs):
        """
        生成链接
        """
        data = self._data.get('create_link')
        cotool.quick_request(data, **kwargs)

    def crt_link(self, **kwargs):
        """
        生成链接
        """
        data = self._data.get('create_link')
        cotool.quick_rqt(data, **kwargs)

    def ldy_list_data_query(self):
        """
        落地页数据列表统计查询
        """
        data = self._data.get('query_ldy_data')
        # url, method, header, params, shared, check = cotool.deal_data(data)
        # res = httprequest(url, method, header, params)
        # cotool.extract_variable(res, shared)
        # cotool.assert_res(res, check)
        res = cotool.quick_request(data)
        return res


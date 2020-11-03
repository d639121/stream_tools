#!/usr/bin/python
# @Time  : 2020/7/17 15:56
# @Author: LOUIE
# @Desc  : 载体管理

from utils.get_api_data import get_data
from common.http_requests import httprequest
from common.common_tools import cotool
from common.config_log import logger


class CarrierMgt():

    def __init__(self):
        self._data = get_data.get_yinhe_data('tool_module/carrier_mgt.yaml')

    @logger()
    def add_carrier(self, type=None, carrierNo=None):
        """
        新增载体
        :param type: 1.微信载体   2.QQ群载体   3.企业微信载体
        :return:
        """
        data = self._data.get('add_carrier')
        url, method, header, params, shared, check = cotool.deal_data(data)
        if type:
            params['carriers'][0]['type'] = type
        if carrierNo:
            params['carriers'][0]['carrierNo'] = carrierNo
        res = httprequest(url, method, header, params)
        cotool.extract_variable(res, shared)
        cotool.assert_res(res, check)

    @logger()
    def delete_carrier(self, id):
        data = self._data.get('delete_carrier')
        url, method, header, params, shared, check = cotool.deal_data(data)
        url = url + str(id)
        res = httprequest(url, method, header, params)
        cotool.extract_variable(res, shared)
        cotool.assert_res(res, check)

    @logger()
    def carrier_list(self, **kwargs):
        '''
        【银河/工具/载体管理】查询
        :param followTzAccount: 账号  followTzAccount/followName/followNick这三个参数只能同时存在一个
        :param followName: 姓名
        :param followNick: 网名
        :param pageNo: 页码，第几页 默认第一页，可修改
        :param pageSize: 每页数据 默认10条，可修改
        :param kwargs: 上述参数通过kwargs进行传递
        :return:
        '''
        data = self._data.get('carrier_list')
        cotool.quick_request(data, **kwargs)




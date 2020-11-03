#!/usr/bin/python
# @Time : 2020/7/28 19:34
# @Author: Fold
# @Desc: 导入流量数据方法

from common.common_tools import cotool
from common.http_requests import httprequest
from config.constant import GLOBAL_VAR
from utils.get_api_data import get_data
from utils.operation_excel import oe


class ImportFlow():
    '''
    导入流量数据方法
    '''

    def __init__(self):
        self._data = get_data.get_yinhe_data('ad_module/import_single.yaml')
        self._time = str(GLOBAL_VAR['todayTime'])


    def import_mobile_single(self, excel, adNo='93994a6c5fa84e9699d68b5c0c467f5b'):
        '''
        导入手机单个广告流量数据
        :return:
        '''
        data = self._data['import_mobile_single']
        url, method, header, params, shared, check = cotool.deal_data(data)
        params['adNo'] = adNo
        file_data, content_type, file_path = oe.send_file(excel, params)
        header['content-type'] = content_type
        res = httprequest(url, method, header, file_data)
        cotool.extract_variable(res, shared)
        cotool.assert_res(res, check)
        oe.delete(file_path)
        return res

    def import_mobile_unit(self, excel, adNo='93994a6c5fa84e9699d68b5c0c467f5b'):
        '''
        导入手机单个广告流量数据
        :return:
        '''
        data = self._data['import_mobile_single']
        url, method, header, params, shared, check = cotool.deal_data(data)
        params['adNo'] = adNo
        file_data, content_type, file_path = oe.send_file(excel, params)
        header['content-type'] = content_type
        res = httprequest(url, method, header, file_data)
        cotool.extract_variable(res, shared)
        oe.delete(file_path)
        return res

    def import_qq_single(self, excel):
        '''
        导入qq单个广告流量数据
        :return:
        '''
        data = self._data['import_qq_single']
        url, method, header, params, shared, check = cotool.deal_data(data)
        file_data, content_type, file_path = oe.send_file(excel, params)
        header['content-type'] = content_type
        res = httprequest(url, method, header, file_data)
        cotool.extract_variable(res, shared)
        cotool.assert_res(res, check)
        oe.delete(file_path)

    def import_wx_single(self, excel):
        '''
        导入微信单个广告流量数据
        :return:
        '''
        data = self._data['import_wx_single']
        url, method, header, params, shared, check = cotool.deal_data(data)
        file_data, content_type, file_path = oe.send_file(excel, params)
        header['content-type'] = content_type
        res = httprequest(url, method, header, file_data)
        cotool.extract_variable(res, shared)
        cotool.assert_res(res, check)
        oe.delete(file_path)

ipf = ImportFlow()



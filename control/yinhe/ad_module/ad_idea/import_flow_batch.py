#!/usr/bin/python
# @Time : 2020/7/30 21:03
# @Author: Fold
# @Desc: 导入流量数据方法

from common.common_tools import cotool
from common.config_log import logger
from common.http_requests import httprequest
from stream_tools.config.constant import GLOBAL_VAR
from utils.get_api_data import get_data
from utils.operation_excel import oe


class ImportFlowBatch():

    def __init__(self):
        self._data = get_data.get_yinhe_data('ad_module/import_batch.yaml')
        self._time = str(GLOBAL_VAR['todayTime'])

    @logger()
    def import_mobile_batch_normal(self, excel):
        '''
        批量导入手机广告流量数据,普通投放模式
        :return:
        '''
        data = self._data['import_mobile_batch_normal']
        url, method, header, params, shared, check = cotool.deal_data(data)
        file_data, content_type, file_path = oe.send_file(excel, params)
        header['content-type'] = content_type
        res = httprequest(url, method, header, file_data)
        cotool.extract_variable(res, shared)
        cotool.assert_res(res, check)
        oe.delete(file_path)

    @logger()
    def import_mobile_batch_vip(self, excel):
        '''
        批量导入手机广告流量数据,高转VIP投放模式
        :return:
        '''
        data = self._data['import_mobile_batch_vip']
        url, method, header, params, shared, check = cotool.deal_data(data)
        file_data, content_type, file_path = oe.send_file(excel, params)
        header['content-type'] = content_type
        res = httprequest(url, method, header, file_data)
        cotool.extract_variable(res, shared)
        cotool.assert_res(res, check)
        oe.delete(file_path)

    @logger()
    def import_mobile_batch_app(self, excel):
        '''
        批量导入手机广告流量数据,app投放模式
        :return:
        '''
        data = self._data['import_mobile_batch_app']
        url, method, header, params, shared, check = cotool.deal_data(data)
        file_data, content_type, file_path = oe.send_file(excel, params)
        header['content-type'] = content_type
        res = httprequest(url, method, header, file_data)
        cotool.extract_variable(res, shared)
        cotool.assert_res(res, check)
        oe.delete(file_path)

    @logger()
    def import_qq_batch(self, excel):
        '''
        批量导入qq广告流量数据
        :return:
        '''
        data = self._data['import_qq_batch']
        url, method, header, params, shared, check = cotool.deal_data(data)
        file_data, content_type, file_path = oe.send_file(excel, params)
        header['content-type'] = content_type
        res = httprequest(url, method, header, file_data)
        cotool.extract_variable(res, shared)
        cotool.assert_res(res, check)
        oe.delete(file_path)

    @logger()
    def import_wx_batch_normal(self, excel):
        '''
        批量导入微信广告流量数据,普通投放模式
        :return:
        '''
        data = self._data['import_wx_batch_normal']
        url, method, header, params, shared, check = cotool.deal_data(data)
        file_data, content_type, file_path = oe.send_file(excel, params)
        header['content-type'] = content_type
        res = httprequest(url, method, header, file_data)
        cotool.extract_variable(res, shared)
        cotool.assert_res(res, check)
        oe.delete(file_path)

    @logger()
    def import_wx_batch_reception(self, excel):
        '''
        批量导入微信广告流量数据,接待投放模式
        :return:
        '''
        data = self._data['import_wx_batch_reception']
        url, method, header, params, shared, check = cotool.deal_data(data)
        file_data, content_type, file_path = oe.send_file(excel, params)
        header['content-type'] = content_type
        res = httprequest(url, method, header, file_data)
        cotool.extract_variable(res, shared)
        cotool.assert_res(res, check)
        oe.delete(file_path)

    @logger()
    def import_wx_batch_vip(self, excel):
        '''
        批量导入微信广告流量数据,高转VIP投放模式
        :return:
        '''
        data = self._data['import_wx_batch_vip']
        url, method, header, params, shared, check = cotool.deal_data(data)
        file_data, content_type, file_path = oe.send_file(excel, params)
        header['content-type'] = content_type
        res = httprequest(url, method, header, file_data)
        cotool.extract_variable(res, shared)
        cotool.assert_res(res, check)
        oe.delete(file_path)

ifb = ImportFlowBatch()

if __name__ == '__main__':
    ifb.import_mobile_batch_normal()


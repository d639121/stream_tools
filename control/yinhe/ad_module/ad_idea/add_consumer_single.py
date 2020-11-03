#!/usr/bin/python
# @Time : 2020/7/30 20:14
# @Author: Fold
# @Desc :录入单个消费

from common.common_tools import cotool
from common.config_log import logger
from common.http_requests import httprequest
from config.constant import GLOBAL_VAR, const
from control.base.login import login
from utils.get_api_data import get_data
from utils.operation_excel import oe


class ConsumerSingle:

    def __init__(self):
        self._data = get_data.get_yinhe_data('ad_module/consumer_single.yaml')
        self._time = str(GLOBAL_VAR['todayTime'])
        self._cad = get_data.get_yinhe_data('ad_module/ad_plan.yaml')
        self._cct = get_data.get_yinhe_data('ad_module/ad_idea.yaml')

    @logger()
    def add_ad_plan(self):
        '''
        创建广告计划
        :return:
        '''
        data = self._cad.get('program_info_save')
        url, method, header, params, shared, check = cotool.deal_data(data)
        token = login.login_action('t0383212689', '123456')
        header['token'] = token
        res = httprequest(url, method, header, params)
        cotool.extract_variable(res, shared)
        cotool.assert_res(res, check)

    @logger()
    def program_pageList(self):
        '''
        广告计划查询
        :return:
        '''
        data = self._cad.get('program_pageList')
        url, method, header, params, shared, check = cotool.deal_data(data)
        token = login.login_action('t0383212689', '123456')
        header['token'] = token
        res = httprequest(url, method, header, params)
        cotool.extract_variable(res, shared)
        cotool.assert_res(res, check)

    @logger()
    def creativity_save(self):
        '''
        创建广告创意
        :return:
        '''
        data = self._cct.get('creativity_save')
        url, method, header, params, shared, check = cotool.deal_data(data)
        token = login.login_action('t0383212689', '123456')
        header['token'] = token
        res = httprequest(url, method, header, params)
        cotool.extract_variable(res, shared)
        cotool.assert_res(res, check)

    @logger()
    def creativity_pageList(self):
        '''
        广告创意查询
        :return:
        '''
        data = self._cct.get('creativity_pageList')
        url, method, header, params, shared, check = cotool.deal_data(data)
        token = login.login_action('t0383212689', '123456')
        header['token'] = token
        res = httprequest(url, method, header, params)
        cotool.extract_variable(res, shared)
        cotool.assert_res(res, check)

    @logger()
    def send_consumer_single(self):
        '''
        录入手机单个广告消费数据接口
        :return:
        '''
        data = self._data['import_consumer_single']
        url, method, header, params, shared, check = cotool.deal_data(data)
        token = login.login_action('t0383212689', '123456')
        header['token'] = token
        params['costDate'] = const.todayStartTimestamp
        # res = requests.post(url=url, headers=headers_from_data, data=file_data, verify=False).json()
        res = httprequest(url, method, header, params)
        cotool.extract_variable(res, shared)
        cotool.assert_res(res, check)

    def imp_consumer_single(self, **kwargs):
        data = self._data['import_consumer_single']
        cotool.quick_rqt(data, **kwargs)

    @logger()
    def import_consumer_batch(self, excel):
        '''
        批量导入广告消费数据
        :return:
        '''
        data = self._data['import_consumer_batch']
        url, method, header, params, shared, check = cotool.deal_data(data)
        file_data, content_type, file_path = oe.send_file(excel, params)
        header['content-type'] = content_type
        res = httprequest(url, method, header, file_data)
        cotool.extract_variable(res, shared)
        cotool.assert_res(res, check)
        oe.delete(file_path)

    @logger()
    def add_consumer_single(self):
        '''
        从创建广告计划开始到创意，录入消费数据
        :return:
        '''
        self.add_ad_plan()
        self.program_pageList()
        self.creativity_save()
        self.creativity_pageList()
        self.send_consumer_single()



consumer = ConsumerSingle()


if __name__ == '__main__':
    consumer.import_consumer_batch()

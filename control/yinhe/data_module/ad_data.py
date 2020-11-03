#!/usr/bin/python 
# @Time  : 2020/8/17 14:15
# @Author: LOUIE
# @Desc  : 广告数据
from common.common_tools import cotool
from common.config_log import logger
from utils.get_api_data import get_data


class AdData:

    def __init__(self):
        self._data = get_data.get_yinhe_data('data_module/ad_data.yaml')

    @logger()
    def query_ad_data(self, **kwargs):
        '''
        查询广告数据
        '''
        data = self._data.get('query_ad_data')
        cotool.quick_request(data, **kwargs)

    @logger()
    def export_ad_data(self, **kwargs):
        '''
        导出广告数据
        '''
        data = self._data.get('export_ad_data')
        cotool.quick_request(data, **kwargs)

    @logger()
    def prepare_export_ad_data(self, **kwargs):
        '''
        预约导出广告数据
        '''
        data = self._data.get('prepare_export_ad_data')
        cotool.quick_request(data, **kwargs)


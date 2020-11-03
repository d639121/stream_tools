#!/usr/bin/python 
# -*- coding: utf-8 -*-
# @Time    : 2020/7/10 9:40
# @Author  : LOUIE

from utils.get_api_data import get_data
from common.common_tools import cotool
from common.config_log import logger


class Template():

    '''
    模板文件
    '''

    def __init__(self):
        self._data = get_data.get_yinhe_data('template.yaml')

    @logger()
    def get_user_info(self):
        data = self._data.get('get_user_info')
        cotool.quick_request(data)

    @logger()
    def submit_course(self, **kwargs):
        data = self._data.get('submit_course')
        cotool.quick_request(data, **kwargs)

    @logger()
    def query_verify_course(self):
        data = self._data.get('query_verify_course')
        cotool.quick_request(data)

    @logger('block')
    def all(self):
        self.get_user_info()
        self.submit_course()
        self.query_verify_course()

if __name__ == '__main__':
    Template().all()

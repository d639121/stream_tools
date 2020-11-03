#!/usr/bin/python 
# @Time  : 2020/8/11 16:50
# @Author: LOUIE
# @Desc  : 落地页管理

from common.common_tools import cotool
from common.config_log import logger
from utils.get_api_data import get_data


class LandingPageMgt:

    def __init__(self):
        self._data = get_data.get_yinhe_data('tool_module/landing_page_mgt.yaml')

    @logger()
    def page_list(self, **kwargs):
        data = self._data['page_list']
        cotool.quick_request(data, **kwargs)


if __name__ == '__main__':
    lpm = LandingPageMgt()
    lpm.page_list()
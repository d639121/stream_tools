#!/usr/bin/python 
# @Time  : 2020/8/25 11:09
# @Author: LOUIE
# @Desc  : 申请流量

from common.common_tools import cotool
from common.config_log import logger
from utils.get_api_data import get_data


class ApplyFlow:

    def __init__(self):
        self._data = get_data.get_haichuan_data('flow_module/apply_flow.yaml')

    @logger()
    def apply_flow(self, **kwargs):
        '''
        申请流量
        :param gatherType: 获客方式 1.手机流量  2.QQ流量  3.微信流量
        :param putMode: 投放模式 1.普通投放  3.高转VIP课  4.APP
        :param subjectName: 科目名称 1.软件测试
        :param subjectId: 科目ID 1.381-软件测试
        '''
        data = self._data.get('apply_flow')
        cotool.quick_request(data, **kwargs)



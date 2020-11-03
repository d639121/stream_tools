#!/usr/bin/python
# @Time  : 2020/8/5 11:34
# @Author: LOUIE
# @Desc  : 兼职工具

from common.common_tools import cotool
from common.config_log import logger
from utils.get_api_data import get_data


class PartTimeTool:

    def __init__(self):
        self._data = get_data.get_yinhe_data('tool_module/part_time.yaml')

    @logger()
    def part_time_pagelist(self, **kwargs):
        '''
        银河/工具/兼职工具】查询
        :param nick: 员工网名 为空查询全部
        :param name: 员工姓名
        :param pageIndex: 页码，第几页 默认第一页，可修改
        :param pageSize: 每页数据 默认20条，可修改
        :param kwargs: 上述参数通过kwargs进行传递
        :return:
        '''
        data = self._data.get('part_time_pagelist')
        res = cotool.quick_request(data, **kwargs)
        return res

    @logger()
    def add_employee(self, **kwargs):
        data = self._data.get('add_employee')
        cotool.quick_request(data, **kwargs)

    @logger()
    def move_employee(self, **kwargs):
        data = self._data.get('move_employee')
        cotool.quick_request(data, **kwargs)

    @logger()
    def forbid_employee(self, **kwargs):
        data = self._data.get('forbid_employee')
        cotool.quick_request(data, **kwargs)

    @logger()
    def edit_employee(self, **kwargs):
        data = self._data.get('edit_employee')
        cotool.quick_request(data, **kwargs)
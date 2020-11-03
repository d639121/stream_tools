#!/usr/bin/python
# @Time  : 2020/7/17 14:36
# @Author: Jones
# @desc  : 入库记录流量数据查询

from utils.get_api_data import get_data
from common.common_tools import cotool
from common.http_requests import httprequest


class PutRecordQuery:

    def __init__(self):
        self._data = get_data.get_yinhe_data('flow_module/put_record_query.yaml')

    def put_record_query(self):
        """
        入库记录流量数据查询
        """
        data = self._data.get('query_put_flow_data')
        url, method, header, params, shared, check = cotool.deal_data(data)
        res = httprequest(url, method, header, params)
        cotool.extract_variable(res, shared)
        cotool.assert_res(res, check)

    def put_record_list(self, **kwargs):
        """
        入库记录查询列表
        :param allocStatus: 0.未分配  1.已分配  为空.全部
        :param isAdult: 0.未成年  1.成年（默认）
        :param gatherTimeStart | gatherTimeEnd: 成对存在，为起始和截止时间戳
        :param mobile: 手机号
        :param qq: QQ号
        :param courseName: 课程名称
        :param kwargs: 上述参数通过kwargs进行传递
        """
        data = self._data.get('put_record_list')
        res = cotool.quick_request(data, **kwargs)
        return res

    def allot_flow(self, **kwargs):
        '''
        分配流量
        '''
        data = self._data.get('allot_flow')
        cotool.quick_request(data, **kwargs)

    def no_intention_list(self, **kwargs):
        """
        暂无意向列表
        """
        data = self._data.get('no_intention_list')
        cotool.quick_request(data, **kwargs)

    def export_adult_list(self, **kwargs):
        """
        导出成年列表
        """
        data = self._data.get('export_adult_list')
        cotool.quick_request(data, **kwargs)

    def export_nonage_list(self, **kwargs):
        """
        导出未成年列表
        """
        data = self._data.get('export_nonage_list')
        cotool.quick_request(data, **kwargs)

    def add_identify(self, **kwargs):
        """
        新增 识别词
        :param identifie: 识别词
        """
        data = self._data.get('add_identify')
        cotool.quick_request(data, **kwargs)

    def delete_identify(self, **kwargs):
        """
        删除 识别词
        :param id: 识别词ID
        """
        data = self._data.get('delete_identify')
        cotool.quick_request(data, **kwargs)

    def edit_identify(self, **kwargs):
        """
        编辑 识别词
        :param id: 识别词ID
        :param identifie: 识别词
        """
        data = self._data.get('edit_identify')
        cotool.quick_request(data, **kwargs)

    def query_identify(self, **kwargs):
        """
        查询 识别词
        :param identifie: 识别词
        """
        data = self._data.get('query_identify')
        cotool.quick_request(data, **kwargs)


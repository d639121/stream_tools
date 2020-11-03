#!/usr/bin/python
# @Time    : 2020/8/26 17:30
# @Author  : Jones
# @Desc: 公众号管理
from common.config_log import logger
from common.http_requests import httprequest
from utils.get_api_data import get_data
from common.common_tools import cotool
from utils.operation_excel import oe


class PublicAccountManager:

    def __init__(self):
        self._data = get_data.get_yinhe_data('ad_module/public_account_manager.yaml')

    @logger()
    def add_public_account(self, **kwargs):
        '''
        新增公众号
        '''
        data = self._data.get('add_public_account')
        cotool.quick_request(data, **kwargs)

    @logger()
    def query_public_account(self, **kwargs):
        '''
        通过公众号名称获取公众号信息
        '''
        data = self._data.get('query_public_account')
        cotool.quick_request(data, **kwargs)

    @logger()
    def editor_public_account(self, **kwargs):
        '''
        修改公众号信息
        '''
        data = self._data.get('editor_public_account')
        cotool.quick_request(data, **kwargs)

    @logger()
    def del_public_account(self, **kwargs):
        '''
        删除公众号
        '''
        data = self._data.get('del_public_account')
        cotool.quick_request(data, **kwargs)

    @logger()
    def query_del_public_account(self, **kwargs):
        '''
        删除公众号后查询该公众号是否存在
        '''
        data = self._data.get('query_del_public_account')
        cotool.quick_request(data, **kwargs)

    @logger()
    def import_public_account(self, excel):
        """
        批量导入公众号
        :param excel: 需要导入的excel数据
        :return:
        """
        data = self._data['import_public_account']
        url, method, header, params, shared, check = cotool.deal_data(data)
        file_data, content_type, file_path = oe.send_file(excel, params)
        header['content-type'] = content_type
        res = httprequest(url, method, header, file_data)
        cotool.extract_variable(res, shared)
        cotool.assert_res(res, check)
        oe.delete(file_path)


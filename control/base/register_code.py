#!/usr/bin/python 
# @Time  : 2020/9/10 21:26
# @Author: LOUIE
# @Desc  : 运营后台获取注册验证码

from common.common_tools import cotool
from common.config_log import logger
from common.http_requests import httprequest
from config.set_token import SetToken
from utils.get_api_data import get_data


class RegisterCode:

    def __init__(self):
        self._data = get_data.get_base_data('register_code.yaml')
        self.cookie = SetToken().get_jsessionid()

    @logger()
    def login_operation(self):
        '''
        登录运营后台
        '''
        url, method, header, params, shared, check = cotool.deal_data(self._data['login_operation'])
        header['cookie'] = self.cookie
        res = httprequest(url, method, header, params)
        cotool.extract_variable(res, shared)
        cotool.assert_res(res, check)

    @logger('block')
    def register_code(self):
        '''
        获取注册验证码
        '''
        self.login_operation()
        url, method, header, params, shared, check = cotool.deal_data(self._data['register_code'])
        header['cookie'] = self.cookie
        res = httprequest(url, method, header, params)
        cotool.extract_variable(res, shared)
        cotool.assert_res(res, check)

    @logger('block')
    def register_code_phone(self, phone):
        '''
        获取注册验证码
        '''
        self.login_operation()
        url, method, header, params, shared, check = cotool.deal_data(self._data['register_code'])
        header['cookie'] = self.cookie
        params['phone'] = phone
        res = httprequest(url, method, header, params)
        cotool.extract_variable(res, shared)
        cotool.assert_res(res, check)


if __name__ == '__main__':
    rec = RegisterCode()
    # rec.login_operation()
    rec.register_code()
#!/usr/bin/python 
# -*- coding: utf-8 -*-
# @Time    : 2020/7/21 10:47
# @Author  : LOUIE

from common.common_tools import cotool
from utils.get_api_data import get_data
from config.constant import GLOBAL_VAR
from common.http_requests import httprequest
from utils.encrypt_func import encrypt_passwd


class Login:

    def __init__(self):
        self._data = get_data.get_base_data('login_account.yaml')
        self._user_info_data = get_data.get_base_data('userinfo.yaml')

    def login_action(self, account=None, password=123456, type=None, action=True):
        data = None
        if type is None:
            data = self._data['tz_platform_account']
        elif type == 'phone':
            data = self._data['tz_platform_account']
        elif type == 'class':
            data = self._data['tz_classroom_account']
        url, method, header, params, shared, check = cotool.deal_data(data)
        if account is not None:
            params['account'] = account
            params['password'] = encrypt_passwd(password)
        res = httprequest(url, method, header, params)
        cotool.extract_variable(res, shared)
        cotool.assert_res(res, check)
        token = res['data']['token']
        if action:
            GLOBAL_VAR['token'] = token
        return token

    def get_user_info(self):
        data = self._user_info_data['get_user_info']
        cotool.quick_request(data)

    def verification_code_login(self):
        data = self._data.get('classroom_verification_login')
        cotool.quick_request(data)

    def get_personal_information(self):
        data = self._data.get('get_personal_information')
        cotool.quick_request(data)



login = Login()

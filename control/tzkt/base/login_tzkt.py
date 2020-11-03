#!/usr/bin/python 
# @Time  : 2020/8/19 15:25
# @Author: LOUIE
# @Desc  : 潭州课堂学员登录和注册

from common.common_tools import cotool
from common.config_log import logger
from utils.get_api_data import get_data
from control.base.register_code import RegisterCode


class LoginTZKT:

    def __init__(self):
        self._data = get_data.get_tzkt_data('login_tzkt.yaml')

    @logger()
    def login_tzkt(self, **kwargs):
        '''
        登录潭州课堂
        '''
        data = self._data.get('login_tzkt')
        cotool.quick_request(data, **kwargs)

    @logger()
    def register_tzkt(self, **kwargs):
        '''
        注册潭州课堂
        '''
        RegisterCode().register_code()
        data = self._data.get('register_tzkt')
        cotool.quick_request(data, **kwargs)


if __name__ == '__main__':
    rec = LoginTZKT()
    rec.register_tzkt()

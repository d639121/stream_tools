#!/usr/bin/python
# @Time  : 2020/7/27 10:13
# @Author: Jones
# @Desc  : 学员录入

from common.http_requests import httprequest
from stream_tools.config.read_config import rc
from control.base.login import login
from utils.get_api_data import get_data
from common.common_tools import cotool
from utils.operation_excel import oe


class StudentInput:

    def __init__(self):
        self._data = get_data.get_yinhe_data('flow_module/student_input.yaml')

    def import_phone_flow_not_free(self):
        """
        导入（手机流量）--未拥有【免费流量组】
        """
        data = self._data.get('student_input_import_for_phone_not_free')
        url, method, header, params, shared, check = cotool.deal_data(data)
        excel = {"1": ['客户姓名', '手机号码', 'QQ号码', '微信号', 'QQ群'],
                 "2": ['lily', '13012345678', '23121231', '123456', '123456']}
        if rc.get_env() == 'pre':
            token = login.login_action('t0322511032')
        else:
            token = login.login_action(account='m17673155296')
        file_data, content_type, file_path = oe.send_file(excel, params)
        header['token'] = token
        header['content-type'] = content_type
        res = httprequest(url, method, header, file_data)
        cotool.extract_variable(res, shared)
        cotool.assert_res(res, check)
        oe.delete(file_path)

    def import_phone_flow_free(self):
        """
        导入（手机流量）--拥有【免费流量组】
        """
        data = self._data.get('student_input_import_for_phone_free')
        url, method, header, params, shared, check = cotool.deal_data(data)
        excel = {"1": ['客户姓名', '手机号码', 'QQ号码', '微信号', 'QQ群'],
                 "2": ['lily', '13012345678', '23121231', '123456', '123456']}
        if rc.get_env() == 'pre':
            token = login.login_action('t0322511032')
        else:
            token = login.login_action('m17673155297')
        file_data, content_type, file_path = oe.send_file(excel, params)
        header['content-type'] = content_type
        header['token'] = token
        res = httprequest(url, method, header, file_data)
        cotool.extract_variable(res, shared)
        cotool.assert_res(res, check)
        oe.delete(file_path)

    def import_qq_flow_free(self):
        """
        导入（QQ流量）--拥有【免费流量组】
        """
        data = self._data.get('student_input_import_for_qq_free')
        url, method, header, params, shared, check = cotool.deal_data(data)
        excel = {"1": ['客户姓名', '手机号码', 'QQ号码', '微信号', 'QQ群'],
                 "2": ['lily', '13012345678', '23121231', '123456', '123456']}
        if rc.get_env() == 'pre':
            token = login.login_action('t0322511032')
        else:
            token = login.login_action('m17673155297')
        file_data, content_type, file_path = oe.send_file(excel, params)
        header['content-type'] = content_type
        header['token'] = token
        res = httprequest(url, method, header, file_data)
        cotool.extract_variable(res, shared)
        cotool.assert_res(res, check)
        oe.delete(file_path)

    def import_qq_flow_not_free(self):
        """
        导入（QQ流量）--拥有【免费流量组】
        """
        data = self._data.get('student_input_import_for_qq_not_free')
        url, method, header, params, shared, check = cotool.deal_data(data)
        excel = {"1": ['客户姓名', '手机号码', 'QQ号码', '微信号', 'QQ群'],
                 "2": ['lily', '13012345678', '23121231', '123456', '123456']}
        if rc.get_env() == 'pre':
            token = login.login_action('t0322511032')
        else:
            token = login.login_action('m17673155297')
        file_data, content_type, file_path = oe.send_file(excel, params)
        header['content-type'] = content_type
        header['token'] = token
        res = httprequest(url, method, header, file_data)
        cotool.extract_variable(res, shared)
        cotool.assert_res(res, check)
        oe.delete(file_path)

    def import_wx_flow_not_free(self):
        """
        学员录入--导入（微信流量）--未拥有【免费流量组】
        """
        data = self._data.get('student_input_import_for_wx_not_free')
        url, method, header, params, shared, check = cotool.deal_data(data)
        excel = {"1": ['客户姓名', '手机号码', 'QQ号码', '微信号', 'QQ群'],
                 "2": ['lily', '13012345678', '23121231', '123456', '123456']}
        if rc.get_env() == 'pre':
            token = login.login_action('t0322511032')
        else:
            token = login.login_action(account='m17673155296')
        file_data, content_type, file_path = oe.send_file(excel, params)
        header['token'] = token
        header['content-type'] = content_type
        res = httprequest(url, method, header, file_data)
        cotool.extract_variable(res, shared)
        cotool.assert_res(res, check)
        oe.delete(file_path)

    def import_wx_flow_free(self, token=None, type=1, subject_id=280, subject_name='PHP'):
        """
        学员录入--导入（微信流量）--拥有【免费流量组】
        """
        if type == 1:
            data = self._data.get('student_input_import_for_wx_free')
        else:
            data = self._data.get('student_input_import_for_wx_free_perssion')
        url, method, header, params, shared, check = cotool.deal_data(data)
        excel = {"1": ['客户姓名', '手机号码', 'QQ号码', '微信号', 'QQ群'],
                 "2": ['lily', '13012345678', '23121231', '123456', '123456']}
        if token is None:
            if rc.get_env() == 'pre':
                token = login.login_action('t0322511032')
            else:
                token = login.login_action('m17673155297')
        file_data, content_type, file_path = oe.send_file(excel, params)
        header['content-type'] = content_type
        header['token'] = token
        params['subjectId'] = subject_id
        params['subjectName'] = subject_name
        res = httprequest(url, method, header, file_data)
        cotool.extract_variable(res, shared)
        cotool.assert_res(res, check)
        oe.delete(file_path)

    def add_student(self, type, token=None, subject_id=280, subject_name='PHP', rdc='1001-2001-4569-4570-4571-4572'):
        """
        录入
        :param rdc: 部门连
        :param subject_name: 科目名称
        :param subject_id: 科目id
        :param type:1,手机流量 2，QQ流量 3，微信流量
        :param token:1，拥有免费流量组 2，未拥有免费流量组
        :return:
        """
        _data = get_data.get_yinhe_data('flow_module/student_input.yaml')
        data = _data['add_student']
        url, method, header, params, shared, check = cotool.deal_data(data)
        if token == 1:
            if rc.get_env() == 'pre':
                token = login.login_action('t0322511032')
                header['token'] = token
            else:
                token = login.login_action('m17673155297')
                header['token'] = token
        elif token == 2:
            if rc.get_env() == 'pre':
                token = login.login_action('t0322511032')
                header['token'] = token
            else:
                token = login.login_action('m17673155296')
                header['token'] = token
        params['gatherType'] = type
        params['subjectId'] = subject_id
        params['subjectName'] = subject_name
        params['receiveDeptIdChain'] = rdc
        # data['phoneNumber'] = phone_number
        res = httprequest(url, method, header, params)
        cotool.extract_variable(res, shared)
        cotool.assert_res(res, check)

    def student_input_query(self, **kwargs):
        """
        流量-分配记录查询
        :param kwargs:
        :param gatherTimeStart: 来源开始时间（毫秒）
        :param gatherTimeEnd： 来源结束时间（毫秒）
        :param qq: qq号码
        :return:
        """
        data = self._data.get('student_input_query')
        cotool.quick_request(data, **kwargs)

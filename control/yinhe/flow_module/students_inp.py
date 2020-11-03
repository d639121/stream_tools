#!/usr/bin/python 
# @Time  : 2020/10/28 15:13
# @Author: Fold
# @Desc  : 学员录入/导入
from common.common_tools import cotool
from common.http_requests import httprequest
from config.constant import const
from utils.get_api_data import get_data
from utils.operation_excel import oe


class StudentsInput:

    def __init__(self):
        self._data = get_data.get_yinhe_data('flow_module/student_input.yaml')

    def imp_phone_flow_free(self, subjectId='280', subjectName='PHP'):
        """
        导入（手机流量）--拥有【免费流量组】
        :param subjectId: 科目id
        :param subjectName: 科目名称
        """
        phone = const.phoneNumber
        data = self._data.get('student_input_import_for_phone_free')
        url, method, header, params, shared, check = cotool.deal_data(data)
        params['subjectId'] = subjectId
        params['subjectName'] = subjectName
        excel = {"1": ['客户姓名', '手机号码', 'QQ号码', '微信号', 'QQ群'],
                 "2": ['lily', phone, '23121231', '123456', '123456']}
        file_data, content_type, file_path = oe.send_file(excel, params)
        header['content-type'] = content_type
        res = httprequest(url, method, header, file_data)
        print(res)
        cotool.extract_variable(res, shared)
        cotool.assert_res(res, check)
        oe.delete(file_path)

    def imp_qq_flow_free(self, subjectId=280, subjectName='PHP'):
        """
        导入（QQ流量）--拥有【免费流量组】
        :param subjectId: 科目id
        :param subjectName: 科目名称
        """
        phone = const.phoneNumber
        qq = const.qq
        data = self._data.get('student_input_import_for_qq_free')
        url, method, header, params, shared, check = cotool.deal_data(data)
        excel = {"1": ['客户姓名', '手机号码', 'QQ号码', '微信号', 'QQ群'],
                 "2": ['lily', phone, qq, '123456', '123456']}
        params['subjectId'] = subjectId
        params['subjectName'] = subjectName
        file_data, content_type, file_path = oe.send_file(excel, params)
        header['content-type'] = content_type
        res = httprequest(url, method, header, file_data)
        cotool.extract_variable(res, shared)
        cotool.assert_res(res, check)
        oe.delete(file_path)
        return res

    def imp_wx_flow_free(self, subjectId=280, subjectName='PHP'):
        """
        学员录入--导入（微信流量）--拥有【免费流量组】
        :param subjectId: 科目id
        :param subjectName: 科目名称
        """
        phone = const.phoneNumber
        qq = const.qq
        data = self._data.get('student_input_import_for_wx_free')
        url, method, header, params, shared, check = cotool.deal_data(data)
        excel = {"1": ['客户姓名', '手机号码', 'QQ号码', '微信号', 'QQ群'],
                 "2": ['lily', 'phone', qq, qq, '123456']}
        params['subjectId'] = subjectId
        params['subjectName'] = subjectName
        file_data, content_type, file_path = oe.send_file(excel, params)
        header['content-type'] = content_type
        res = httprequest(url, method, header, file_data)
        cotool.extract_variable(res, shared)
        cotool.assert_res(res, check)
        oe.delete(file_path)
        return res

    def add_student(self, gatherType=1, subject_id=280, subject_name='PHP', rdc='1001-2001-4569-4570-4571-4572'):
        """
        录入
        :param gatherType: 1,手机流量 2，QQ流量 3，微信流量
        :param rdc: 部门连
        :param subject_name: 科目名称
        :param subject_id: 科目id
        :return:
        """
        data = self._data.get('add_student')
        url, method, header, params, shared, check = cotool.deal_data(data)
        params['gatherType'] = gatherType
        params['subjectId'] = subject_id
        params['subjectName'] = subject_name
        params['receiveDeptIdChain'] = rdc
        res = httprequest(url, method, header, params)
        cotool.extract_variable(res, shared)
        return res
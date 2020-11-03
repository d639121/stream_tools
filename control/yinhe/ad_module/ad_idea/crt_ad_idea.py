#!/usr/bin/python
# @Time    : 2020/7/14 16:16
# @Author  : Jones
# @desc: 创建微信广告创意
from common.http_requests import httprequest
from utils.get_api_data import get_data
from common.common_tools import cotool
from config.constant import GLOBAL_VAR


class AddAdIdea:

    def __init__(self):
        self._data = get_data.get_yinhe_data('ad_module/ad_idea.yaml')
        self._ad_data = self._data.get('get_ad_data_id')

    def get_idea_id_for_tools(self, gatherType=3, adid=None):
        '''
        获取创意ID(工具使用方法)
        :param gatherType: 流量类型 1，手机流量 2，qq流量 3，微信流量
        :return:
        '''
        self._data = get_data.get_yinhe_data('ad_module/ad_idea.yaml')
        data = self._data.get('get_ad_ideas_id_for_tools')
        url, method, header, params, shared, check = cotool.deal_data(data)
        params['gatherType'] = gatherType
        params['id'] = adid
        res = httprequest(url, method, header, params)
        cotool.extract_variable(res, shared)
        return res

    def query_zt_info(self, isEnterpriseWx=0, **kwargs):
        '''
        查询载体信息
        :param isEnterpriseWx: 载体类型，0微信 1企业微信
        :param kwargs: 载体名称 vector=***
        :return:
        '''

        if isEnterpriseWx == 0:
            data = self._data.get('query_zt_info_for_person')
            url, method, header, params, shared, check = cotool.deal_data(data)
            params['isEnterpriseWx'] = isEnterpriseWx
            if kwargs:
                params = dict(params, **kwargs)
            res = httprequest(url, method, header, params)
            cotool.extract_variable(res, shared)
            cotool.assert_res(res, check)
            return res
        else:
            data = self._data.get('query_zt_info_for_company')
            url, method, header, params, shared, check = cotool.deal_data(data)
            params['isEnterpriseWx'] = isEnterpriseWx
            if kwargs:
                params = dict(params, **kwargs)
            res = httprequest(url, method, header, params)
            cotool.extract_variable(res, shared)
            cotool.assert_res(res, check)
            return res

    def qry_vector_api(self, **kwargs):
        '''
        查询载体
        :param kwargs:
        :return:
        '''
        data = self._data.get('qry_vector_info_for_company')
        res = cotool.quick_rqt(data, **kwargs)
        return res

    def create_wc_ad_idea_for_tools(self, vector=None, isEnterpriseWx=0):
        '''
        创建微信广告创意(工具使用方法)
        :param vector: 载体名称
        :param isEnterpriseWx: 微信/企业微信   0，微信   1，企业微信
        :return:
        '''
        if vector is not None:
            self.query_zt_info(isEnterpriseWx=isEnterpriseWx, vector=vector)
        if isEnterpriseWx == 0:
            data = self._data.get('create_person_wc_ad_ideas')
            url, method, header, params, shared, check = cotool.deal_data(data)
            params['vector'] = GLOBAL_VAR['carrierNo']
            params['receiveDeptId'] = GLOBAL_VAR['belongDepartmentId']
            params['followerTanzkAccount'] = GLOBAL_VAR['followTzAccount']
            params['receiveDeptName'] = GLOBAL_VAR['receiveDeptName']
            params['vectorId'] = GLOBAL_VAR['zt_id']
            params['vectorName'] = GLOBAL_VAR['carrierName']
            params['programId'] = GLOBAL_VAR['adId']
            params['programName'] = GLOBAL_VAR['adName']
            res = httprequest(url, method, header, params)
            cotool.extract_variable(res, shared)
            return res
        else:
            data = self._data.get('create_wc_ad_ideas')
            url, method, header, params, shared, check = cotool.deal_data(data)
            params['vector'] = GLOBAL_VAR['carrierNo']
            params['receiveDeptId'] = GLOBAL_VAR['belongDepartmentId']
            params['followerTanzkAccount'] = GLOBAL_VAR['followTzAccount']
            params['receiveDeptName'] = GLOBAL_VAR['receiveDeptName']
            params['companyWechatId'] = GLOBAL_VAR['companyWechatId']
            params['vectorId'] = GLOBAL_VAR['zt_id']
            params['vectorName'] = GLOBAL_VAR['carrierName']
            params['programId'] = GLOBAL_VAR['adId']
            params['programName'] = GLOBAL_VAR['adName']
            res = httprequest(url, method, header, params)
            cotool.extract_variable(res, shared)
            return res

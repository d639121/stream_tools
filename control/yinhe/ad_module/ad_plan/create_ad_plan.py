#!/usr/bin/python
# @Time    : 2020/7/14 16:16
# @Author  : Jones
# @Desc: 创建微信广告计划

from common.config_log import logger
from common.http_requests import httprequest
from utils.get_api_data import get_data
from common.common_tools import cotool


class CreateAdPlan:

    def __init__(self):
        self._data = get_data.get_yinhe_data('ad_module/ad_plan.yaml')

    def create_ad_plan(self, gatherType=3, allocInstType=3, putMode=1):
        '''
        创建广告计划
        :param gatherType: 流量类型 1，手机流量 2，QQ流量 3，微信流量
        :param allocInstType: 分配模式，不同流量类型，对应分配模式不一致
        :return:
        '''
        data = self._data.get('create_wechat_ad_plant')
        # cotool.quick_request(data, **kwargs)
        url, method, header, params, shared, check = cotool.deal_data(data)
        params['gatherType'] = gatherType
        params['allocInstType'] = allocInstType
        params['putMode'] = putMode
        res = httprequest(url, method, header, params)
        cotool.extract_variable(res, shared)
        cotool.assert_res(res, check)
        return res

    def create_wc_ad_plan_for_model(self, put_model=1, channelId=4):
        data = self._data.get('create_wechat_ad_plant')
        url, method, header, params, shared, check = cotool.deal_data(data)
        params['putMode'] = put_model
        params['channelId']=channelId
        res = httprequest(url, method, header, params)
        cotool.extract_variable(res, shared)
        cotool.assert_res(res, check)
        return res

    def create_wc_xiaoka_ad_plan(self):
        """
        创建微信广告计划-直线下发
        """
        data = self._data.get('create_wechat_xiaoka_ad_plan')
        url, method, header, params, shared, check = cotool.deal_data(data)
        res = httprequest(url, method, header, params)
        cotool.extract_variable(res, shared)
        cotool.assert_res(res, check)
        return res

    def get_plan_id(self, gatherType=3):
        """
        获取微信广告计划ID
        """
        data = self._data.get('get_plan_id')
        url, method, header, params, shared, check = cotool.deal_data(data)
        params['gatherType'] = gatherType
        res = httprequest(url, method, header, params)
        cotool.extract_variable(res, shared)
        cotool.assert_res(res, check)
        return res

    def create_wc_ad_plan_for_hand(self):
        """
        创建微信广告计划-手动分配
        """
        data = self._data.get('create_wechat_ad_plant_for_hand')
        url, method, header, params, shared, check = cotool.deal_data(data)
        res = httprequest(url, method, header, params)
        cotool.extract_variable(res, shared)
        cotool.assert_res(res, check)
        return res

    def create_wc_ad_plan_for_reception(self):
        """
        创建微信广告计划-直线下发，接待投放模式
        """
        data = self._data.get('create_wechat_ad_plant_for_reception')
        url, method, header, params, shared, check = cotool.deal_data(data)
        res = httprequest(url, method, header, params)
        cotool.extract_variable(res, shared)
        cotool.assert_res(res, check)
        return res

    @logger()
    def program_info_save(self, **kwargs):
        '''
        【银河/广告/广告计划】新增广告计划，计划分配-普通
        :return:
        '''
        data = self._data.get('program_info_save')
        cotool.quick_request(data, **kwargs)

    @logger()
    def program_inf_save(self, **kwargs):
        '''
        【银河/广告/广告计划】新增广告计划，计划分配-普通
        :return:
        '''
        data = self._data.get('program_info_save')
        cotool.quick_rqt(data, **kwargs)

    @logger()
    def program_info_save_direct(self, **kwargs):
        '''
        【银河/广告/广告计划】新增广告计划，直线下发分配方式，普通投放模式：putMode=1,allocInstType=3；高转VIP：putMode=3,allocInstType=3
        :return:
        '''
        data = self._data.get('program_info_save_direct')
        cotool.quick_request(data, **kwargs)

    @logger()
    def program_pageList(self, **kwargs):
        '''
        广告计划查询
        :return:
        '''
        data = self._data.get('program_pageList')
        cotool.quick_request(data, **kwargs)

    @logger()
    def program_page_list(self, **kwargs):
        '''
        广告计划查询
        :return:
        '''
        data = self._data.get('program_pageList')
        cotool.quick_rqt(data, **kwargs)

    @logger()
    def query_ad_plan(self, **kwargs):
        """
        通过任意条件查询广告计划
        :param kwargs:
        :return:
        """
        data = self._data.get('query_ad_plan')
        cotool.quick_request(data, **kwargs)

    @logger()
    def ad_plan(self, **kwargs):
        '''
        广告计划相关接口
        :return:
        '''
        self.program_info_save(**kwargs)
        self.program_pageList(**kwargs)

    @logger()
    def ad_plan_direct(self, **kwargs):
        '''
        直线下发分配方式，普通投放模式：putMode=1,allocInstType=3；高转VIP：putMode=3,allocInstType=3
        :return:
        '''
        self.program_info_save_direct(**kwargs)
        self.program_pageList()




#!/usr/bin/python
# @Time    : 2020/7/14 16:16
# @Author  : Jones
# @desc: 创建微信广告创意
from common.config_log import logger
from common.http_requests import httprequest
from utils.get_api_data import get_data
from common.common_tools import cotool


class CreateAdIdea:

    def __init__(self):
        self._data = get_data.get_yinhe_data('ad_module/ad_idea.yaml')
        self._ad_data = self._data.get('get_ad_data_id')

    def get_idea_id(self, gatherType=3):
        '''
        获取创意ID
        :param gatherType: 流量类型 1，手机流量 2，qq流量 3，微信流量
        :return:
        '''
        self._data = get_data.get_yinhe_data('ad_module/ad_idea.yaml')
        data = self._data.get('get_ad_ideas_id')
        url, method, header, params, shared, check = cotool.deal_data(data)
        params['gatherType'] = gatherType
        res = httprequest(url, method, header, params)
        cotool.extract_variable(res, shared)
        cotool.assert_res(res, check)
        return res

    def create_wc_ad_idea(self):
        """
        创建企业微信广告创意create_person_wc_ad_ideas
        """
        data = self._data.get('create_wc_ad_ideas')
        url, method, header, params, shared, check = cotool.deal_data(data)
        res = httprequest(url, method, header, params)
        cotool.extract_variable(res, shared)
        cotool.assert_res(res, check)
        return res

    def create_person_wc_ad_idea(self):
        """
        创建个人微信广告创意
        """
        data = self._data.get('create_person_wc_ad_ideas')
        url, method, header, params, shared, check = cotool.deal_data(data)
        res = httprequest(url, method, header, params)
        cotool.extract_variable(res, shared)
        cotool.assert_res(res, check)
        return res

    def create_qq_idea(self):
        '''
        创建QQ广告创意
        :return:
        '''
        data = self._data.get('create_qq_ad_ideas')
        url, method, header, params, shared, check = cotool.deal_data(data)
        res = httprequest(url, method, header, params)
        cotool.extract_variable(res, shared)
        cotool.assert_res(res, check)
        return res

    def create_ad_idea(self, gatherType=1):
        '''
        创建广告创意
        :param gatherType: 流量类型 1，手机流量 2，QQ流量 3，微信流量
        :return:
        '''
        data = self._data.get('create_ad_ideas')
        url, method, header, params, shared, check = cotool.deal_data(data)
        params['gatherType'] = gatherType
        res = httprequest(url, method, header, params)
        cotool.extract_variable(res, shared)
        cotool.assert_res(res, check)
        return res

    def create_personal_wechat_ad_ideas(self):
        """
        创建个人微信广告创意
        """
        data = self._data.get('create_personal_wechat_ad_ideas')
        url, method, header, params, shared, check = cotool.deal_data(data)
        res = httprequest(url, method, header, params)
        cotool.extract_variable(res, shared)
        cotool.assert_res(res, check)
        return res

    def ad_idea_flow_data_query(self):
        """
        广告创意流量数据查询
        """
        data = self._data.get('query_ad_ideas_data')
        url, method, header, params, shared, check = cotool.deal_data(data)
        res = httprequest(url, method, header, params)
        cotool.extract_variable(res, shared)
        cotool.assert_res(res, check)
        return res

    @logger()
    def creativity_save(self, **kwargs):
        '''
        新增广告创意-需要验证码（手机）
        '''
        data = self._data.get('creativity_save')
        cotool.quick_request(data, **kwargs)

    @logger()
    def creativity_sav(self, **kwargs):
        '''
        新增广告创意-需要验证码（手机）
        '''
        data = self._data.get('creativity_save')
        cotool.quick_rqt(data, **kwargs)

    @logger()
    def creativity_save_direct(self, **kwargs):
        '''
        新增广告创意-需要验证码（手机）直线下发模式
        '''
        data = self._data.get('creativity_save_direct')
        cotool.quick_request(data, **kwargs)

    @logger()
    def creativity_pageList(self, **kwargs):
        '''
        广告创意查询
        '''
        data = self._data.get('creativity_pageList')
        res = cotool.quick_request(data, **kwargs)
        return res

    @logger()
    def creativity_page_list(self, **kwargs):
        '''
        广告创意查询
        '''
        data = self._data.get('creativity_pageList')
        res = cotool.quick_rqt(data, **kwargs)
        return res

    @logger()
    def create_creativity(self, **kwargs):
        '''
        创建广告创意
        '''
        self.creativity_save(**kwargs)
        self.creativity_pageList()

    @logger()
    def create_creativity_direct(self, **kwargs):
        '''
        创建广告创意
        '''
        self.creativity_save_direct(**kwargs)
        self.creativity_pageList()

    @logger()
    def add_ad_data(self, **kwargs):
        '''
        新增广告数据
        '''
        data = self._data.get('add_ad_data')
        cotool.quick_request(data, **kwargs)

    @logger()
    def get_ad_data_id(self, gatherType=1):
        '''
        获取广告数据id
        :param gatherType: 流量类型 1，手机流量，2，QQ流量 3，微信流量
        :return:
        '''
        self._data = get_data.get_yinhe_data('ad_module/ad_idea.yaml')
        ad_data = self._data.get('get_ad_data_id')
        url, method, header, params, shared, check = cotool.deal_data(ad_data)
        params['gatherType'] = gatherType
        res = httprequest(url, method, header, params)
        cotool.extract_variable(res, shared)
        cotool.assert_res(res, check)
        return res

    @logger()
    def change_ad_data(self, noExposure=2, noClicks=2, cost=2, rebates=1.3):
        '''
        修改广告数据
        :param noExposure: 曝光量
        :param cost: 账面消费
        :param noClicks:点击量
        :param rebates: 返点
        :return:
        '''
        data = self._data.get('change_ad_data')
        url, method, header, params, shared, check = cotool.deal_data(data)
        params['noExposure'] = noExposure
        params['noClicks'] = noClicks
        params['cost'] = cost
        params['rebates'] = rebates
        res = httprequest(url, method, header, params)
        cotool.extract_variable(res, shared)
        cotool.assert_res(res, check)
        return res

    @logger()
    def del_ad_data(self, gatherType=1):
        '''
        删除广告数据
        :return:
        '''
        data = self._data.get('del_ad_data')
        url, method, header, params, shared, check = cotool.deal_data(data)
        params['gatherType'] = gatherType
        res = httprequest(url, method, header, params)
        cotool.extract_variable(res, shared)
        cotool.assert_res(res, check)
        return res

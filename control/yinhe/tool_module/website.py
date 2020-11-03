#!/usr/bin/python
# @Time  : 2020/7/14 21:06
# @Author: Fold
# @Desc  : 落地页相关接口

from common.common_tools import cotool
from control.yinhe.ad_module.ad_idea.create_ad_idea import CreateAdIdea
from utils.get_api_data import get_data
from common.config_log import logger



@logger('class')
class Website():

    def __init__(self):
        self._data = get_data.get_yinhe_data('tool_module/websites.yaml')
        self._api_data = get_data.get_yinhe_data('tool_module/landing_page_with_api.yaml')

    @logger()
    def create_website_pay(self, **kwargs):
        '''
        【银河/工具/落地页工具】新建落地页-一键支付
        :return:
        '''
        data = self._data.get('create_website_pay')
        cotool.quick_request(data, **kwargs)

    @logger()
    def create_website_p(self, **kwargs):
        '''
        【银河/工具/落地页工具】新建落地页-一键支付
        :return:
        '''
        data = self._data.get('create_website_pay')
        cotool.quick_rqt(data, **kwargs)

    @logger()
    def create_website_NotneedCaptch(self, **kwargs):
        '''
        【银河/工具/落地页工具】新建落地页-空白落地页不需要验证
        :return:
        '''
        data = self._data.get('create_website_NotneedCaptch')
        cotool.quick_request(data, **kwargs)

    @logger()
    def create_website_no(self, **kwargs):
        '''
        【银河/工具/落地页工具】新建落地页-空白落地页不需要验证
        :return:
        '''
        data = self._data.get('create_website_NotneedCaptch')
        cotool.quick_rqt(data, **kwargs)

    @logger()
    def create_website_NeedCaptch(self, **kwargs):
        '''
        【银河/工具/落地页工具】新建落地页-空白落地页需要验证
        :return:
        '''
        data = self._data.get('create_website_NeedCaptch')
        cotool.quick_request(data, **kwargs)

    @logger()
    def create_website_n(self, **kwargs):
        '''
        【银河/工具/落地页工具】新建落地页-空白落地页需要验证
        :return:
        '''
        data = self._data.get('create_website_NeedCaptch')
        cotool.quick_rqt(data, **kwargs)


    @logger()
    def publish_website(self):
        '''
        发布落地页
        :return:
        '''
        data = self._data.get('publish_website')
        cotool.quick_request(data)

    @logger()
    def publish_web(self):
        '''
        发布落地页
        :return:
        '''
        data = self._data.get('publish_website')
        cotool.quick_rqt(data)

    @logger()
    def association_creativity(self):
        '''
        生成链接
        :return:
        '''
        data = self._data.get('association_creativity')
        cotool.quick_request(data)

    @logger()
    def association_cr(self):
        '''
        生成链接
        :return:
        '''
        data = self._data.get('association_creativity')
        cotool.quick_rqt(data)

    @logger()
    def association_creativity_api(self, **kwargs):
        '''
        生成链接,api 模式
        计划分配： allocInstType=1
        手动分配： allocInstType=2,isTest=0&1
        直线下发： allocInstType=2,isTest=0,receiveDeptId=4572,
                  receiveDeptIdChain='1001-2001-4569-4570-4571-4572',
                  receiveDeptName='rm一院'
        :return:
        '''
        data = self._api_data.get('association_creativity_api')
        cotool.quick_request(data, **kwargs)

    @logger()
    def association_crt_api(self, **kwargs):
        '''
        生成链接,api 模式
        计划分配： allocInstType=1
        手动分配： allocInstType=2,isTest=0&1
        直线下发： allocInstType=2,isTest=0,receiveDeptId=4572,
                  receiveDeptIdChain='1001-2001-4569-4570-4571-4572',
                  receiveDeptName='rm一院'
        :return:
        '''
        data = self._api_data.get('association_creativity_api')
        cotool.quick_rqt(data, **kwargs)


    @logger()
    def landing_page_create(self, payMode, isSmsVerify, **kwargs):
        '''
         新建落地页，发布落地页，生成链接，生成二维码
        :param payMode: 支付方式，0：一键支付；1：仅提交模式
        :param isSmsVerify: 是否需要验证码，0：不需要；1：需要
        :return:
        '''
        if payMode == 0:
            self.create_website_pay(**kwargs)  # 创建落地页
        elif payMode == 1 and isSmsVerify == 1:
            self.create_website_NeedCaptch(**kwargs)
        else:
            self.create_website_NotneedCaptch(**kwargs)
        self.publish_website()  # 发布落地页
        CreateAdIdea().creativity_pageList()
        self.association_creativity()  # 生成链接
        # create_code()  # 生成二维码

    @logger()
    def landing_page_crt(self, payMode, isSmsVerify,  **kwargs):
        '''
         新建落地页，发布落地页，生成链接，生成二维码
        :param payMode: 支付方式，0：一键支付；1：仅提交模式
        :param isSmsVerify: 是否需要验证码，0：不需要；1：需要
        :return:
        '''
        if payMode == 0:
            self.create_website_p(**kwargs)  # 创建落地页
        elif payMode == 1 and isSmsVerify == 1:
            self.create_website_n(**kwargs)
        else:
            self.create_website_no(**kwargs)
        self.publish_web()  # 发布落地页
        self.association_cr()  # 生成链接
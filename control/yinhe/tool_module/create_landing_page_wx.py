#!/usr/bin/python
# @Time    : 2020/7/17 14:36
# @Author  : Jones
# @desc: 创建二维码

from common.http_requests import httprequest
from control.yinhe.ad_module.ad_idea.crt_ad_idea import AddAdIdea
from control.yinhe.flow_module.check_mobile_success import Check
from control.yinhe.tool_module.create_qr_code import CreateQrCode
from control.yinhe.tool_module.landing_page_with_api import LandingPageWithApi
from control.yinhe.tool_module.website import Website
from utils.get_api_data import get_data
from common.common_tools import cotool
from config.constant import GLOBAL_VAR, const


class CrtLadingPage:

    def __init__(self):
        self._data = get_data.get_yinhe_data('tool_module/landing_page_tool.yaml')
        GLOBAL_VAR['projectName'] = const.projectName
        GLOBAL_VAR['ideaName'] = const.ideaName
        GLOBAL_VAR['websiteName'] = const.websiteName
        GLOBAL_VAR['landingPageName'] = const.landingPageName
        self.c = Check()

    def publish_web(self):
        """
        发布落地页
        """
        data = self._data.get('publish_website')
        url, method, header, params, shared, check = cotool.deal_data(data)
        res = httprequest(url, method, header, params)
        cotool.extract_variable(res, shared)
        return res

    def create_qr_code_for_tools(self, **kwargs):
        """
        生成企业微信二维码，发布(工具使用)
        """
        data = self._data.get('create_qr_code_for_tools')
        url, method, header, params, shared, check = cotool.deal_data(data)
        if kwargs:
            params = dict(params, **kwargs)
        res = httprequest(url, method, header, params)
        cotool.extract_variable(res, shared)
        return res

    def create_landing_page_for_api(self, **kwargs):
        """
        创建API落地页
        """
        data = self._data.get('create_landing_page_for_api')
        res = cotool.quick_rqt(data, **kwargs)
        return res

    def add_personal_code_for_tools(self, **kwargs):
        """
        生成个人微信二维码，发布(工具使用)
        """
        data = self._data.get('add_personal_code_for_tools')
        url, method, header, params, shared, check = cotool.deal_data(data)
        if kwargs:
            params = dict(params, **kwargs)
        res = httprequest(url, method, header, params)
        cotool.extract_variable(res, shared)
        return res

    def create_link(self, **kwargs):
        """
        生成链接
        """
        data = self._data.get('create_link')
        cotool.quick_rqt(data, **kwargs)

    def ldy_list_data_query(self):
        """
        落地页数据列表统计查询
        """
        data = self._data.get('query_ldy_data')
        url, method, header, params, shared, check = cotool.deal_data(data)
        res = httprequest(url, method, header, params)
        cotool.extract_variable(res, shared)
        return res

    def create_landingpage_for_wc(self, ideas_id=None, good_id=None):
        '''
        通过参数创建個人微信落地页
        '''
        cad = AddAdIdea()
        cad.get_idea_id_for_tools(adid=ideas_id)
        if good_id == None:
            self.add_personal_code_for_tools()
            self.publish_web()
            self.create_link()
            url = self.ldy_list_data_query()
            return url
        else:
            self.add_personal_code_for_tools(goodsId=good_id)
            self.publish_web()
            self.create_link()
            url = self.ldy_list_data_query()
            return url
        
    def create_landingpage_for_company_wc(self, ideas_id=None, good_id=None):
        '''
        創建企業微信落地頁
        :param good_id: 商品ID
        :param ideas_id: 创意ID
        :return:
        '''
        cad = AddAdIdea()
        cad.get_idea_id_for_tools(adid=ideas_id)
        if good_id == None:
            self.create_qr_code_for_tools()
            self.publish_web()
            self.create_link()
            url = self.ldy_list_data_query()
            return url
        else:
            self.create_qr_code_for_tools(goodsId=good_id)
            self.publish_web()
            self.create_link()
            url = self.ldy_list_data_query()
            return url

    def create_landing_page_for_company_api(self, good_id=None):
        '''
        創建企業微信落地頁
        :param good_id: 商品ID
        :param ideas_id: 创意ID
        :return:
        '''
        lpw = LandingPageWithApi()
        if good_id == None:
            self.create_landing_page_for_api()
            self.publish_web()
            lpw.association_crt()
            self.c.list_landing_pag(websiteType=2)

        else:
            self.create_landing_page_for_api(goodsId=good_id)
            self.publish_web()
            lpw.association_crt()
            self.c.list_landing_pag(websiteType=2)

    def create_landing_page_api(self, api, goods_id=None):
        '''
        api获取广告方式创建落地页
        :param goods_id: 商品id
        :param api: 1:仅提交-不需要验证码-计划， 2:仅提交-需要验证码-计划, 3:仅提交-不需要验证码-手动,
                    4:仅提交-需要验证码-手动, 5:仅提交-不需要验证码-直线, 6:仅提交-需要验证码-直线, 7:一键提交-手动,
                    8:一键提交-直线, 9:企业微信, 10:先支付再企业微信
        :return:
        '''
        wb = Website()
        c = Check()
        lpw = LandingPageWithApi()
        cqc = CreateQrCode()
        if api == 1:
            wb.create_website_no(adCreateType=2, version=2.13)
            wb.publish_web()
            wb.association_crt_api(allocInstType=1)
            c.list_landing_pag()
        elif api == 2:
            wb.create_website_n(adCreateType=2, version=2.13)
            wb.publish_web()
            wb.association_crt_api(allocInstType=1)
            c.list_landing_pag()
        elif api == 3:
            wb.create_website_no(adCreateType=2, version=2.13)
            wb.publish_web()
            wb.association_crt_api(allocInstType=2, isTest=0)
            c.list_landing_pag()
        elif api == 4:
            wb.create_website_n(adCreateType=2, version=2.13)
            wb.publish_web()
            wb.association_crt_api(allocInstType=1)
            c.list_landing_pag()
        elif api == 5:
            wb.create_website_no(adCreateType=2, version=2.13)
            wb.publish_web()
            wb.association_crt_api(allocInstType=2, isTest=0, receiveDeptId=4572,
                                          receiveDeptIdChain='1001-2001-4569-4570-4571-4572',
                                          receiveDeptName='rm一院')
            c.list_landing_pag()
        elif api == 6:
            wb.create_website_n(adCreateType=2, version=2.13)
            wb.publish_web()
            wb.association_crt_api(allocInstType=2, isTest=0, receiveDeptId=4572,
                                          receiveDeptIdChain='1001-2001-4569-4570-4571-4572',
                                          receiveDeptName='rm一院')
            c.list_landing_pag()
        elif api == 7:
            lpw.save_pag(type=3, goodsId=goods_id)
            cqc.publish_web()
            lpw.association_crt(type=2)
            c.list_landing_pag_api()
        elif api == 8:
            lpw.save_pag(type=3, goodsId=goods_id)
            cqc.publish_web()
            lpw.association_crt(type=3)
            c.list_landing_pag_api()



# cqc = CrtLadingPage()
# cqc.create_landingpage_for_company_wc(ideas_id='113997')
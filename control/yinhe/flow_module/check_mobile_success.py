#!/usr/bin/python
# @Time  : 2020/7/16 10:12
# @Author: Fold
# @Desc  :手机模式校验字段和流程校验是否成功

from common.common_tools import cotool
from common.config_db import db
from common.config_log import logger
from config.constant import GLOBAL_VAR
from utils.get_api_data import get_data


@logger('class')
class Check():

    def __init__(self):
        self._data = get_data.get_yinhe_data('tool_module/website_link_check.yaml')
        self._data1 = get_data.get_yinhe_data('flow_module/put_record_query/customer_leaning_repeat.yaml')
        self._data2 = get_data.get_base_data('login_account.yaml')
        self._data3 = get_data.get_yinhe_data('classroom_check.yaml')
        self._data4 = get_data.get_yinhe_data('tool_module/landing_page_order.yaml')

    @logger()
    def list_landing_page(self, **kwargs):
        '''
        【银河/工具/落地页工具】落地页数据查询
        :return:
        '''
        data = self._data.get('list_landing_pag')
        cotool.quick_request(data, **kwargs)

    @logger()
    def list_landing_pag(self, **kwargs):
        '''
        【银河/工具/落地页工具】落地页数据查询
        :return:
        '''
        data = self._data.get('list_landing_pag')
        cotool.quick_rqt(data, **kwargs)

    def list_landing_page_api(self, **kwargs):
        '''
        【银河/工具/落地页工具】落地页数据查询
        :return:
        '''
        data = self._data.get('list_landing_pag_api')
        cotool.quick_request(data, **kwargs)

    @logger()
    def list_landing_page_NoonedCapath(self):
        '''
        【银河/工具/落地页工具】落地页数据查询--无支付
        :return:
        '''
        data = self._data.get('list_landing_page_NoonedCapath')
        cotool.quick_request(data)

    @logger()
    def website_stat_queryStatInfo(self):
        '''
        【银河/工具/落地页工具/查询落地页数据】查看数据
        :return:
        '''
        data = self._data.get('website_stat_queryStatInfo')
        cotool.quick_request(data)

    @logger()
    def website_queryStatInfo_NoonedCapath(self):
        '''
        【银河/工具/落地页工具/查询落地页数据】查看数据--无支付
        :return:
        '''
        data = self._data.get('website_queryStatInfo_NoonedCapath')
        cotool.quick_request(data)

    @logger()
    def classroom_login(self):
        '''
        【潭州课堂】获取登录学员 token
        :return:
        '''
        data = self._data2.get('classroom_login')
        cotool.quick_request(data)

    @logger()
    def api_course_queryByStudent(self):
        '''
        【潭州课堂/我的课表】查看我的课表
        :return:
        '''
        data = self._data3.get('api_course_queryByStudent')
        cotool.quick_request(data)


    @logger()
    def order_manager_list(self):
        '''
        查看订单管理中单据状态是否为自动提单
        :return:
        '''
        data = self._data4.get('order_manager_list')
        cotool.quick_request(data)

    @logger()
    def customer_LeaningRepeat_list(self, **kwargs):
        '''
        【银河/流量/入库记录查询】查询,校验是否已经入库
        :return:
        '''
        data = self._data1.get('customer_LeaningRepeat_list')
        cotool.quick_request(data, **kwargs)


    @logger()
    def check_sql(self):
        '''
        查询数据库，返回分配状态、不可分配原因
        :return:查询结果

        '''
        id = GLOBAL_VAR['repeatId']
        website_id = GLOBAL_VAR['websiteLinkId']
        sql = "select alloc_status,un_alloc_reason,gather_time,repeat_times,pay_amount,remarks,enter_way from crm_customer.t_customer_leaning_repeat where id = %s and website_id = %s;"
        params = [id, website_id]
        result = db.execute_sql(sql, params)
        rs = {}
        rs['alloc_status'] = result[0][0]
        rs['un_alloc_reason'] = result[0][1]
        rs['gather_time'] = result[0][2].strftime('%Y-%m-%d %H:%M:%S')
        rs['repeat_times'] = result[0][3]
        rs['pay_amount'] = float(result[0][4])
        rs['remarks'] = result[0][5]
        rs['enter_way'] = result[0][6]

        return rs

    @logger()
    def landing_page_query(self, pay_mode):
        '''
        根据支付方式选择落地页查询，并校验相关字段
        :param pay_mode:支付方式 0：一键支付；1：仅提单
        :return:
        '''
        if pay_mode == 0:
            self.list_landing_page()  # 落地页数据查询
            self.website_stat_queryStatInfo()  # 查询落地页数据-查看数据
        else:
            self.list_landing_page_NoonedCapath()  # 落地页数据查询
            self.website_queryStatInfo_NoonedCapath()  # 查询落地页数据-查看数据

    @logger()
    def classroom_query(self):
        '''
        登录潭州课堂查看我的课表中是否存在该数据，目前因为没有万能验证码，故无太大作用
        :return:
        '''
        self.classroom_login()  # 获取登录学员 token
        self.api_course_queryByStudent()  # 查看我的课表

    @logger()
    def customer_LeaningRepeat_query(self, **kwargs):
        '''
        入库记录查询页面查询数据，并校验相关字段，查询数据库查找对应的数据查看分配状态、不可分配原因
        :return: 返回分配状态、不可分配原因
        '''
        self.customer_LeaningRepeat_list(**kwargs)  # 查询,校验是否已经入库
        result = self.check_sql()  # 查询数据库，返回分配状态、不可分配原因
        return result

    @logger()
    def check_one_submit(self, pay_mode):
        '''
        通过支付模式，来确定使用哪种方式校验
        :param pay_mode: 支付方式 0：一键支付；1：仅提单
        :return:
        '''
        if pay_mode ==0:
            self.landing_page_query(pay_mode)
            self.classroom_query()
        else:
            self.landing_page_query(pay_mode)
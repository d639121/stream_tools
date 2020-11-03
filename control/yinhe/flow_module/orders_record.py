#!/usr/bin/python 
# @Time  : 2020/10/21 15:26
# @Author: Fold
# @Desc  : 成单整体流程
import time

from config.constant import GLOBAL_VAR, const
from control.CRM.worksheet_mgt.add_worksheet import WorkSheet
from control.base.login import Login
from control.base.register_code import RegisterCode
from control.yinhe.ad_module.ad_idea.add_consumer_single import ConsumerSingle
from control.yinhe.ad_module.ad_idea.import_flow_single import ImportFlow
from control.yinhe.flow_module.import_flow_query import ImportFlowQuery
from control.yinhe.flow_module.order_record_query import OrderRecord


class OrdersRecord:
    def __init__(self):
        self.consumer = ConsumerSingle()
        GLOBAL_VAR['projectName'] = const.projectName
        GLOBAL_VAR['ideaName'] = const.ideaName
        GLOBAL_VAR['gatherTimeStart'] = const.gatherTimeStart
        self._time = str(GLOBAL_VAR['todayTime'])
        self._qq = GLOBAL_VAR['qq']
        self._phone = const.phoneNumber
        GLOBAL_VAR['phoneNumber'] = self._phone
        self._ifq = ImportFlowQuery()
        self._if = ImportFlow()
        self.rtc = RegisterCode()
        self.ac = Login()
        self.ws = WorkSheet()
        self._or = OrderRecord()
        self.ac.login_action('t0383212689', '123456')

    def test_order_record(self):
        self.consumer.add_ad_plan()
        self.consumer.program_pageList()
        self.consumer.creativity_save()
        self.consumer.creativity_pageList()
        ad_num = GLOBAL_VAR['creativityNo']
        excel = {
            "1": ["客户昵称（姓名）", "手机号码（必填）", "QQ号码", "微信", "参考年龄", "流量来源时间（必填,三天内数据）", "地域（市级，非必填）", "流量备注"],
            "2": ["张三", self._phone, self._qq, self._qq, 28, self._time, "长沙市", "流量备注"]
        }
        self._if.import_mobile_single(excel, adNo=ad_num)
        self.rtc.register_code_phone(self._phone)
        self.ac.verification_code_login()
        self.ac.get_personal_information()
        time.sleep(300)
        self.ws.add_worksheet()
        self.ws.qry_worksheet()
        self.ws.chk_worksheet()
        time.sleep(300)
        self._or.qry_order_record()

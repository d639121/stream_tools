#!/usr/bin/python 
# @Time  : 2020/9/3 17:10
# @Author: Fold
# @Desc  : 流量预算管理

import datetime

from common.common_tools import cotool
from common.config_log import logger
from common.http_requests import httprequest
from control.base.login import login
from utils.get_api_data import get_data


class FlowBudgetMgt:

    def __init__(self):
        self._data = get_data.get_haichuan_data('budget_mgt/flow_budget.yaml')
        self.next_month = str(datetime.date(datetime.date.today().year, datetime.date.today().month + 2, 1))
        i = datetime.datetime.now().day
        subject_list = [
            {"id": "506", "name": "Photoshop", "cn": "261-505-506"},
            {"id": "507", "name": "Indesign", "cn": "261-505-507"}, {"id": "508", "name": "Axure", "cn": "261-505-508"},
            {"id": "509", "name": "CDR", "cn": "261-505-509"},
            {"id": "510", "name": "Illustrator", "cn": "261-505-510"},
            {"id": "511", "name": "Dreamweaver", "cn": "261-505-511"},
            {"id": "512", "name": "CAD", "cn": "261-505-512"}, {"id": "513", "name": "UG", "cn": "261-505-513"},
            {"id": "514", "name": "Solidworks", "cn": "261-505-514"},
            {"id": "515", "name": "Sketchup", "cn": "261-505-515"},
            {"id": "516", "name": "Rhino3D", "cn": "261-505-516"},
            {"id": "517", "name": "Pro/E", "cn": "261-505-517"}, {"id": "518", "name": "Zbrush", "cn": "261-505-518"},
            {"id": "519", "name": "Cinema 4D", "cn": "261-505-519"}, {"id": "520", "name": "SAI", "cn": "261-505-520"},
            {"id": "521", "name": "Flash", "cn": "261-505-521"}, {"id": "522", "name": "3DMAX", "cn": "261-505-522"},
            {"id": "523", "name": "MAYA", "cn": "261-505-523"}, {"id": "524", "name": "VRay", "cn": "261-505-524"},
            {"id": "525", "name": "AE", "cn": "261-505-525"}, {"id": "526", "name": "Premiere", "cn": "261-505-526"},
            {"id": "527", "name": "Fireworks", "cn": "261-505-527"},
            {"id": "528", "name": "其它软件", "cn": "261-505-528"}, {"id": "529", "name": "NX", "cn": "261-505-529"},
            {"id": "530", "name": "SW", "cn": "261-505-530"}, {"id": "531", "name": "PLC", "cn": "261-505-531"},
            {"id": "532", "name": "inventor", "cn": "261-505-532"},
            {"id": "921", "name": "pycharm", "cn": "261-505-921"},
            {"id": "922", "name": "IDEL", "cn": "261-505-922"}, {"id": "923", "name": "NOTE++", "cn": "261-505-923"},
            {"id": "924", "name": "SQL", "cn": "261-505-924"}, {"id": "925", "name": "DEMO", "cn": "261-505-925"}
        ]
        self._id = subject_list[i - 1]['id']
        self._name = subject_list[i - 1]['name']
        self._chain = subject_list[i - 1]['cn']

    @logger()
    def add_flow_budget(self, gather=None, mode=None):
        """
        :param gather: 获客方式
        :param mode: 投放模式
        :return:
        """
        data = self._data.get('add_flow_budget')
        url, method, header, params, shared, check = cotool.deal_data(data)
        params['costMonth'] = self.next_month
        params['subjectId'] = self._id
        params['subjectName'] = self._name
        params['subjectIdChain'] = self._chain
        if gather is not None:
            params['gatherType'] = gather
        if mode is not None:
            params['putMode'] = mode
        res = httprequest(url, method, header, params)
        cotool.extract_variable(res, shared)
        cotool.assert_res(res, check)

    @logger()
    def qry_flow_budget(self, **kwargs):
        """
        :param kwargs:
        :return:
        """
        data = self._data.get('qry_flow_budget')
        cotool.quick_request(data, **kwargs)


    @logger()
    def chk_flow_budget(self, **kwargs):
        """
        :param kwargs:
        :return:
        """
        data = self._data.get('chk_flow_budget')
        cotool.quick_request(data, **kwargs)

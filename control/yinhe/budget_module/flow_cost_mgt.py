#!/usr/bin/python 
# @Time  : 2020/8/5 11:30
# @Author: LOUIE
# @Desc  : 流量成本管理

from common.common_tools import cotool
from common.config_log import logger
from common.http_requests import httprequest
from control.base.login import login
from utils.get_api_data import get_data
from utils.operation_excel import oe


class FlowCostMgt:

    def __init__(self):
        self._data = get_data.get_yinhe_data('budget_module/flow_cost_mgt.yaml')

    @logger()
    def flow_cost_mgt_page_list(self, **kwargs):
        """
        :param startCostMonth/endCostMonth: 成本月份开始时间/结束时间，成对出现 时间戳格式：
        :param promotionerDeptIdChain: 推广组织，组织链
        :param subjectId: 科目Id
        :param channelId: 渠道id
        :param putMode: 投放模式 1.普通  2.接待  3.高转VIP  4.APP  5.小咖
        :param gatherType: 获客方式 1.手机流量 2.QQ流量 3.微信流量
        :param creatorName: 创建人
        :param startCreateTime/endCreateTime: 创建时间，成对出现  时间格式：1596211200000
        :param kwargs:
        :return:
        """
        data = self._data.get('flow_cost_mgt_pageList')
        res = cotool.quick_request(data, **kwargs)
        return res

    @logger()
    def flow_cost_mgt_save(self, **kwargs):
        """
        :param kwargs:
        :return:
        """
        data = self._data.get('flow_cost_mgt_save')
        cotool.quick_request(data, **kwargs)

    @logger()
    def flow_cost_mgt_update(self, **kwargs):
        """
        :param kwargs:
        :return:
        """
        data = self._data.get('flow_cost_mgt_update')
        cotool.quick_request(data, **kwargs)

    @logger()
    def del_flow_cost_mgt(self, **kwargs):
        """
        :param kwargs:
        :return:
        """
        data = self._data.get('del_flow_cost_mgt')
        cotool.quick_request(data, **kwargs)

    @logger()
    def flow_cost_mgt_import_others(self, file_name, status, msg):
        """
        :param file_name: 文件名
        :param status: 响应状态码
        :param msg: 返回信息
        :return:
        """
        data = self._data.get('flow_cost_mgt_import')
        url, method, header, params, shared, check = cotool.deal_data(data)
        file_data, content_type, file_path = oe.send_others_file(file_name, params)
        header['content-type'] = content_type
        check['status'] = status
        check['msg'] = msg
        res = httprequest(url, method, header, file_data)
        cotool.extract_variable(res, shared)
        cotool.assert_res(res, check)

    @logger()
    def flow_cost_mgt_import(self, excel):
        """
        :param excel: excel文件头组成的list
        :return:
        """
        data = self._data.get('flow_cost_mgt_import')
        url, method, header, params, shared, check = cotool.deal_data(data)
        file_data, content_type, file_path = oe.send_file(excel, params)
        header['content-type'] = content_type
        res = httprequest(url, method, header, file_data)
        cotool.extract_variable(res, shared)
        cotool.assert_res(res, check)
        oe.delete(file_path)

    @logger()
    def flow_cost_mgt_export(self, **kwargs):
        """
        :param kwargs:
        :return:
        """
        data = self._data.get('flow_cost_mgt_export')
        cotool.quick_request(data, **kwargs)


fcm = FlowCostMgt()

if __name__ == '__main__':
    res = fcm.flow_cost_mgt_page_list(gatherType=3, startCostMonth=1601481600000, endCostMonth=1604159999999, channelId=4)
    rs = res['data']['list']
    id_list = []
    if len(rs):
        for i in range(len(rs)):
            id = rs[i]['id']
            print(id)
            id_list.append(id)
    ids = ','.join(str(i) for i in id_list)

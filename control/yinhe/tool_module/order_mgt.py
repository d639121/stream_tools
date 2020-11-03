#!/usr/bin/python
# @Time  : 2020/8/10 20:28
# @Author: Fold
# @Desc  : 订单管理查询

from common.common_tools import cotool
from common.config_log import logger
from utils.get_api_data import get_data


class OrderMgt:

    def __init__(self):
        self._data = get_data.get_yinhe_data('tool_module/order_mgt.yaml')

    @logger()
    def orders_manage(self, **kwargs):
        '''
        邀课引流管理查询
        :param payTimeStart/payTimeEnd: 支付时间，成对存在  格式为："2020-08-09T16:00:00.000Z" - "2020-08-10T15:59:59.000Z"
        :param payNo: 交易单号
        :param isCreateWorksheet: 提单状态  1.已提单 0.未提单
        :param courseSource: 商品来源  0.自建课程 1.教务系统  2.小咖课程
        :param nickName: 推广人
        :param goodsName: 商品名称
        :param pageNo: 页码，第几页 默认第一页，可修改
        :param pageSize: 每页数据 默认20条，可修改
        :param tabType: 1. 新流量 2.老流量 此处为默认参数，可修改
        :param kwargs: 上述参数通过kwargs进行传递
        :return:
        '''

        data = self._data.get('orders_page_list')
        cotool.quick_request(data, **kwargs)
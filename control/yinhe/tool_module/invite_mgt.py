#!/usr/bin/python
# @Time  : 2020/8/1 14:09
# @Author: Fold
# @Desc  : 邀课引流管理

from common.config_log import logger
from utils.get_api_data import get_data
from common.common_tools import cotool


class InvitationMgt:

    def __init__(self):
        self._data = get_data.get_yinhe_data('tool_module/invitation_mgt.yaml')

    def generate_link(self):
        """
        生成邀课连接
        """
        data = self._data['generate_link']
        cotool.quick_request(data)

    @logger()
    def diversion_list(self, **kwargs):
        '''
        邀课引流管理查询
        :param courseId: 课程id
        :param inviteName: 邀课人
        :param createStartTime | createEndTime: 成对存在，为起始和截止时间戳
        :param linkType: 学员听课平台 1.H5(手机版网页) 2.微信小程序 3.H5(手机版网页) 不存在或为null为全部
        :param status: 状态 0.已失效 1.正常 不存在或为null为全部
        :param inviteLessonDeptIdChain: 邀课部门，为邀课部门的组织id
        :param receiveDeptIdChain: 接受售前院，为售前院的组织id
        :param pageIndex: 页码，第几页 默认第一页，可修改
        :param pageSize: 每页数据 默认20条，可修改
        :param tabType: 1. 新流量 2.老流量 此处为默认参数，可修改
        :param kwargs: 上述参数通过kwargs进行传递
        :return:
        '''

        data = self._data.get('diversion_list')
        cotool.quick_request(data, **kwargs)


#!/usr/bin/python 
# @Time  : 2020/8/5 11:36
# @Author: LOUIE
# @Desc  : 邀课引流统计

from common.common_tools import cotool
from common.config_log import logger
from utils.get_api_data import get_data


class InvitationStatistics:

    def __init__(self):
        self._data = get_data.get_yinhe_data('tool_module/invitation_statistics.yaml')

    @logger()
    def free_statistics(self, **kwargs):
        '''
                邀课引流统计查询
                :param roleId: 角色组：8.免费流量组 13.免费流量兼职组 不存在或为null为全部
                :param inviteStartTime | inviteEndTime: 成对存在，为起始和截止时间戳, 默认当天时间的00:00:00~23:59:59
                :param roleType: 角色类型 1.负责人 2.小伙伴  99.机构管理员 11.超级兼职 12.高级兼职 13.普通兼职 不存在或为null为全部
                :param inviterName: 邀课人
                :param inviteDeptChain: 邀课部门，为邀课部门的组织id
                :param pageIndex: 页码，第几页 默认第一页，可修改
                :param pageSize: 每页数据 默认20条，可修改
                :param kwargs: 上述参数通过kwargs进行传递
                :return:
                '''

        data = self._data.get('free_statistics')
        cotool.quick_request(data, **kwargs)
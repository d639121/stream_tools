#!/usr/bin/python
# @Time  : 2020/8/7 17:08
# @Author: Fold
# @Desc  : 落地页数据

from common.common_tools import cotool
from common.config_log import logger
from utils.get_api_data import get_data


class WebsiteLinkData:

    def __init__(self):
        self._data = get_data.get_yinhe_data('tool_module/website_link_data.yaml')

    @logger()
    def list_creativity(self, **kwargs):
        '''
                银河/工具/兼职工具】查询
                :param websiteCode: 落地页链接 websiteCode/websiteName/websiteId 这三个参数只能同时存在一个
                :param websiteName: 对内分享名称
                :param websiteLinkId: 落地页链接id
                :param creativityCode: 创意编码
                :param isTest: 是否测试 0.否 1.是
                :param channelCode: 投放渠道 0.其他 1.广点通 2.哔哩哔哩 3.微信公众号 4.微博 5.百度 6.头条抖音 7.UC 8.快手
                9.喜马拉雅 10.爱奇艺 null或者不存在时为全部
                :param subjectId: 意向科目id
                :param putMode: 投放模式 "1".普通 "3".高转VIP
                :param submitStartTime/submitEndTime: 来源时间，默认当天 成对存在 2020-08-07 23:59:59
                :param startTime/endTime: 发布时间 成对存在 2020-08-07 23:59:59
                :param websiteType: 落地页类型 1.表单落地页 2.微信落地页 3.活动落地页
                :param pageNo: 页码，第几页 默认第一页，可修改
                :param pageSize: 每页数据 默认10条，可修改
                :param kwargs: 上述参数通过kwargs进行传递
                :return:
                '''

        data = self._data.get('list_creativity')
        cotool.quick_request(data, **kwargs)
#!/usr/bin/python 
# -*- coding: utf-8 -*-
# @Time   : 2020/4/21 10:16
# @Author : LOUIE
# @Desc   : 变量配置文件

import datetime
import random
from utils import generator
from config.read_config import rc
from datetime import date, timedelta
import time


class Const:
    pre_data = {}
    referPrice = "1000"
    floorPrice = "800"
    discountsPrice = "888"
    userName = 'LOUIE'
    today = date.today()
    yesterday = today - timedelta(days=1)
    tomorrow = today + timedelta(days=1)
    theDayAfterTomorrow = today + timedelta(days=2)   # 后天
    # 昨天时间戳
    yesterdayStartTimestamp = str((int(time.mktime(time.strptime(str(yesterday), '%Y-%m-%d')))) * 1000)
    yesterdayEndTimestamp = str((int(time.mktime(time.strptime(str(today), '%Y-%m-%d'))) - 1) * 1000)
    # 今天时间戳
    todayStartTimestamp = str((int(time.mktime(time.strptime(str(today), '%Y-%m-%d')))) * 1000)
    todayEndTimestamp = str((int(time.mktime(time.strptime(str(tomorrow), '%Y-%m-%d'))) - 1) * 1000)
    gatherTimeStart = str((int(time.mktime(time.strptime(str(today), '%Y-%m-%d')))) * 1000)
    gatherTimeEnd = str((int(time.mktime(time.strptime(str(tomorrow), '%Y-%m-%d'))) - 1) * 1000)
    # 明天时间戳
    tomorrowStartTimestamp = str(int(time.mktime(time.strptime(str(tomorrow), '%Y-%m-%d'))) * 1000)
    tomorrowEndTimestamp = str((int(time.mktime(time.strptime(str(theDayAfterTomorrow), '%Y-%m-%d'))) - 1) * 1000)
    # 今天开始时间(格式化时间)
    todayStartTime = str(time.strftime("%Y-%m-%d 00:00:00", time.localtime()))
    todayEndTime = str(time.strftime("%Y-%m-%d 23:59:59", time.localtime()))

    @property
    def timestamp(self):
        '''
        当前时间戳
        :return: 1595230844000
        '''
        return str(generator.timestamp())

    @property
    def setTime(self):
        '''
        特殊时间格式
        :return: 2020-07-20T15:38:07Z
        '''
        return str(time.strftime("%Y-%m-%dT%H:%M:%SZ", time.localtime(time.time())))

    @property
    def todyTime(self):

        return str(time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(time.time())))

    @property
    def title(self):
        '''
        标题
        :return: 自动化测试95277114
        '''
        return str("自动化测试{}".format(generator.random_ean8()))

    @property
    def landingPageName(self):
        '''
        落地页
        :return: 落地页95277114
        '''
        return str("落地页-{}".format(generator.random_ean8()))

    @property
    def transNo(self):
        '''
        交易单号
        :return: 1595230844000
        '''
        return self.timestamp

    @property
    def projectName(self):
        '''
        计划名称
        :return: 自动化计划95277114
        '''
        return str("自动化计划{}".format(generator.random_ean8()))

    @property
    def phoneNumber(self):
        '''
        手机号
        :return: 13347335633
        '''
        return str(generator.random_phone_number())

    @property
    def qq(self):
        '''
        qq号
        :return: 95277114
        '''
        return str(generator.random_ean8())

    @property
    def courseName(self):
        '''
        课程名称
        :return: 自动化课程95277114
        '''
        return str("自动化课程{}".format(generator.random_ean8()))

    @property
    def classTypeName(self):
        '''
        小咖班型名称
        :return: 自动化班型95277114
        '''
        return str("自动化班型{}".format(generator.random_ean8()))

    @property
    def ideaName(self):
        '''
        银河创意名称
        :return: 自动化创意95277114
        '''
        return str("自动化创意{}".format(generator.random_ean8()))

    @property
    def goodsName(self):
        '''
        小咖商品名称
        :return: 自动化商品95277114
        '''
        return str("自动化商品{}".format(generator.random_ean8()))

    @property
    def channelName(self):
        '''
        银河渠道名称
        :return: 自动化渠道95277114
        '''
        return str("自动化渠道{}".format(generator.random_ean8()))

    @property
    def websiteName(self):
        '''
        银河落地页名称
        :return: 自动化落地页95277114
        '''
        return str("自动化落地页{}".format(generator.random_ean8()))

    @property
    def partner(self):
        '''
        小伙伴 token
        :return:
        '''
        return rc.get_token("partner")

    @property
    def leader(self):
        '''
        负责人 token
        :return:
        '''
        return rc.get_token("leader")

    @property
    def random_year_month_str(self):
        """
        生成年月组合  2020-01
        :return:
        """
        a1 = (1976, 1, 1, 0, 0, 0, 0, 0, 0)
        a2 = (2020, 12, 31, 23, 59, 59, 0, 0, 0)
        start = time.mktime(a1)
        end = time.mktime(a2)
        t = random.randint(start, end)
        date_tuple = time.localtime(t)
        date = time.strftime("%Y-%m", date_tuple)
        return date

    @property
    def month_ago_time(self):
        """
        前一个月的第一天
        :return:
        """
        return str(int(time.mktime(datetime.date(datetime.date.today().year, datetime.date.today().month - 1, 1).timetuple())) * 1000)

    @property
    def two_month_next_time(self):
        """
        后两个月的第一天
        :return:
        """
        year = datetime.date.today().year
        if datetime.date.today().month > 10:
            year = year + 1
            month = datetime.date.today().month - 10
        else:
            month = datetime.date.today().month + 2
        day = datetime.datetime.now().day
        return str(int(time.mktime(time.strptime('{}-{}-{} 00:00:00'.format(year, month, day), '%Y-%m-%d %H:%M:%S'))) * 1000)

    @property
    def this_month_first(self):
        year = datetime.date.today().year
        month = datetime.date.today().month
        return str(int(time.mktime(time.strptime('{}-{}-01 00:00:00'.format(year, month), '%Y-%m-%d %H:%M:%S'))) * 1000)

    @property
    def next_month_first(self):
        year = datetime.date.today().year
        month = datetime.date.today().month
        if month > 10:
            year = year + 1
            month = month - 10
        else:
            month = month+2
        return str(int(time.mktime(time.strptime('{}-{}-01 00:00:00'.format(year, month), '%Y-%m-%d %H:%M:%S'))) * 1000)

    @property
    def next_month_last(self):
        year = datetime.date.today().year
        month = datetime.date.today().month
        if month > 11:
            year = year + 1
            month = month - 11
        else:
            month = month+1
        day = datetime.datetime.now().day
        return str(int(time.mktime(time.strptime('{}-{}-{} 00:00:00'.format(year, month, day),
                                                 '%Y-%m-%d %H:%M:%S'))) * 1000 - 1)

    @property
    def next_two_month_last(self):
        year = datetime.date.today().year
        month = datetime.date.today().month
        if month > 10:
            year = year + 1
            month = month - 10
        else:
            month = month+2
        day = datetime.datetime.now().day
        return str(int(time.mktime(time.strptime('{}-{}-{} 00:00:00'.format(year, month, day),
                                                 '%Y-%m-%d %H:%M:%S'))) * 1000 - 1)

    @property
    def random_chinese(self):
        '''
        随机几个中文
        :return:
        '''
        return generator.random_name()

const = Const()


GLOBAL_VAR = {

    "referPrice": "1000",
    "floorPrice": "800",
    "discountsPrice": "888",
    "userName": 'LOUIE',
    "qq": const.qq,
    "title": const.title,
    "transNo": const.transNo,
    "setTime": const.setTime,
    "leader": const.leader,
    "partner": const.partner,
    "phoneNumber": const.phoneNumber,
    "ideaName": const.ideaName,
    "goodsName": const.goodsName,
    "courseName": const.courseName,
    "channelName": const.channelName,
    "projectName": const.projectName,
    "websiteName": const.websiteName,
    "classTypeName": const.classTypeName,
    "landingPageName": const.landingPageName,
    "timestamp": const.timestamp,
    "yesterday": const.yesterday,
    "tomorrow": const.tomorrow,
    "theDayAfterTomorrow": const.theDayAfterTomorrow,
    "payTimeStart": const.yesterday,
    "todayStartTime": const.todayStartTime,      # 2020-06-10 00:00:00
    "todayEndTime": const.todayEndTime,          # 2020-06-10 23:59:59
    "todayTime": const.todyTime,                 # 2020/06/10 16:25:36
    "gatherTimeStart": const.todayStartTimestamp,    # 1591113600000
    "gatherTimeEnd": const.todayEndTimestamp,        # 1591718399999
    "yesterdayStartTimestamp": const.yesterdayStartTimestamp,
    "yesterdayEndTimestamp": const.yesterdayEndTimestamp,
    "todayStartTimestamp": const.todayStartTimestamp,
    "todayEndTimestamp": const.todayEndTimestamp,
    "tomorrowStartTimestamp": const.tomorrowStartTimestamp,
    "tomorrowEndTimestamp": const.tomorrowEndTimestamp,
    "monthAgoTimeStart": const.month_ago_time,   # 上一个月第一天的开始时间
    "twoMonthAgoTimeStart": const.two_month_next_time,  # 上两个月第一天
    "yearAndMonth": const.random_year_month_str,  # 随机年月组合 1980-08
    "thisMonthFirst": const.this_month_first,     # 本月第一天的时间戳 毫秒
    "nextMonthFirst": const.next_month_first,     # 下月第一天的时间戳 毫秒
    "nextMonthLast": const.next_month_last,  # 下月最后一天的时间戳 毫秒
    "newTwoMonth": const.next_two_month_last,  # 下两月最后一天
    "RandomChinese": const.random_chinese,  # 随机中文
}

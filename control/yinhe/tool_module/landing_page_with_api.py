#!/usr/bin/python 
# @Time  : 2020/8/10 21:03
# @Author: LOUIE
# @Desc  : 新建落地页-API模式

from utils.get_api_data import get_data
from common.common_tools import cotool
from control.yinhe.tool_module.create_qr_code import CreateQrCode


class LandingPageWithApi:

    def __init__(self):
        self._data = get_data.get_yinhe_data('tool_module/landing_page_with_api.yaml')
        self.cqc = CreateQrCode()

    def save_page(self, type=1, **kwargs):
        """
        保存落地页
        :param type: 1.企业微信模式 2.企业微信模式-不带商品+ 3.一键提交模式
        """
        if int(type) < 4:
            mode = 'save_page{}'.format(str(type))
            data = self._data[mode]
            cotool.quick_request(data, **kwargs)

    def save_pag(self, type=1, **kwargs):
        """
        保存落地页
        :param type: 1.企业微信模式 2.企业微信模式-不带商品+ 3.一键提交模式
        """
        if int(type) < 4:
            mode = 'save_page{}'.format(str(type))
            data = self._data[mode]
            cotool.quick_rqt(data, **kwargs)

    def association_creativity(self, type=1):
        """
        创建链接
        :param type: 1.微信活码模式-直线下发 2.手动分配 3.直线下发
        """
        FollowReq = {

            "gatherType": 3,
            "isTest": 0,
            "receiveDeptIdChain": "",
            "receiveDeptName": ""
        }
        if type == 1:
            dic1 = {"allocInstType": 3, "gatherType": 3, "putMode": 1}
        elif type == 2:
            dic1 = {"allocInstType": 2, "gatherType": 1, "putMode": 3}
        elif type == 3:
            dic1 = {"allocInstType": 3, "gatherType": 1, "putMode": 3, 'receiveDeptId': 14,
                    'receiveDeptIdChain': "1001-2001-3007-14", 'receiveDeptName': "wy测试部门"}
        FollowReq = dict(FollowReq, **dic1)
        accountId = 'wx359bdedd5d18907a'
        self.cqc.create_link(releaseChannel=3, subjectId=280, websiteLinkFollowReq=FollowReq, accountId=accountId, channelId=6, subject='PHP')

    def association_crt(self, type=1):
        """
        创建链接
        :param type: 1.微信活码模式-直线下发 2.手动分配 3.直线下发
        """
        FollowReq = {

            "gatherType": 3,
            "isTest": 0,
            "receiveDeptIdChain": "",
            "receiveDeptName": ""
        }
        if type == 1:
            dic1 = {"allocInstType": 3, "gatherType": 3, "putMode": 1}
        elif type == 2:
            dic1 = {"allocInstType": 2, "gatherType": 1, "putMode": 3}
        elif type == 3:
            dic1 = {"allocInstType": 3, "gatherType": 1, "putMode": 3, 'receiveDeptId': 14,
                    'receiveDeptIdChain': "1001-2001-3007-14", 'receiveDeptName': "wy测试部门"}
        FollowReq = dict(FollowReq, **dic1)
        accountId = 'wx359bdedd5d18907a'
        self.cqc.crt_link(releaseChannel=3, subjectId=280, websiteLinkFollowReq=FollowReq, accountId=accountId,
                             channelId=6, subject='PHP')


if __name__ == '__main__':
    lpwa = LandingPageWithApi()
    lpwa.save_page()
    CreateQrCode().publish_website()
    lpwa.association_creativity(2)

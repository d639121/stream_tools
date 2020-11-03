#!/usr/bin/python 
# @Time  : 2020/8/18 17:31
# @Author: Fold
# @Desc  : 新增流量成本管理

import datetime
import allure
from common.config_log import logger
from stream_tools.config.constant import GLOBAL_VAR
from stream_tools.config.read_config import rc
from control.base.login import login
from control.yinhe.budget_module.flow_cost_mgt import FlowCostMgt


class TestFlowCostMgtAdd:

    def setup_class(self):
        if rc.get_env() == 'pre':
            login.login_action('t0322511032', '123456')
        else:
            login.login_action('t0384223793', '123456')
        i = datetime.datetime.now().day
        self._cm = GLOBAL_VAR['thisMonthFirst']
        self.new_time = GLOBAL_VAR['twoMonthAgoTimeStart']
        self.next_end = GLOBAL_VAR['newTwoMonth']
        subject_list = [
            {"id": "269", "name": "产品策划"}, {"id": "270", "name": "游戏策划"}, {"id": "271", "name": "产品运营"},
            {"id": "373", "name": "SEM"}, {"id": "375", "name": "Android开发"}, {"id": "376", "name": "IOS"},
            {"id": "272", "name": "游戏运营"}, {"id": "273", "name": "品牌营销"}, {"id": "274", "name": "电商运营"},
            {"id": "275", "name": "新媒体运营"}, {"id": "276", "name": "SEO"},  {"id": "283", "name": "HTML5"},
            {"id": "284", "name": "JavaScript"}, {"id": "285", "name": "jQuery"}, {"id": "286", "name": "React"},
            {"id": "293", "name": "其它投资"}, {"id": "295", "name": "平面设计"}, {"id": "301", "name": "瓜果"},
            {"id": "373", "name": "SEM"}, {"id": "375", "name": "Android开发"}, {"id": "376", "name": "IOS"},
            {"id": "377", "name": "微信开发"}, {"id": "378", "name": "android"}, {"id": "380", "name": "运维其它"},
            {"id": "381", "name": "软件测试"}, {"id": "382", "name": "运维管理"}, {"id": "383", "name": "信息安全"},
            {"id": "385", "name": "Unity3d游戏开发"}, {"id": "392", "name": "Phone"}, {"id": "387", "name": "Html5游戏"},
            {"id": "388", "name": "VR"}, {"id": "390", "name": "敏捷开发"}, {"id": "391", "name": "软件"},
            {"id": "386", "name": "Cocos2d-x游戏开发"}, {"id": "387", "name": "Html5游戏"}, {"id": "388", "name": "VR"},
            {"id": "390", "name": "敏捷开发"}, {"id": "391", "name": "软件"}, {"id": "392", "name": "Phone"},
            {"id": "394", "name": "云计算"}, {"id": "395", "name": "大数据"}, {"id": "396", "name": "数据库"},
            {"id": "397", "name": "Hadoop开发"}, {"id": "399", "name": "嵌入式"}, {"id": "401", "name": "IT认证"},
            {"id": "402", "name": "计算机基础"}, {"id": "403", "name": "基金"}, {"id": "404", "name": "股票"},
            {"id": "405", "name": "期货"}, {"id": "407", "name": "婚恋"}, {"id": "408", "name": "时尚美妆"},
            {"id": "409", "name": "宠物绿植"}, {"id": "410", "name": "美食烹饪"}, {"id": "411", "name": "手工DIY"},
            {"id": "412", "name": "星座"}, {"id": "415", "name": "健身"}, {"id": "416", "name": "武术"},
            {"id": "417", "name": "养生"}, {"id": "418", "name": "体育"}, {"id": "419", "name": "舞蹈"},
            {"id": "420", "name": "其它运动"}, {"id": "421", "name": "瑜伽"}, {"id": "423", "name": "声乐乐器"},
            {"id": "424", "name": "音乐制作"}, {"id": "425", "name": "书画创作"}, {"id": "482", "name": "韩语零基础"},
            {"id": "484", "name": "韩语中高级"}, {"id": "485", "name": "旅游韩语"}, {"id": "486", "name": "韩流文化"},
            {"id": "487", "name": "TOPIK考试/留学"}, {"id": "488", "name": "法语"}, {"id": "489", "name": "泰语"},
            {"id": "490", "name": "西班牙语"}, {"id": "491", "name": "葡萄牙语"}, {"id": "492", "name": "方言"},
            {"id": "493", "name": "其他"}, {"id": "494", "name": "网页设计"}, {"id": "495", "name": "形象设计"},
            {"id": "496", "name": "服装设计"}, {"id": "497", "name": "网店设计"}, {"id": "498", "name": "VI设计"},
            {"id": "500", "name": "交互设计"}, {"id": "501", "name": "游戏UI设计"}
        ]
        self._id = subject_list[i]['id']

        self._name = subject_list[i]['name']
        print(self._name)
        self._new_id = subject_list[80-i]['id']
        self._new_name = subject_list[80-i]['name']

    def setup(self):
        self._fcm = FlowCostMgt()

    @logger('case')
    @allure.step('新增流量成本-手机-普通投放模式')
    def test_add_flow_cost_mgt_mobile(self):
        with allure.step('新增流量成本-手机-普通投放模式'):
            self._fcm.flow_cost_mgt_save(costMonth=self._cm, subjectId=self._id, subjectName=self._name)

    @logger('case')
    @allure.step('新增流量成本-微信-普通投放模式')
    def test_add_flow_cost_mgt_wx(self):
        with allure.step('新增流量成本-微信-普通投放模式'):
            self._fcm.flow_cost_mgt_save(gatherType=3, costMonth=self._cm, subjectId=self._id, subjectName=self._name)

    @logger('case')
    @allure.step('新增流量成本-QQ-普通投放模式')
    def test_add_flow_cost_mgt_qq(self):
        with allure.step('新增流量成本-QQ-普通投放模式'):
            self._fcm.flow_cost_mgt_save(gatherType=2, costMonth=self._cm, subjectId=self._id, subjectName=self._name)

    @logger('case')
    @allure.step('修改流量成本-QQ-普通投放模式')
    def test_update_flow_cost_mgt(self):
        with allure.step('新增流量成本-QQ-普通投放模式'):
            self._fcm.flow_cost_mgt_save(gatherType=2, costMonth=self.new_time, subjectId=self._new_id,
                                         subjectName=self._new_name)
        with allure.step('查询流量成本记录'):
            self._fcm.flow_cost_mgt_page_list(gatherType=2, startCostMonth=self.new_time, endCostMonth=self.next_end,
                                              channelId=4)
        with allure.step('修改流量成本记录'):
            self._fcm.flow_cost_mgt_update()

    @logger('case')
    @allure.step('修改流量成本为微信获客方式-普通投放模式')
    def test_update_flow_cost_mgt_gather(self):
        with allure.step('新增流量成本-手机-普通投放模式'):
            self._fcm.flow_cost_mgt_save(gatherType=1, costMonth=self.new_time, subjectId=self._new_id,
                                         subjectName=self._new_name)
        with allure.step('查询流量成本记录'):
            self._fcm.flow_cost_mgt_page_list(gatherType=1, startCostMonth=self.new_time, endCostMonth=self.next_end,
                                              channelId=4)
        with allure.step('修改流量成本记录,手机方式改成WX'):
            self._fcm.flow_cost_mgt_update(gatherType=3)

    @logger('case')
    @allure.step('删除流量成本为微信获客方式-普通投放模式')
    def test_del_flow_cost_mgt(self):
        with allure.step('新增流量成本-微信-普通投放模式'):
            self._fcm.flow_cost_mgt_save(gatherType=3, costMonth=self.new_time, subjectId=self._id,
                                         subjectName=self._name)
        with allure.step('查询流量成本记录'):
            self._fcm.flow_cost_mgt_page_list(gatherType=3, startCostMonth=self.new_time, endCostMonth=self.next_end,
                                              channelId=4)
        with allure.step('删除流量成本记录'):
            self._fcm.del_flow_cost_mgt()

    @logger('case')
    @allure.step('批量删除流量成本为微信获客方式-普通投放模式')
    def test_del_flow_cost_mgt_batch(self):
        with allure.step('查询流量成本记录'):
            res = self._fcm.flow_cost_mgt_page_list(startCostMonth=self.new_time, endCostMonth=self.next_end)
            rs = res['data']['list']
            id_list = []
            if len(rs):
                for i in range(len(rs)):
                    id = rs[i]['id']
                    id_list.append(id)
            ids = ','.join(str(i) for i in id_list)
        with allure.step('批量删除流量成本记录'):
            self._fcm.del_flow_cost_mgt(ids=ids)
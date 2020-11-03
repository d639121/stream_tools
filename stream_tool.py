#!/usr/bin/python 
# @Time  : 2020/10/16 17:28
# @Author: Fold
# @Desc  :

import sys
import time
from PyQt5.QtWidgets import QMainWindow, QApplication
from Tools.scripts.make_ctype import rc
from config.constant import const, GLOBAL_VAR
from control.base.login import login
from control.yinhe.account_module.agent_manager import AgentManager
from control.yinhe.account_module.contract_manager import ContractManager
from control.yinhe.account_module.email_manager import EmailManager
from control.yinhe.account_module.put_account_manager import PutAccountManager
from control.yinhe.ad_module.ad_idea.add_consumer_single import ConsumerSingle
from control.yinhe.ad_module.ad_idea.create_ad_idea import CreateAdIdea
from control.yinhe.ad_module.ad_idea.import_flow_single import ImportFlow
from control.yinhe.ad_module.ad_idea.qry_ad_ideals import QryIdeals
from control.yinhe.ad_module.ad_plan.create_ad_plan import CreateAdPlan
from control.yinhe.tool_module.create_landing_page_wx import CrtLadingPage
from control.yinhe.case_execute import ExecuteTestCases
from control.yinhe.flow_module.check_mobile_success import Check
from control.yinhe.flow_module.students_inp import StudentsInput
from control.yinhe.tool_module.website import Website
from utils.redis import ConnRedis
from control.yinhe.ad_module.ad_idea.crt_ad_idea import AddAdIdea
from control.yinhe.flow_module.orders_record import OrdersRecord
from pages import page_main

class MainDialog(QMainWindow):

    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.ui = page_main.Ui_MainWindow()
        self.ui.setupUi(self)
        self.aai = AddAdIdea()

    def login_tools(self):
        account = self.ui.account.text().strip()
        password = self.ui.password.text().strip()
        env = self.ui.env.currentText()
        rc.set_en(env)
        login.login_action(account=account, password=password)
        self.ui.comNum.setText('当前登录账号:' + account)
        self.ui.baudNum.setText('当前环境:' + env)
        self.ui.stackedWidget.setCurrentIndex(0)


    def crt_orders_record(self):
        cor = OrdersRecord()
        cor.test_order_record()

    def crt_ad_idea(self):
        gather_t = self.ui.comboBox.currentText()
        alloc_t = self.ui.comboBox_3.currentText()
        put_m = self.ui.comboBox_2.currentText()
        nee = self.ui.comboBox_4.currentText()
        vector = self.ui.lineEdit_3.text().strip()
        sub_id = self.ui.lineEdit_6.text().strip()
        times = self.ui.spinBox.value()
        gather = {"手机": 1, "QQ": 2, "微信": 3}
        alloc_inst_type = {"计划分配": 1, "手动分配": 2, "直线下发": 3}
        mode = {"普通投放": 1, "小咖投放": 2, "高转VIP": 3, "APP": 4, "接待": 5}
        needs = {"需要验码": 1, "不要验码": 0, "个人微信": 2, "企业微信": 3}
        gather_type = gather[gather_t]
        put_mode = mode[put_m]
        alloc_type = alloc_inst_type[alloc_t]
        need = needs[nee]
        if need == 2:
            wx = 0
        if need == 3:
            wx = 1
        i = 1
        for i in range(times):
            proname = const.projectName
            GLOBAL_VAR['projectName'] = proname
            ideaname = const.ideaName
            GLOBAL_VAR['ideaName'] = ideaname
            cma = CreateAdPlan()
            cmc = CreateAdIdea()
            aai = AddAdIdea()
            oj = ConnRedis()
            cma.program_inf_save(gatherType=gather_type, putMode=put_mode, allocInstType=alloc_type, name=proname,
                                 subjectId=sub_id)
            cma.program_page_list(gatherType=gather_type)

            if gather_type == 3 and alloc_type == 3:
                aai.create_wc_ad_idea_for_tools(vector=vector, isEnterpriseWx=wx)
            else:
                cmc.creativity_sav(isNeedCaptch=need, name=ideaname)
            result = cmc.creativity_page_list(gatherType=gather_type)
            id = result['data']['list'][0]['id']
            name = result['data']['list'][0]['name']
            programId = result['data']['list'][0]['programId']
            programName = result['data']['list'][0]['programName']
            subjectName = result['data']['list'][0]['subjectName']
            allocInstType = {v: k for k, v in alloc_inst_type.items()}[result['data']['list'][0]['allocInstType']]
            putMode = {v: k for k, v in mode.items()}[result['data']['list'][0]['putMode']]

            res = '创意ID：{}\n创意名称：{}\n计划ID：{}\n计划名称：{}\n科目名称：{}\n分配方式：{}\n投放模式：{}\n'.format(
                id, name, programId, programName, subjectName, allocInstType, putMode,
            )

            self.ui.textEdit.setText(res)
            # fuc_name = sys._getframe().f_code.co_name
            oj.set_redis('createIdeas')
            time.sleep(1)


    def import_flow(self):
        times = self.ui.spinBox_2.value()
        i = 1
        for i in range(times):
            imf = ImportFlow()
            ideal = self.ui.lineEdit.text().strip()
            phone = const.phoneNumber
            time = str(const.todyTime)
            qq = const.qq
            excel = {
                "1": ["客户昵称（姓名）", "手机号码（必填）", "QQ号码", "微信", "参考年龄", "流量来源时间（必填,三天内数据）", "地域（市级，非必填）", "流量备注"],
                "2": ["张三", phone, qq, qq, 20, time, "长沙市", "流量备注"]
            }
            imf.import_mobile_unit(excel, adNo=ideal)
            oj = ConnRedis()
            oj.set_redis('importFlow')

    def imp_consumer(self):
        con = ConsumerSingle()
        time = const.todayStartTimestamp
        GLOBAL_VAR['creativityId'] = self.ui.lineEdit_2.text().strip()
        con.imp_consumer_single(costDate=time)
        oj = ConnRedis()
        oj.set_redis('importConsume')

    def crt_landing_page(self):
        wb = Website()
        qi = QryIdeals()
        c = Check()
        c_wx = CrtLadingPage()
        GLOBAL_VAR['adName'] = const.projectName
        GLOBAL_VAR['creativityId'] = self.ui.lineEdit_4.text().strip()
        vec = self.ui.lineEdit_7.text().strip()
        project_id = self.ui.lineEdit_5.text().strip()
        GLOBAL_VAR['goodsId'] = project_id
        t_module = self.ui.comboBox_5.currentText()
        t_type = self.ui.comboBox_6.currentText()
        webName = const.websiteName
        GLOBAL_VAR['websiteName'] = webName

        if t_module == '手动创建广告':
            if t_type == '仅提交-需要验证码':
                qi.qry_ideals(gatherType=1)
                wb.landing_page_crt(1, 1)
                c.list_landing_page()
            elif t_type == '仅提交-不需要验证码':
                qi.qry_ideals(gatherType=1)
                wb.landing_page_crt(1, 0)
                c.list_landing_page()
            elif t_type == '一键提交':
                qi.qry_ideals(gatherType=1)
                wb.landing_page_crt(0, 1, goodsId=project_id)
                c.list_landing_page()
            elif t_type == '个人微信':
                c_wx.create_landingpage_for_wc()
            elif t_type == '先支付再个人微信':
                c_wx.create_landingpage_for_wc(good_id=project_id)
            elif t_type == '企业微信':
                c_wx.create_landingpage_for_company_wc()
            elif t_type == '先支付再企业微信':
                c_wx.create_landingpage_for_company_wc(good_id=project_id)
            elif t_type == '活动':
                GLOBAL_VAR['url'] = '暂未增加此场景，待后续增加'
            elif t_type == '先支付后活动':
                GLOBAL_VAR['url'] = '暂未增加此场景，待后续增加'
        else:
            if t_type == '仅提交-不需要验证码-计划':
                c_wx.create_landing_page_api(1)
            elif t_type == '仅提交-需要验证码-计划':
                c_wx.create_landing_page_api(2)
            elif t_type == '仅提交-不需要验证码-手动':
                c_wx.create_landing_page_api(3)
            elif t_type == '仅提交-需要验证码-手动':
                c_wx.create_landing_page_api(4)
            elif t_type == '仅提交-不需要验证码-直线':
                c_wx.create_landing_page_api(5)
            elif t_type == '仅提交-需要验证码-直线':
                c_wx.create_landing_page_api(6)
            elif t_type == '一键提交-手动':
                c_wx.create_landing_page_api(7, goods_id=project_id)
            elif t_type == '一键提交-直线':
                c_wx.create_landing_page_api(8, goods_id=project_id)
            elif t_type == '企业微信':
                self.aai.qry_vector_api(carrierName=vec)
                c_wx.create_landing_page_for_company_api()
            elif t_type == '先支付再企业微信':
                self.aai.qry_vector_api(carrierName=vec)
                c_wx.create_landing_page_for_company_api(good_id=project_id)
        res = GLOBAL_VAR['url']
        print(res)
        rest = '链接：{}\n'.format(res)
        self.ui.textEdit_2.setText(rest)
        oj = ConnRedis()
        oj.set_redis('createLangdingPage')

    def add_channel_agency(self):
        am = AgentManager()
        channel_name = self.ui.lineEdit_11.text().strip()
        channel_id = self.ui.lineEdit_12.text().strip()
        third_agency_code = self.ui.lineEdit_13.text().strip()
        agency_name = self.ui.lineEdit_14.text().strip()
        am.add_agent(channelId=channel_id, channelName=channel_name, thirdAgencyCode=third_agency_code,
                     agencyName=agency_name, agencyShortName=agency_name)
        res = str(am.qry_channel_agency(thirdAgencyCode=third_agency_code))
        self.ui.agent_result.setText(res)
        oj = ConnRedis()
        oj.set_redis('createAgent')

    def add_channel_agency_rebate(self):
        am = AgentManager()
        rebate = self.ui.lineEdit_29.text().strip()
        am.add_rebate(rebate=rebate)
        time.sleep(1)
        res = str(am.qry_channel_agency_rebate())
        self.ui.rebate_result.setText(res)
        oj = ConnRedis()
        oj.set_redis('createRebate')

    def student_imp(self):
        times = self.ui.spinBox_3.value()
        i = 1
        for i in range(times):
            si = StudentsInput()
            subject_id = self.ui.lineEdit_8.text().strip()
            name = self.ui.lineEdit_9.text().strip()
            gt = self.ui.comboBox_13.currentIndex()+1
            if gt == 1:
                res = str(si.imp_phone_flow_free(subjectId=subject_id, subjectName=name))
            elif gt == 2:
                res = str(si.imp_qq_flow_free(subjectId=subject_id, subjectName=name))
            else:
                res = str(si.imp_wx_flow_free(subjectId=subject_id, subjectName=name))
            self.ui.textBrowser.setText(res)
            oj = ConnRedis()
            oj.set_redis('student_imp')

    def student_input(self):
        times = self.ui.spinBox_3.value()
        i = 1
        for i in range(times):
            si = StudentsInput()
            subject_id = self.ui.lineEdit_8.text().strip()
            name = self.ui.lineEdit_9.text().strip()
            chain = self.ui.lineEdit_10.text().strip()
            gt = self.ui.comboBox_13.currentIndex() + 1
            res = str(si.add_student(gatherType=gt, subject_id=subject_id, subject_name=name, rdc=chain))
            self.ui.textBrowser.setText(res)
            oj = ConnRedis()
            oj.set_redis('student_inp')

    def exe_test_case_ad(self):
        et = ExecuteTestCases()
        et.run_target_module('ad')

    def exe_test_case_budget(self):
        et = ExecuteTestCases()
        et.run_target_module('budget')

    def exe_test_case_data(self):
        et = ExecuteTestCases()
        et.run_target_module('data')

    def exe_test_case_flow(self):
        et = ExecuteTestCases()
        et.run_target_module('flow')

    def exe_test_case_system(self):
        et = ExecuteTestCases()
        et.run_target_module('system')

    def exe_test_case_tool(self):
        et = ExecuteTestCases()
        et.run_target_module('tool')

    def exe_test_case_account(self):
        et = ExecuteTestCases()
        et.run_target_module('account')

    def mail_generate(self):
        em = EmailManager()
        apply_id = self.ui.lineEdit_30.text().strip()
        GLOBAL_VAR['applyId'] = apply_id
        res = str(em.generate_email())
        self.ui.textEdit_5.setText(res)
        oj = ConnRedis()
        oj.set_redis('generateMail')

    def send_mail(self):
        em = EmailManager()
        mail_id = self.ui.lineEdit_31.text().strip()
        GLOBAL_VAR['mailId'] = mail_id
        res = str(em.send_email())
        self.ui.textEdit_5.setText(res)
        oj = ConnRedis()
        oj.set_redis('sendMail')

    def crt_account(self):
        pam = PutAccountManager()
        cn = self.ui.lineEdit_58.text().strip()  # 渠道名称
        ci = self.ui.lineEdit_59.text().strip()  # 渠道id
        cai = self.ui.lineEdit_60.text().strip()  # 渠道代理商id
        an = self.ui.lineEdit_61.text().strip()  # 账户名称
        at = self.ui.comboBox_22.currentIndex()+1
        result = pam.add_acc(channelName=cn, channelId=ci, channelAgencyId=cai, accountName=an, accountType=at)
        res = str(result)
        self.ui.account_result.setText(res)
        oj = ConnRedis()
        oj.set_redis('createPutAccount')

    def crt_contract(self):
        cm = ContractManager()
        ci = self.ui.lineEdit_32.text().strip()
        cn = self.ui.lineEdit_51.text().strip()
        chn = self.ui.lineEdit_52.text().strip()
        chi = self.ui.lineEdit_53.text().strip()
        asn = self.ui.lineEdit_54.text().strip()
        ac = self.ui.lineEdit_55.text().strip()
        r = self.ui.lineEdit_57.text().strip()
        cai = self.ui.lineEdit_56.text().strip()
        ft = self.ui.comboBox_21.currentIndex()+1
        result = cm.create_contract(contractId=ci, contractName=cn, channelName=chn, channelId=chi, agencyShortName=asn,
                                    agencyCode=ac, rebates=r, channelAgencyId=cai, fapiaoType=ft)
        res = str(result)
        self.ui.textBrowser_4.setText(res)
        oj = ConnRedis()
        oj.set_redis('createContract')


if __name__ == '__main__':
    myapp = QApplication(sys.argv)
    myDlg = MainDialog()
    myDlg.show()
    sys.exit(myapp.exec_())

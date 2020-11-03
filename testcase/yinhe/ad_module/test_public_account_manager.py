#!/usr/bin/python
# @Time   : 2020/8/26 20:14
# @Author : Jones
# @Desc   : 公众号管理

from allure_commons._allure import step
from common.config_log import logger
from stream_tools.config.constant import GLOBAL_VAR, const
from stream_tools.config.read_config import rc
from control.base.login import login
from control.yinhe.ad_module.public_account_manager import PublicAccountManager


class TestPublicAccountManager:

    def setup(self):
        self._pam = PublicAccountManager()
        if rc.get_env() == 'pre':
            login.login_action('t0322511032')
        else:
            login.login_action('t0383212689')

    @step('广告-公众号管理-新增')
    @logger('case')
    def test_add_public_account(self):
        name = const.qq
        with step('新增公众号'):
            self._pam.add_public_account(name=name)
        with step('新增后查询'):
            self._pam.query_public_account(name=name)
            assert GLOBAL_VAR['gzh_name'] == name

    @step('广告-公众号管理-编辑')
    @logger('case')
    def test_editor_public_account(self):
        name = const.qq
        wx = const.title
        with step('新增公众号'):
            self._pam.add_public_account(name=name)
        with step('新增后查询获取公众号ID'):
            self._pam.query_public_account(name=name)
        with step('编辑公众号'):
            self._pam.editor_public_account(wx=wx)
            self._pam = PublicAccountManager()
            self._pam.query_public_account(name=name)
            assert GLOBAL_VAR['gzh_wx'] == wx

    @step('广告-公众号管理-删除')
    @logger('case')
    def test_del_public_account(self):
        name = const.qq
        with step('新增公众号'):
            self._pam.add_public_account(name=name)
        with step('新增后查询获取公众号ID'):
            self._pam.query_public_account(name=name)
        with step('删除公众号'):
            self._pam.del_public_account()
            self._pam.query_del_public_account(name=name)
            assert GLOBAL_VAR['totalItem'] == '0'

    @step('广告-公众号管理-批量导入')
    @logger('case')
    def test_import_public_account(self):
        if rc.get_env() == 'pre':
            excel = {
                "1": ["公众号名称(必填)", "科目（必填，输入的科目请和CRM系统保持一致）", "渠道（必填）", "合同时间（必填,格式YYYY-MM-DD）",
                      "打款时间（必填,格式YYYY-MM-DD）",
                      "号主联系方式（必填）", "价格（必填，请输入标准的数字）", "投放时间（YYYY-MM-DD）",
                      "微信号", "流量数（标准数字）", "报名数（标准数字）", "发文链接", "创建人潭州账号（必填，请输入CRM系统中存在的潭州账号）"],
                "2": ["张三", "C++", "公众号", "2019-10-25", "2019-10-25", "ksmebaby", "436", "2019-10-25", "tzyhMax", "52",
                      "0", "www.test.com", "t0322511032"],
                "3": ["李四", "C++", "公众号", "2019-10-25", "2019-10-25", "ksmebaby", "436", "2019-10-25", "tzyhMax", "52",
                      "0", "www.test.com", "t0322511032"],
                "4": ["王五", "C++", "公众号", "2019-10-25", "2019-10-25", "ksmebaby", "436", "2019-10-25", "tzyhMax", "52",
                      "0", "www.test.com", "t0322511032"],
            }
        else:
            excel = {
                "1": ["公众号名称(必填)", "科目（必填，输入的科目请和CRM系统保持一致）", "渠道（必填）", "合同时间（必填,格式YYYY-MM-DD）", "打款时间（必填,格式YYYY-MM-DD）",
                      "号主联系方式（必填）", "价格（必填，请输入标准的数字）", "投放时间（YYYY-MM-DD）",
                      "微信号", "流量数（标准数字）", "报名数（标准数字）", "发文链接", "创建人潭州账号（必填，请输入CRM系统中存在的潭州账号）"],
                "2": ["张三", "PHP", "公众号", "2019-10-25", "2019-10-25", "ksmebaby", "436", "2019-10-25", "tzyhMax", "52", "0", "www.test.com", "t0383212689"],
                "3": ["李四", "PHP", "公众号", "2019-10-25", "2019-10-25", "ksmebaby", "436", "2019-10-25", "tzyhMax", "52", "0", "www.test.com", "t0383212689"],
                "4": ["王五", "PHP", "公众号", "2019-10-25", "2019-10-25", "ksmebaby", "436", "2019-10-25", "tzyhMax", "52", "0", "www.test.com", "t0383212689"],
            }
        self._pam.import_public_account(excel=excel)
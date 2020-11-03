#!/usr/bin/python
# @Time  : 2020/4/3 17:05
# @Author: LOUIE
# @Desc  : 设置凭证

from config.read_config import rc
from common.config_log import log
from control.base.login import login
import requests


class SetToken():

    def __init__(self):
        env = rc.get_env().title()
        log.info("************** 当前运行环境: %s *************" % env)
        self.partner, self.leader, self.students, self.cookie = rc.get_account_info(env)

    def get_platform_token(self):
        leader_token = login.login_action(self.leader, action=False)
        # partner_token = login.login_action(self.partner, action=False)
        return leader_token #, partner_token

    def get_students_token(self):
        students_token = login.login_action(self.students, type='class', action=False)
        return students_token

    def get_jsessionid(self):
        url = "https://admin-fat.shiguangkey.com/captcha.jpg"
        cookie = self.cookie
        url = rc.set_env(url)
        res = requests.get(url)
        set_cookie = res.headers.get("Set-Cookie")
        JSESSIONID = str(set_cookie).split(";")[0]
        print(JSESSIONID)
        # 利用反射拿到cookies常量并格式化JSESSIONID合成最新cookies
        operation_cookie = cookie.format(JSESSIONID)
        return operation_cookie

    def set_token_to_config(self):
        '''
        将凭证数据写入配置文件
        :return: None
        '''
        leader = self.get_platform_token()
        # students = self.get_students_token()
        cookie = self.get_jsessionid()
        try:
            # rc.set_token('partner', str(partner))
            rc.set_token('leader', str(leader))
            # rc.set_token('students', str(students))
            rc.set_token('cookie', str(cookie))
            log.info("凭证获取成功并写入 /common/config.txt 配置文件中")
        except Exception as e:
            log.error("凭证获取失败，请检查！错误: %s" %e)


if __name__ == '__main__':
    SetToken().set_token_to_config()

#!/usr/bin/python 
# @Time    : 2020/6/3 21:09
# @Author  : LOUIE
# @Desc  : 工具函数

import requests
from stream_tools.config.read_config import rc
from datetime import datetime
from testcase.conftest import passed, failed


title = "流程自动化脚本【apiFlowAutoTest】"
url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=c6e56725-386e-48ac-90ee-c9d07c647ce9"   # Official Hook
# url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=82991c03-ba73-4e66-b2db-c086c755ae29"   # Test Hook

def struct_desc():
    '''
    构造描述信息
    '''
    env = rc.get_env().title()
    today = datetime.now().strftime('%Y-%m-%d %H:%M')
    desc = "{} \n日期: {}  环境: {} \n运行结果: \n用例合计: {} 条\n通过用例: {} 条\n失败用例: {} 条".format(title, today, env,len(passed) + len(failed),len(passed), len(failed))
    return desc

def send_wechat_news():
    '''
    发送企业微信消息
    :return:
    '''
    headers = {"Content-Type": "text/plain"}
    data = {
    "msgtype": "text",
    "text": {
        "content": struct_desc(),
    }
    }
    res = requests.post(url=url, headers=headers, json=data)
    json_data = res.json()
    print(json_data)
    if json_data["errcode"] == 0:
        print("企业微信消息已发送!!")
    else:
        print("#### 企业微信消息发送失败!请核对errcode码")


if __name__ == '__main__':
    send_wechat_news()
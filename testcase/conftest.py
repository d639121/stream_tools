#!/usr/bin/python 
# @Time   : 2020/4/28 19:34
# @Author : Jones
# @DesC   : 配置项
import os

import pytest
from stream_tools.config.set_token import SetToken


passed = []
failed = []

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport():
    # 获取钩子方法的调用结果
    out = yield
    # 3. 从钩子方法的调用结果中获取测试报告
    report = out.get_result()
    print('用例结果:', report)
    if report.when=='call' and report.passed:
        passed.append(report.passed)
    elif report.when=='call' and report.failed:
        failed.append(report.failed)

@pytest.fixture(scope="session", autouse=True)
def set_token():
    """
    获取token写入配置文件，scop级别设置为session，脚本运行时只调用一次
    :return:
    """
    SetToken().set_token_to_config()

@pytest.fixture()
def login():
    print('登录成功')


def get_root_path():
    '''
    获取当前项目根目录
    :return:
    '''
    cur_path = os.getcwd()
    all_file = [f for f in os.listdir(cur_path)]
    if 'apiFlowAutoTest' in cur_path:
        while not cur_path.endswith('apiFlowAutoTest'):
            cur_path = os.path.abspath(os.path.join(cur_path, "./.."))
        return cur_path
    else:
        while 'report' and 'common' not in all_file:
            cur_path = os.path.abspath(os.path.join(cur_path, "./.."))
            all_file = [f for f in os.listdir(cur_path)]
        return cur_path

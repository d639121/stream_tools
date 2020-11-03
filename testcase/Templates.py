#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/4 18:28
# @Author  : LOUIE

"""
测试用例模板文件
"""

from utils.operation_yaml import OperationYAML
from common.http_requests import httprequest
from stream_tools.config.constant import GLOBAL_VAR
from common.config_log import log
from utils.operation_json import OperationJson as Opt_json
from common.common_tools import CommonTools as cotool
import pytest
import allure

"""
@allure.epic()	        epic描述	        敏捷里面的概念，定义史诗，往下是feature
@allure.feature()	    模块名称	        功能点的描述，往下是story
@allure.story()	        用户故事	        用户故事，往下是title
@allure.title(用例标题)	用例的标题	    重命名html报告名称
@allure.testcase()	    测试用例链接地址	对应功能测试用例系统里面的case
@allure.issue()	        缺陷	            对应缺陷管理系统里面的链接
@allure.description()	用例描述	        测试用例的描述
@allure.step()	        操作步骤	        测试用例的步骤
@allure.severity()	    用例等级	        blocker，critical，normal，minor，trivial
@allure.link()	        链接	            定义一个链接，在测试报告展现
@allure.attachment()	附件	            报告添加附件
"""

data = OperationYAML().rafactor_data("Template.yaml")


allure.feature("流程名称")
class TestTemplates():      # 测试类必须以Test开头

    def setup(self):        # 在每个方法运行之前执行 setup 中的操作，同样还有setup_class,setup_module
        pass

    def teardown_class(self):   # 在每个类运行之前执行 teardown_class 中的操作，teardown,teardown_module
        # 将整个全局字典写入json文件
        Opt_json("Template.json").write_to_res_json(GLOBAL_VAR)

    @pytest.mark.parametrize("caseid, desc, precondition, parameterize, url, method, header, data, shared, check", data)
    def test_democase(self, caseid, desc, precondition, parameterize, url, method, header, data, shared, check):
        # 打印日志信息
        log.info("CaseId: <- {} ->".format(caseid))
        log.info("Desc: {}".format(desc))
        # 判断是否需要前置运行所需接口
        if precondition:
            print("我需要前置条件")
        # 处理header
        header = cotool().set_header(header)
        # 处理params中的参数
        params = cotool().set_params(parameterize, data)
        res = httprequest(url, method, header, params)
        # 对res进行提取变量处理
        if shared:
            cotool.extract_variable(res, shared)
        # 断言code及msg，后期取断言data中的字段是否存在于res中
        cotool().assert_res(res, check)
        # allure记录信息
        allure.dynamic.story("CaseID: < {} > - {}".format(caseid, desc))


if __name__ == '__main__':
    pytest.main(["-sv", __file__])

"""
pytest常用命令：
pytest --help：查看帮助文档，当不记得命令时，使用此命令即可，常用
参数：-s
运行过程中执行print打印函数：pytest -s
参数： --collect-only 或 --co
收集将要执行的用例，但不会执行用例：pytest --collcet-onty，可以使用这个参数查看一下命令是否正确，是否能够收集到指定的测试用例
参数：-k args（args：可以是py文件名，也可以是函数名）
运行包含关键词的用例：pytest -k change，如图：
参数：-v / --verbose  或 -q / --quiet 
打印用例执行的详细或简略过程，pytest -v ，pytest -q
参数：pytest --html=path
生成简易html报告，path是存储报告的路径。
参数：--alluredir=DIR 和 --clean-alluredir
--alluredir=DIR：在指定目录DIR生成allure报告
--clean-alluredir：清除alluredir如果目录存在的化
一般结合 --alluredir=DIR 命令一起使用 pytest --alluredir=./report/html --clean-alluredir
参数：-x
用例运行失败则立即停止执行
参数：--maxfail=num
用例运行时 允许的最大失败次数，超过则立即停止，pytest --maxfail=3
参数：-m 'mark1 and not mark2' 
--markers  显示所有mark标记
用例运行带有mark1标记的并且不运行mark2标记的
参数：--tb=选项（选项：'auto', 'long', 'short', 'no', 'line', 'native'）
用例运行失败时，展示错误的详细程度
参数：-l 或--showlocals
用例运行失败时，打印相关的局部变量，pytest -l
参数：--lf, --last-failed
只执行上次执行失败的测试
参数：--ff, --failed-first
先执行完上次失败的测试后，再执行上次正常的测试
参数：运行指定的函数（使用两对冒号 : 分隔）
pytest 模块名::类名::函数名，pytest test.py::check_ui
Allure命令：
commond: generate
生成allure报告
示例：allure generate ./report/xlm -o ./report/html -c  ./report/html
参数：-c, --clean
在生成新的Allure报告之前，先清除该目录
参数： -o, --report-dir, --output
指定目录生成allure报告
commond：open 
打开生成的报告，本地查看
示例：allure open ./report/html 
参数：-h, --host
指定域名地址
参数：-p, --port
指定端口号
commond：serve
打开生成的报告，可对外提供在线展示
示例：allure serve./report/html 
参数：-h, --host
指定域名地址
参数：-p, --port
指定端口号

"""
#!/usr/bin/python
# @Time   : 2020/8/12 11:35
# @Author : Jones
# @Desc   : 流量-分配准备

from allure_commons._allure import step
from common.config_log import logger
from control.yinhe.flow_module.allot_prepare import AllotPrepare


class TestAllotPrepare:

    def setup(self):
        self._app = AllotPrepare()

    @step('流量-分配准备-查询')
    @logger('case')
    def test_allot_prepare_query(self):
        self._app.allot_prepare_query()

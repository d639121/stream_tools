#!/usr/bin/python
# @Time   : 2020/8/12 11:35
# @Author : Jones/Louie
# @Desc   : 流量-分配记录查询

from allure_commons._allure import step
from common.config_log import logger
from control.yinhe.flow_module.allot_record_query import AllotRecordQuery
import pytest


class TestAllotRecordQuery:

    def setup(self):
        self._arq = AllotRecordQuery()

    @step('流量-分配记录查询-查询')
    @logger('case')
    def test_query_allot_plan(self):
        self._arq.allot_record_query()

    @step('导出到院查询记录')
    @logger('case')
    def test_export_record(self):
        self._arq.export_record()

    @step('导出到人查询记录')
    @logger('case')
    def test_export_person_record(self):
        self._arq.export_person_record()
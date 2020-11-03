#!/usr/bin/python 
# @Time  : 2020/10/24 14:46
# @Author: Fold
# @Desc  :
import os

import pytest

from config.read_config import rc


class ExecuteTestCases:
    def run_target_module(self, module_name):
        args = ['-sl']
        case_dir = os.path.join(rc.PROJECT_PATH, 'testcase\yinhe')
        if module_name == 'account':
            args.append(os.path.join(case_dir, 'account_module'))
        elif module_name == 'ad':
            args.append(os.path.join(case_dir, 'ad_module'))
        elif module_name == 'budget':
            args.append(os.path.join(case_dir, 'budget_module'))
        elif module_name == 'data':
            args.append(os.path.join(case_dir, 'data_module'))
        elif module_name == 'flow':
            args.append(os.path.join(case_dir, 'flow_module'))
        elif module_name == 'system':
            args.append(os.path.join(case_dir, 'system_module'))
        elif module_name == 'tool':
            args.append(os.path.join(case_dir, 'tool_module'))
        elif module_name == 'all':
            args.append(case_dir)
        else:
            print('module_name参数传值错误，请传入指定参数！')
        print('指定路径', args)
        print('当前路径：', os.getcwd())
        pytest.main(args)

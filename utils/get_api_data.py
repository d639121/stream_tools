#!/usr/bin/python 
# -*- coding: utf-8 -*-
# @Time    : 2020/7/13 10:43
# @Author  : LOUIE

import yaml
import os
from config.constant import const
from config.read_config import rc


class GetApiData():

    def _get_yaml_path(self, module, yaml_path):

        api_yaml_path = os.path.join(rc.PROJECT_PATH, 'data/api', module, yaml_path)
        with open(api_yaml_path, mode="r", encoding="utf-8") as file:
            data = yaml.full_load(file)
        return data

    def get_api_data(self, params):
        desc = []
        url = []
        parameterize = []
        method = []
        header = []
        param = []
        check = []
        shared = []
        desc.append(params.get("desc", None))
        url.append(rc.set_env(params["url"]))
        parameterize.append(params.get("parameterize", None))
        method.append(params.get('method'))
        header.append(params.get("header", None))
        param.append(params.get("data", None))
        shared.append(params.get("shared", None))
        check.append(params.get("check", None))
        list_data = list(zip(desc, parameterize, url, method, header, param, shared, check))[0]
        return list_data

    def get_haichuan_data(self, yaml_path):
        data = self._get_yaml_path('haichuan', yaml_path)
        conf_data = data.get('config')['valueable']
        const.pre_data = conf_data
        return data

    def get_yinhe_data(self, yaml_path):
        data = self._get_yaml_path('yinhe', yaml_path)
        conf_data = data.get('config')['valueable']
        const.pre_data = conf_data
        return data

    def get_CRM_data(self, yaml_path):
        data = self._get_yaml_path('CRM', yaml_path)
        return data

    def get_base_data(self, yaml_path):
        data = self._get_yaml_path('base', yaml_path)
        return data

    def get_tzkt_data(self, yaml_path):
        data = self._get_yaml_path('tzkt', yaml_path)
        return data

    # def set_yinhe_data(self, module='yinhe', yaml_path=None):
    #     config_data = self._get_yaml_path(module, yaml_path)['config']['valueable']
    #     return config_data



get_data = GetApiData()


# if __name__ == '__main__':
#     # print(get_data.set_yinhe_data(yaml_path='ad_module/ad_idea.yaml'))
#     data = get_data.get_base_data('login_account.yaml')
#     print(data)
#     import re
#     compile = re.compile(r'\$<(\w+?)>')
#     res = compile.findall(str(data))
#     from config.constant import GLOBAL_VAR, const
#     from utils.get_value import gv
#     glob = {}
#     for i in res:
#         glob[i] = GLOBAL_VAR[i]
#     data = gv.resolve_global_var(data, glob)
#     print(data)

#!/usr/bin/python
# @Time  : 2020/3/25 16:00
# @Author: LOUIE
# @Desc  : 操作 YAML 文件

from stream_tools.config.read_config import rc
import yaml


class OperationYAML():

    def operate_yaml(self, file):

        yaml_path = rc.PROJECT_PATH + "/data/case" + file
        if not yaml_path.endswith(".yaml"):
            yaml_path = str(yaml_path) + ".yaml"
        try:
            with open(yaml_path, 'r+', encoding="utf-8") as f:
                data = yaml.load(f, Loader=yaml.Loader)
            return data
        except Exception as e:
            print("YAML文件获取数据失败，请检查！")
            raise e

    def rafactor_data(self, filename):
        caseid = []
        desc = []
        url = []
        method = []
        header = []
        data = []
        shared = []
        check = []
        precondition = []
        parameterize = []
        params = self.operate_yaml(filename)
        for key, value in params.items():
            for i in range(0, len(value)):
                if value[i]["run"] is True:
                    desc.append(value[i]["desc"])
                    caseid.append(value[i]["caseid"])
                    handle_url = rc.set_env(value[i]['url'])
                    url.append(handle_url)
                    method.append(value[i]["method"])
                    shared.append(value[i]["shared"])
                    check.append(value[i]["check"])
                    precondition.append(value[i]["precondition"])
                    parameterize.append(value[i]["parameterize"])
                    if "header" in value[i]:
                        header.append(value[i]["header"])
                    else:
                        header.append(None)
                    if value[i]["data"] is not None:
                        data.append(value[i]['data'])
                    else:
                        data.append(None)
        data = list(zip(caseid, desc, precondition, parameterize, url, method, header, data, shared, check))
        return data


oyaml = OperationYAML()






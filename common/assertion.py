#!/usr/bin/python 
# @Time  : 2020/9/19 10:13
# @Author: LOUIE
# @Desc  : 断言

import re


class Assertion:

    def __init__(self):
        pass

    @classmethod
    def check(self, responseObj, checkPoint):
        responseBody = responseObj
        errorKey = {}
        for key, value in checkPoint.items():
            if key in responseBody:
                if isinstance(value, (str, int)):
                    # 等值校验
                    if responseBody[key] != value:
                        errorKey[key] = responseBody[key]
                elif isinstance(value, dict):
                    sourceData = responseBody[key]
                    if "value" in value:
                        # 模糊匹配校验
                        regStr = value["value"]
                        rg = re.match(regStr, "%s" % sourceData)
                        if not rg:
                            errorKey[key] = sourceData
                    elif "type" in value:
                        # 数据类型校验
                        typeS = value["type"]
                        if typeS == "N":
                            # 说明是整形校验
                            if not isinstance(sourceData, int):
                                errorKey[key] = sourceData
            else:
                errorKey[key] = "[%s] not exist" % key
        return errorKey
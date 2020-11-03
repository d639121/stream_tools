#!/usr/bin/python
# @Time  : 2020/4/20 14:37
# @Author: LOUIE
# @Desc  : HTTP请求方法

from common.config_log import log
import requests
import json


class HttpRequest():

    def __init__(self):
        self.session = requests.session()

    def send_request(self, url, method, headers=None, data=None, cookies=None, **kwargs):
        """
        发起 http 请求：
        首先判断 method 请求方法，如果是 post 方法， 依据头部中的 content-type 字段判断传参方式
        eg: request = HttpRequests()
            response = request(method, url, data)
            or
            response = request.send_request(method, url, data)
            print(response.text)
        :param url: 完整请求地址
        :param method: 请求方法，默认post请求
        :param headers: 请求头部信息
        :param data: 请求正文
        :param cookies: cookies信息，非必传
        :return: response
        """
        method = method.upper()
        log.info("请求地址: %s" % url)
        log.info("请求方法: [- %s -]" % method)
        log.info("请求头部: %s" % headers)
        if cookies:
            log.info("Set Cookies: %s" % cookies)
        if isinstance(data, str):
            try:
                data = json.loads(data)
            except Exception:
                data = eval(data)
        log.info("请求正文: %s" % data)
        if method == "POST":
            if headers["content-type"] == "application/x-www-form-urlencoded":
                response = requests.post(url=url, data=data, headers=headers, cookies=cookies, timeout=30, **kwargs)
            elif headers["content-type"] == "application/json":
                response = requests.post(url=url, json=data, headers=headers, cookies=cookies, timeout=30, **kwargs)
            else:
                response = requests.post(url=url, data=data, headers=headers, cookies=cookies, timeout=30, verify=False, **kwargs)
        elif method == "GET":
            response = requests.get(url=url, params=data, headers=headers, cookies=cookies, timeout=30, **kwargs)
        else:
            print("Method 值错误，请检查!!!")
        try:
            if response.status_code == 200:
                log.info("响应消息: %s" % response.json())
                return response.json()
        except json.decoder.JSONDecodeError:
            return response
        except Exception as e:
            log.error("Error: %s" % e)
        return response

    def __call__(self, url, method, headers=None, data=None, **kwargs):
        """
        示例，可以直接通过类对象实例直接调用此方法
        request = HttpRequests()
        response = request(method, url, data)
        """
        return self.send_request(url, method, headers, data, **kwargs)

    def close_session(self):
        '''
        关闭session请求方法
        '''
        self.session.close()
        try:
            del self.session.cookies['JSESSIONID']
        except:
            pass


httprequest = HttpRequest()

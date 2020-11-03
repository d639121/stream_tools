#!/usr/bin/python 
# @Time  : 2020/5/18 10:12
# @Author: LOUIE
# @Desc  : 通用方法文件

from common.config_log import log
from config.constant import const,GLOBAL_VAR
from utils.get_api_data import get_data
from utils.get_value import gv
from config.read_config import rc
from common.http_requests import httprequest


class CommonTools:
    # def __init__(self):
    #     self.pre_data = const.pre_data

    def extract_variable(self, res, shared):
        '''
        提取变量方法
        :param res: 响应内容response
        :param shared: 提取response中的参数名
        :return:
        '''
        if shared is not None:
            for k, v in shared.items():
                if "-" not in v:
                    value = gv.get_jsonpath_value(res, v)
                else:
                    key, num = str(v).split("-")
                    value = gv.get_jsonpath_value(obj=res, key=key, num=int(num))
                GLOBAL_VAR[k] = value
                setattr(const, k, value)
                log.info("提取变量: [ {}: {} ]".format(k, value))

    def set_params(self, parameterize, params):
        '''
        参数化处理数据
        :param parameterize: 参数化配置
        :param params: yaml文件中最基础的data数据
        :return: params/data
        '''
        data = None
        if rc.get_env() == 'pre':
            if len(const.pre_data) > 0:
                for k, v in const.pre_data.items():
                    if params is not None:
                        if k in params.keys():
                            params[k] = v
            # return params
            if parameterize is not None:
                for k, v in parameterize.items():
                    if k in v:
                        parameterize[k] = GLOBAL_VAR[v]
                        data = gv.resolve_global_var(params, parameterize)
                    else:
                        return params
                return data
            else:
                return params
        elif parameterize is not None:
            for k, v in parameterize.items():
                if k in v:
                    parameterize[k] = GLOBAL_VAR[v]
                    data = gv.resolve_global_var(params, parameterize)
                else:
                    return params
            return data
        else:
            return params

    def set_header(self, header):
        '''
        处理header中的token方法
        :param header: 原生header数据
        :return: header
        '''
        if header is not None:
            if "token" in header.keys():
                token = str(header['token']).replace('$<', '').replace('>', '')
                header["token"] = GLOBAL_VAR.get(token, GLOBAL_VAR['leader'])
            elif "cookie" in header.keys():
                header["cookie"] = rc.get_token("cookie")
            # 解决多次调用查询时报的主机拒绝远程连接的错误
            # if "user-agent" not in header.keys():
            #     header["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36"
            # header["Connection"] = "close"
            # header["keep-alive"] = "False"
            return header
        else:
            return header

    def deal_data(self, data):
        '''
        封装整体方法
        :param data: 传入的数据
        :return: url, method, header, params, shared, check
        '''
        data = get_data.get_api_data(data)
        desc, parameterize, url, method, header, param, shared, check = data
        log.info('描述信息: %s' % desc)
        header = self.set_header(header)
        params = self.set_params(parameterize, param)
        return url, method, header, params, shared, check

    def quick_request(self, data, **kwargs):
        '''
        封装整体方法
        :param data: 传入的数据
        :param kwargs: 传入的字典会加入到data中
        :return: res
        '''
        data = get_data.get_api_data(data)
        desc, parameterize, url, method, header, param, shared, check = data
        log.info('描述信息: %s' % desc)
        header = self.set_header(header)
        params = self.set_params(parameterize, param)
        if kwargs:
            params = dict(params, **kwargs)
        res = httprequest(url, method, header, params)
        self.extract_variable(res, shared)
        self.assert_res(res, check)
        return res

    def quick_rqt(self, data, **kwargs):
        '''
        封装整体方法
        :param data: 传入的数据
        :param kwargs: 传入的字典会加入到data中
        :return: res
        '''
        data = get_data.get_api_data(data)
        desc, parameterize, url, method, header, param, shared, check = data
        log.info('描述信息: %s' % desc)
        header = self.set_header(header)
        params = self.set_params(parameterize, param)
        if kwargs:
            params = dict(params, **kwargs)
        res = httprequest(url, method, header, params)
        self.extract_variable(res, shared)
        return res

    def assert_res(self, res, check):
        '''
        断言方法
        当 check 为 no_check、no和 None 时跳过断言
        当 check 为 dict 类型时, 判断字段是否存在于 code 和 entity 字典中,进行断言
        :param res: 响应内容 response
        :param check: YAML文件中的 check 节点数据
        :return: None
        '''
        code = ['code', 'status', 'res', 'msg']
        entity = ['data', 'result']
        if check == "no_check" or check is None:
            log.info("This Api Has No Check!")
        elif isinstance(check, dict):
            for k,j in check.items():
                if k in code:
                    acode = res[k]
                    ecode = check[k]
                    assert str(acode) == str(ecode)
                    log.info('校验类型: [-{}], 结果: [Passed], 预期: [{}]'.format(k, str(ecode)) )
                if k in entity:
                    data = res[k]
                    for check_param in check["data"]:
                        if isinstance(check_param, dict):
                            for k, v in check_param.items():
                                if k == 'in':
                                    assert v in str(data)
                                    log.info('校验类型: [-in]  结果: [Passed]  预期: {}'.format(v))
                                if str(k).replace(' ', '') == 'notin':
                                    assert v not in str(data)
                                    log.info('校验类型: [-notin]  结果: [Passed]  预期: {}'.format(v))
                                if k == 'eq':
                                    for m, n in v.items():
                                        assert n == gv.get_jsonpath_value(data, m)
                                        log.info('校验类型: [-eq]  结果: [Passed]  预期: {}'.format(v))
                                if k == 'tag':
                                    assert GLOBAL_VAR[v] in str(data)
                                    log.info('校验类型: [-tag]  结果: [Passed]  预期: {}'.format(GLOBAL_VAR[v]))
                                if k == 'notnone':
                                    assert check["data"] is not None
                                    log.info('校验类型: [-notnone]  结果: [Passed]  预期: NotNone')
                        elif isinstance(check_param, str):
                            assert check_param in str(data)
                            log.info('校验类型: [-in]  结果: [Passed]  预期: [{}]'.format(check_param))
                        else:
                            print('请输入正确校验数据格式！！')
                if k == 'status_code':
                    assert res.status_code == int(j)
                    log.info('校验类型: [-status_code]  结果: [Passed]  预期: [{}]'.format(j))
        else:
            print("YAML文件中 check 非字典类型，类型错误！")
        log.info(' = = = ' * 8 + '分割线' + ' = = = ' * 8)

cotool = CommonTools()

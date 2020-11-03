#!/usr/bin/python
# @Time  : 2020/7/27 15:50
# @Author: Fold
# @Desc  : 操作EXCEL

import datetime
import os
import ssl
import xlwt
from config.read_config import rc
from urllib3 import encode_multipart_formdata
import urllib3
urllib3.disable_warnings()

ssl._create_default_https_context = ssl._create_unverified_context


class SendFile():

    '''
    form-data方式进行请求的post
    '''

    def add_excel(self, excel):
        '''
        创建excel文件，将数据写入excel
        :param excel: excel中的数据
        :return:
        '''
        timeStr = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        workbook = xlwt.Workbook(encoding='utf-8')
        # 创建一个worksheet
        sheet = workbook.add_sheet("Sheet1")
        ldata = []
        num = [a for a in excel]
        # for循环指定取出key值存入num中
        num.sort()
        # 字典数据取出后无需，需要先排序
        for x in num:
            # for循环将data字典中的值分批的保存在ldata中
            t = excel[x]
            ldata.append(t)
        for row, p in enumerate(ldata):
            for item, value in enumerate(p):
                sheet.write(row, item, value)
        if not os.path.exists(rc.PROJECT_PATH):
            os.makedirs(rc.PROJECT_PATH)
        file_name = "import%s.xlsx" % timeStr  # 文件名
        xls_path = os.path.join(rc.PROJECT_PATH, "config/excel", file_name)  # 构建文件路径
        # 保存
        workbook.save(xls_path)
        return file_name, xls_path

    def delete(self, path):
        '''
        删除excel文件
        :param path: 文件路径
        :return:
        '''
        if os.path.exists(path):  # 如果文件存在
            # 删除文件，可使用以下两种方法。
            os.remove(path)
        else:
            print('no such file!')  # 则返回文件不存在
    def send_file(self,  colume_name, data):
        """
        :param filename：文件的名称
        :param file_path：文件的绝对路径
        :param data：yaml文件中的原始data数据
        """
        ae = SendFile()
        file_name, file_path = ae.add_excel(colume_name)
        with open(file_path, mode="rb")as f:  # 打开文件
            data['file'] = (file_name, f.read())
            files = data
            encode_data = encode_multipart_formdata(files)
            file_data = encode_data[0]
            content_type = encode_data[1]
            return file_data, content_type, file_path

    def send_others_file(self, file_name, data):
        """
        :param file_name:
        :param data：yaml文件中的原始data数据
        """
        PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file_path = os.path.join(PROJECT_PATH, "config/excel", file_name)
        with open(file_path, mode="rb")as f:  # 打开文件
            data['file'] = (file_name, f.read())
            files = data
            encode_data = encode_multipart_formdata(files)
            file_data = encode_data[0]
            content_type = encode_data[1]
            return file_data, content_type, file_path


oe = SendFile()



#!/usr/bin/python 
# @Time  : 2020/10/19 18:07
# @Author: Fold
# @Desc  :
from common.common_tools import cotool
from utils.get_api_data import get_data


class QryIdeals():

    def __init__(self):
        self._data = get_data.get_yinhe_data('ad_module/ad_idea.yaml')

    def qry_ideals(self, **kwargs):
        data = self._data.get('qry_ideals')
        cotool.quick_rqt(data, **kwargs)


# if __name__ == '__main__':
#     qi = QryIdeals()
#     qi.qry_ideals(gatherType=1)
#!/usr/bin/python 
# @Time  : 2020/8/10 19:50
# @Author: Fold
# @Desc  : 商品管理

from common.common_tools import cotool
from common.config_log import logger
from utils.get_api_data import get_data


class GoodsManage:

    def __init__(self):
        self._data = get_data.get_yinhe_data('tool_module/goods_manage.yaml')

    @logger()
    def goods_manage(self, **kwargs):
        """
        邀课引流管理查询
        :param teachingMethod: 教学方式  8010.直播  8011录播
        :param isSmallClass: 是否精品小课  1.是 0.否
        :param goodsStatus: 状态  1.上架 2.下架
        :param courseFlag: 商品来源  0.自建课程 1.教务系统  2.小咖课程
        :param cateIds: 科目 [a,b,c] a是一级科目 b是二级科目 c是三级科目
        :param nickName: 创建者
        :param goodsName: 商品名称
        :param courseId: 课程id
        :param pageNo: 页码，第几页 默认第一页，可修改
        :param pageSize: 每页数据 默认20条，可修改
        :param tabType: 1. 新流量 2.老流量 此处为默认参数，可修改
        :param kwargs: 上述参数通过kwargs进行传递
        :return:
        """

        data = self._data.get('goods_page_list')
        cotool.quick_request(data, **kwargs)
# -*- coding: utf-8 -*-
from common.pxfilter import XssHtml
from common.utils import html_escape


class InvalidData(Exception):
    pass


def valid_organization(data):
    if data['name'] != '':
        pass
    else:
        raise InvalidData(u'组织名字不能为空')

    if len(data['head']) == 0 or len(data['eva_member']) == 0:
        raise InvalidData(u'负责人或评价人员不能为空')


def valid_award(data):
    if data['name'] != '':
        pass
    else:
        raise InvalidData(u'奖项名字不能为空')
    if data['begin_time'] > data['end_time']:
        raise InvalidData(u'开始时间不能晚于结束时间')
    for k, v in data.items():
        if v == '' or v is None:
            raise InvalidData(u'不能为空')

    # 验证时xss富文本过滤
    parser = XssHtml()
    parser.feed(data['requirement'])
    parser.close()
    data['requirement'] = parser.getHtml()
    data['name'] = html_escape(data['name'])


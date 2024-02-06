#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：flask-server 
@File    ：response.py
@IDE     ：PyCharm 
@Author  ：xuyj
@Date    ：2024/2/6 15:20 
"""


class JsonResponse(object):
    """
    统一的json返回格式
    """

    def __init__(self, data, code, msg, status):
        self.data = data
        self.code = code
        self.message = msg
        self.status = status

    @classmethod
    def success(cls, data=None, code='0', msg='', status='success'):
        return cls(data, code, msg, status)

    @classmethod
    def error(cls, data=None, code='-1', msg='', status='error'):
        return cls(data, code, msg, status)

    def to_dict(self):
        return {
            "code": self.code,
            "data": self.data,
            "message": self.message,
            "status": self.status,
        }

#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：flask-server 
@File    ：flask_overwrite.py
@IDE     ：PyCharm 
@Author  ：xuyj
@Date    ：2024/2/6 15:19 
"""
"""
继承flask中的Flask类，重写相关函数
项目中的所有Flask都引自这里，不再引用原生的flask中的Flask
"""
from flask import Flask as _Flask, jsonify

from server.util.response import JsonResponse


class Flask(_Flask):
    def make_response(self, rv):
        if rv is None or isinstance(rv, (list, dict)):
            rv = JsonResponse.success(rv)
        if isinstance(rv, JsonResponse):
            rv = jsonify(rv.to_dict())

        return super().make_response(rv)

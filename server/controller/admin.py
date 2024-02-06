#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：flask-server 
@File    ：admin.py
@IDE     ：PyCharm 
@Author  ：xuyj
@Date    ：2024/2/6 15:18 
"""
from flask import current_app

from server.controller import admin_blue
from server.util.response import JsonResponse


@admin_blue.route('/alluser')
def alluser():
    current_app.logger.info('/admin/alluser')
    return JsonResponse.success('alluser')


@admin_blue.route('/deluser')
def deluser():
    current_app.logger.info('/admin/deluser')
    return JsonResponse.success('deluser')

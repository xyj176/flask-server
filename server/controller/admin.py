#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：flask-server 
@File    ：admin.py
@IDE     ：PyCharm 
@Author  ：xuyj
@Date    ：2024/2/6 15:18 
"""
from flask import Blueprint, current_app

from server.util.response import JsonResponse

admin_blue = Blueprint(name='admin', import_name=__name__, url_prefix='/admin')


@admin_blue.route('/alluser')
def alluser():
    current_app.logger.info('/admin/alluser')
    return JsonResponse.success('alluser')


@admin_blue.route('/deluser')
def deluser():
    current_app.logger.info('/admin/deluser')
    return JsonResponse.success('deluser')

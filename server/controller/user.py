#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：flask-server 
@File    ：user.py
@IDE     ：PyCharm 
@Author  ：xuyj
@Date    ：2024/2/6 15:18 
"""
from flask import Blueprint, current_app

from server.util.response import JsonResponse

user_blue = Blueprint(name='user', import_name=__name__, url_prefix='/user')


# 请求地址：ip+port+/user/register
@user_blue.route('/register')
def register():
    current_app.logger.info('/user/register')
    return JsonResponse.success('register')


# 请求地址：ip+port+/user/login
@user_blue.route('login')
def login():
    current_app.logger.info('/user/login')
    return JsonResponse.success('login')


# 请求地址：ip+port+/user/modify_pw
@user_blue.route('/modify_pw')
def modify_pw():
    current_app.logger.info('/user/modify_pw')
    return JsonResponse.success('modify_pw')

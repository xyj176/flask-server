#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：flask-server 
@File    ：user.py
@IDE     ：PyCharm 
@Author  ：xuyj
@Date    ：2024/2/6 15:18 
"""
from flask import current_app, request

from server.controller import user_blue
from server.model import User, db
from server.util.response import JsonResponse


# 请求地址：ip+port+/user/register
@user_blue.route('/register', methods=['GET', 'POST'])
def register():
    current_app.logger.info('/user/register')
    name = request.form.get('name')
    password = request.form.get('password')
    user = User(name=name, password=password)
    # 提交到数据库
    db.session.add(user)
    db.session.commit()
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

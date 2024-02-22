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
    # 注册
    name = request.args.get('name')
    query = User.query.filter_by(name=name).first()
    if query is not None:
        return JsonResponse.success(data='用户名已存在，请重新注册！')
    password = request.args.get('password')
    user = User(name=name, password=password)
    # 提交到数据库
    db.session.add(user)
    db.session.commit()
    return JsonResponse.success('注册成功！')


# 请求地址：ip+port+/user/login
@user_blue.route('login')
def login():
    current_app.logger.info('/user/login')
    # 登录判断
    name = request.args.get('name')
    password = request.args.get('password')
    user = User.query.filter_by(name=name, password=password).first()
    if user is None:
        return JsonResponse.success(data='用户名或密码不匹配，登录失败！')
    return JsonResponse.success(data='登录成功')


# 请求地址：ip+port+/user/modify_pw
@user_blue.route('/modify_pw')
def modify_pw():
    current_app.logger.info('/user/modify_pw')
    # 修改密码
    name = request.args.get('name')
    query = User.query.filter_by(name=name).first()
    if query is None:
        return JsonResponse.success(data='用户名不存在！')
    new_password = request.args.get('new_password')
    if len(new_password) == 0:
        return JsonResponse.success(data='密码为空，请重新输入！')
    query.password = new_password
    db.session.commit()
    return JsonResponse.success('密码修改成功！')


@user_blue.route('/query/<int:id>')
def query_by_id(id):
    # 根据主键查询
    user = User.query.get_or_404(id)
    return JsonResponse.success(data=user.name)


@user_blue.route('/query/all')
def query_all():
    # users = User.query.all()
    # result = '一共有{}条记录'.format(len(users))
    count = User.query.count()
    result = '一共有{}条记录'.format(count)
    return JsonResponse.success(data=result)


@user_blue.route('/query/like')
def query_like():
    users = User.query.filter(User.name.startswith('x')).all()
    # users = User.query.filter(User.name.endswith('x')).all()
    # users = User.query.filter(User.name.contains('x')).all()
    return JsonResponse.success(data='模糊查询')


@user_blue.route('/update')
def update():
    user = User.query.filter_by(name='xyj').first()
    user.password = 'xin'
    db.session.commit()
    return JsonResponse.success(data='更新完成')


@user_blue.route('/delete')
def delete():
    # 查询
    user = User.query.get(9)
    # 删除
    if user is not None:
        db.session.delete(user)
    # 同步到数据库
    db.session.commit()
    return JsonResponse.success(data='删除成功')

#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：flask-server 
@File    ：__init__.py.py
@IDE     ：PyCharm 
@Author  ：xuyj
@Date    ：2024/2/6 15:17 
"""
from flask import Blueprint

# 定义蓝图
admin_blue = Blueprint(name='admin', import_name=__name__, url_prefix='/admin')
user_blue = Blueprint(name='user', import_name=__name__, url_prefix='/user')
upload_blue = Blueprint(name='upload', import_name=__name__, url_prefix='/upload')

# 引入相应的子模块，让其内部的接口函数生效
from . import admin
from . import user
from . import upload

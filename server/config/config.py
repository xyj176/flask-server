#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：flask-server 
@File    ：config.py
@IDE     ：PyCharm 
@Author  ：xuyj
@Date    ：2024/2/6 14:40 
"""


class Config(object):
    """默认配置"""
    SECRET_KEY = '产品密钥'
    SQLALCHEMY_DATABASE_URI = 'postgresql://cspon:dist2023@192.168.1.15:5432/cspon'
    SQLALCHEMY_TRACK_MODIFICATIONS = True  # 动态追踪修改
    SQLALCHEMY_ECHO = True  # 显示生成的SQL语句，可用于调试
    UPLOAD_FOLDER = 'upload'  # 文件上传的保存文件夹
    RESULT_FOLDER = 'result'  # 结果保存文件夹
    STATIC_FOLDER = 'static'  # 静态文件夹

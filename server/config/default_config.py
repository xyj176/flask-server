#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：flask-server 
@File    ：default_config.py
@IDE     ：PyCharm 
@Author  ：xuyj
@Date    ：2024/2/6 14:40 
"""

# 定义配置对象
from server.config import configData


class Config(object):
    """默认配置"""
    HOST = configData['host'] if configData['host'] is not None else '0.0.0.0'
    PORT = configData['port'] if configData['port'] is not None else 5050
    SECRET_KEY = configData['secret_key'] if configData['secret_key'] is not None else '产品密钥'
    SQLALCHEMY_DATABASE_URI = configData['database']['uri']
    SQLALCHEMY_TRACK_MODIFICATIONS = configData['database']['track']  # 动态追踪修改
    SQLALCHEMY_ECHO = configData['database']['echo']  # 显示生成的SQL语句，可用于调试
    UPLOAD_FOLDER = configData['upload_folder'] if configData['upload_folder'] is not None else 'upload'  # 文件上传的保存文件夹
    RESULT_FOLDER = configData['result_folder'] if configData['result_folder'] is not None else 'result'  # 结果保存文件夹
    STATIC_FOLDER = configData['static_folder'] if configData['static_folder'] is not None else 'static'  # 静态文件夹

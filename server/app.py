#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：flask-server 
@File    ：app.py
@IDE     ：PyCharm 
@Author  ：xuyj
@Date    ：2024/2/6 14:37 
"""
from .config.config import Config
from .controller import admin_blue
from .controller import user_blue
from .util import log
from .flask_overwrite import Flask
from flask import current_app

from server.util.response import JsonResponse


def create_app(config):
    app = Flask(__name__)
    # 读取配置
    app.config.from_object(config)
    # app.config.from_envvar('', silent=True)  # 通过环境变量读取配置

    # 添加日志
    app.logger.addHandler(log.getLogHandler())
    # 注册blueprint,blueprint里面也有接口函数
    app.register_blueprint(user_blue)
    app.register_blueprint(admin_blue)

    return app


# 创建app
app = create_app(Config)


@app.route('/')
def hello():
    current_app.logger.info('hello')
    return JsonResponse.success('hello')


@app.route('/config')
def get_config():
    current_app.logger.info('get_config')
    return JsonResponse.success(app.config.get('SECRET_KEY'))

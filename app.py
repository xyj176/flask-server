#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：flask-server 
@File    ：app.py
@IDE     ：PyCharm 
@Author  ：xuyj
@Date    ：2024/2/6 14:37 
"""
from flask import Flask, current_app

import logHandler
from config import Config


def create_app(config):
    app = Flask(__name__)
    # 读取配置
    app.config.from_object(config)
    # app.config.from_envvar('', silent=True)  # 通过环境变量读取配置
    return app


app = create_app(Config)
app.logger.addHandler(logHandler.getLogHandler())


@app.route('/')
def hello():
    current_app.logger.info('hello')
    return 'hello'


@app.route('/config')
def get_config():
    current_app.logger.info('get_config')
    return app.config.get('SECRET_KEY')

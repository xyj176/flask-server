#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：flask-server 
@File    ：main.py
@IDE     ：PyCharm 
@Author  ：xuyj
@Date    ：2024/2/6 14:35 
"""
# 服务启动的入口
from server.app import app

if __name__ == '__main__':
    host = app.config.get('HOST')
    port = app.config.get('PORT')
    app.run(host=host, port=port)

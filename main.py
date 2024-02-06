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
    app.run(host='0.0.0.0', port=5050)

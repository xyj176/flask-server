#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：flask-server 
@File    ：base.py
@IDE     ：PyCharm 
@Author  ：xuyj
@Date    ：2024/2/21 9:29 
"""
from server.model import db


class BaseModel(db.Model):
    __table_args__ = {'schema': 'public'}  # 指定模式
    __abstract__ = True  # 抽象类，可以将其他数据表中的公共字段存放在这个类中，然后继承该类
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
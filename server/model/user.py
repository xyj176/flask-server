#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：flask-server 
@File    ：user.py
@IDE     ：PyCharm 
@Author  ：xuyj
@Date    ：2024/2/21 9:28 
"""
from datetime import datetime

from server.model import db
from server.model.base import BaseModel


class User(BaseModel):
    __tablename__ = 'user'

    name = db.Column(db.String, nullable=False, comment='用户名')
    password = db.Column(db.String, nullable=False, comment='密码')
    email = db.Column(db.String, nullable=True, comment='邮箱')
    time = db.Column('create_time', db.DateTime, default=datetime.now, comment='创建时间')
    update_time = db.Column('update_time', db.DateTime, default=datetime.now, onupdate=datetime.now, comment='更新时间')

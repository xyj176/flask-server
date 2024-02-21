#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：flask-server 
@File    ：__init__.py.py
@IDE     ：PyCharm 
@Author  ：xuyj
@Date    ：2024/2/21 9:20 
"""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .user import User

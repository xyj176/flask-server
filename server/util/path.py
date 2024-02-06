#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：flask-server 
@File    ：path.py
@IDE     ：PyCharm 
@Author  ：xuyj
@Date    ：2024/2/6 15:51 
"""
import os


def make_dir(make_dir_path):
    path = make_dir_path.strip()
    if not os.path.exists(path):
        os.makedirs(path)

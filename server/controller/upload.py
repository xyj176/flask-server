#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：flask-server 
@File    ：upload.py
@IDE     ：PyCharm 
@Author  ：xuyj
@Date    ：2024/2/22 15:51 
"""
import os

from server.controller import upload_blue
from flask import request, current_app
from server.util import JsonResponse


@upload_blue.route('/picture', methods=['POST'])
def upload_picture():
    pic = request.files.get('picture')
    upload_folder = current_app.config.get('UPLOAD_FOLDER')
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)
    pic.save(os.path.join(upload_folder, pic.filename))
    return JsonResponse.success(data='上传成功')

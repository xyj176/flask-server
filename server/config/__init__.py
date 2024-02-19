#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：flask-server 
@File    ：__init__.py.py
@IDE     ：PyCharm 
@Author  ：xuyj
@Date    ：2024/2/6 15:57 
"""
import nacos
import yaml

# Nacos服务器地址
SERVER_ADDRESSES = "192.168.2.230:18848"

# 命名空间
NAMESPACE = "public"

# 用户名和密码
username = 'nacos'
password = 'nacos'

# 获取Nacos客户端工具，四个参数(Nacos服务器地址，命名空间，用户名，密码)
client = nacos.NacosClient(server_addresses=SERVER_ADDRESSES, namespace=NAMESPACE, username=username, password=password)
# 组名
group = "DEFAULT_GROUP"

# data_id
data_id = "flask-nacos-demo"

# 使用pyyaml模块，把从配置中心获取的yaml数据转字典数据
configData = yaml.load(client.get_config(data_id, group), Loader=yaml.FullLoader)

# 打印配置信息
print(configData, type(configData))

from .default_config import Config

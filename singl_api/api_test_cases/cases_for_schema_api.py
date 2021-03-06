# coding:utf-8
from basic_info.get_auth_token import get_headers
import unittest
import requests
import json
from basic_info.data_from_db import *
from basic_info.Open_DB import MYSQL
from basic_info.setting import MySQL_CONFIG, schema_resource

ms = MYSQL(MySQL_CONFIG["HOST"], MySQL_CONFIG["USER"], MySQL_CONFIG["PASSWORD"], MySQL_CONFIG["DB"])


class CreateSchema(unittest.TestCase):
    """测试create schema api"""
    schema_name = time.strftime("%Y%m%d%H%M%S", time.localtime()) + 'schema'

    # 正常创建
    def test_case01(self):
        """正常创建schema"""
        from basic_info.url_info import create_schema_url
        data = {"name": self.schema_name, "fields": [{"name": "id", "type": "int"}], "resource": schema_resource}
        res = requests.post(url=create_schema_url, headers=get_headers(), data=json.dumps(data))
        print(res.status_code, res.json())
        self.assertEqual(res.status_code, 201, 'schema创建失败')
        self.assertIsNotNone(res.text, '创建schema时没有返回schemaid')








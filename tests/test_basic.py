# -*- coding: utf-8 -*-
"""
    :author: Qin Haining (秦海宁)
    :url: http://greyli.com
    :copyright: © 2018 Qin Haining <2364839934@qq.com>
    :license: MIT, see LICENSE for more details.
"""
from flask import current_app

from tests.base import BaseTestCase


class BasicTestCase(BaseTestCase):

    def test_app_exist(self):
        self.assertFalse(current_app is None)

    def test_app_is_testing(self):
        self.assertTrue(current_app.config['TESTING'])

    def test_404_error(self):
        response = self.client.get('/foo')
        data = response.get_data(as_text=True)
        self.assertEqual(response.status_code, 404)
        self.assertIn('404 Error', data)

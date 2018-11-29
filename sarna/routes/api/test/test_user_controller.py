# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from sarna.routes.api.test import BaseTestCase


class TestUserController(BaseTestCase):
    """UserController integration test stubs"""

    def test_get_users(self):
        """Test case for get_users

        Get a list of Users
        """
        query_string = [('page', 1),
                        ('page_size', 100)]
        response = self.client.open(
            '/api/v1/user',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

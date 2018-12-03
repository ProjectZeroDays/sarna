# coding: utf-8

from __future__ import absolute_import

from sarna.routes.api.test import BaseTestCase


class TestClientController(BaseTestCase):
    """ClientController integration test stubs"""

    def test_get_client(self):
        """Test case for get_client

        Get client data
        """
        response = self.client.open(
            '/api/v1/client/{client_id}'.format(client_id=789),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_client_assessments(self):
        """Test case for get_client_assessments

        Get list of assessment of the client
        """
        query_string = [('page', 1),
                        ('page_size', 100)]
        response = self.client.open(
            '/api/v1/client/{client_id}/assessment'.format(client_id=789),
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_client_templates(self):
        """Test case for get_client_templates

        Get list of assessment of the client
        """
        query_string = [('page', 1),
                        ('page_size', 100)]
        response = self.client.open(
            '/api/v1/client/{client_id}/template'.format(client_id=789),
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_clients(self):
        """Test case for get_clients

        Get a list of clients
        """
        query_string = [('page', 1),
                        ('page_size', 100)]
        response = self.client.open(
            '/api/v1/client',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

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

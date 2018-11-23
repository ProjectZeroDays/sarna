# coding: utf-8

from __future__ import absolute_import

from sarna
/ routes / api.models.envelop
from sarna / routes / api.test
import BaseTestCase


class TestClientController(BaseTestCase):
    """ClientController integration test stubs"""

    def test_client_client_id_get(self):
        """Test case for client_client_id_get

        Get client data
        """
        response = self.client.open(
            '/api/v1/client/{client_id}'.format(client_id=789),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_client_get(self):
        """Test case for client_get

        Get a list of clients
        """
        response = self.client.open(
            '/api/v1/client',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest

    unittest.main()

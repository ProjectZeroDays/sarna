# coding: utf-8

from __future__ import absolute_import

from sarna.routes.api.test import BaseTestCase


class TestFindingController(BaseTestCase):
    """FindingController integration test stubs"""

    def test_get_findign_templates(self):
        """Test case for get_findign_templates

        Get a list of finding templates
        """
        query_string = [('page', 1),
                        ('page_size', 100)]
        response = self.client.open(
            '/api/v1/findign',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

# coding: utf-8

from __future__ import absolute_import

from sarna.routes.api.test import BaseTestCase


class TestAssessmentController(BaseTestCase):
    """AssessmentController integration test stubs"""

    def test_get_assessment(self):
        """Test case for get_assessment

        Get assessment data
        """
        response = self.client.open(
            '/api/v1/assessment/{assessment_id}'.format(assessment_id=789),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_assessment_findingis(self):
        """Test case for get_assessment_findingis

        Get a list of findings in assessment
        """
        query_string = [('page', 1),
                        ('page_size', 100)]
        response = self.client.open(
            '/api/v1/assessment/{assessment_id}/findig'.format(assessment_id=789),
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

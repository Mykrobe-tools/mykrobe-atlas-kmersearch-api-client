# coding: utf-8

"""
    K-mer Search API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import kmersearch_api_client
from kmersearch_api_client.api.build_api import BuildApi  # noqa: E501
from kmersearch_api_client.rest import ApiException


class TestBuildApi(unittest.TestCase):
    """BuildApi unit test stubs"""

    def setUp(self):
        self.api = kmersearch_api_client.api.build_api.BuildApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_build_post(self):
        """Test case for build_post

        """
        pass


if __name__ == '__main__':
    unittest.main()

# coding: utf-8

"""
    K-mer Search API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import kmersearch-api-client
from kmersearch-api-client.api.variant_search_api import VariantSearchApi  # noqa: E501
from kmersearch-api-client.rest import ApiException


class TestVariantSearchApi(unittest.TestCase):
    """VariantSearchApi unit test stubs"""

    def setUp(self):
        self.api = kmersearch-api-client.api.variant_search_api.VariantSearchApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_variant_search_post(self):
        """Test case for variant_search_post

        """
        pass


if __name__ == '__main__':
    unittest.main()

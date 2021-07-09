# coding: utf-8

"""
    K-mer Search API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from kmersearch-api-client.configuration import Configuration


class NewSamples(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'sample_paths': 'list[str]',
        'sample_names': 'list[str]'
    }

    attribute_map = {
        'sample_paths': 'sample_paths',
        'sample_names': 'sample_names'
    }

    def __init__(self, sample_paths=None, sample_names=None, local_vars_configuration=None):  # noqa: E501
        """NewSamples - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._sample_paths = None
        self._sample_names = None
        self.discriminator = None

        if sample_paths is not None:
            self.sample_paths = sample_paths
        if sample_names is not None:
            self.sample_names = sample_names

    @property
    def sample_paths(self):
        """Gets the sample_paths of this NewSamples.  # noqa: E501


        :return: The sample_paths of this NewSamples.  # noqa: E501
        :rtype: list[str]
        """
        return self._sample_paths

    @sample_paths.setter
    def sample_paths(self, sample_paths):
        """Sets the sample_paths of this NewSamples.


        :param sample_paths: The sample_paths of this NewSamples.  # noqa: E501
        :type: list[str]
        """

        self._sample_paths = sample_paths

    @property
    def sample_names(self):
        """Gets the sample_names of this NewSamples.  # noqa: E501


        :return: The sample_names of this NewSamples.  # noqa: E501
        :rtype: list[str]
        """
        return self._sample_names

    @sample_names.setter
    def sample_names(self, sample_names):
        """Sets the sample_names of this NewSamples.


        :param sample_names: The sample_names of this NewSamples.  # noqa: E501
        :type: list[str]
        """

        self._sample_names = sample_names

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, NewSamples):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NewSamples):
            return True

        return self.to_dict() != other.to_dict()

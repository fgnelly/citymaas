# coding: utf-8

"""
    Kerbside Curblr Api

    API for serving kerbside assets. Data is served in CurbLR format https://github.com/sharedstreets/curblr  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: tbd@ford.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Authority(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'phone': 'str',
        'url': 'str'
    }

    attribute_map = {
        'name': 'name',
        'phone': 'phone',
        'url': 'url'
    }

    def __init__(self, name=None, phone=None, url=None):  # noqa: E501
        """Authority - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._phone = None
        self._url = None
        self.discriminator = None

        self.name = name
        self.phone = phone
        self.url = url

    @property
    def name(self):
        """Gets the name of this Authority.  # noqa: E501


        :return: The name of this Authority.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Authority.


        :param name: The name of this Authority.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def phone(self):
        """Gets the phone of this Authority.  # noqa: E501


        :return: The phone of this Authority.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this Authority.


        :param phone: The phone of this Authority.  # noqa: E501
        :type: str
        """
        if phone is None:
            raise ValueError("Invalid value for `phone`, must not be `None`")  # noqa: E501

        self._phone = phone

    @property
    def url(self):
        """Gets the url of this Authority.  # noqa: E501


        :return: The url of this Authority.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Authority.


        :param url: The url of this Authority.  # noqa: E501
        :type: str
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(Authority, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Authority):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
# coding: utf-8

"""
    Cloudbreak API

    Cloudbreak is a powerful left surf that breaks over a coral reef, a mile off southwest the island of Tavarua, Fiji. Cloudbreak is a cloud agnostic Hadoop as a Service API. Abstracts the provisioning and ease management and monitoring of on-demand clusters. SequenceIQ's Cloudbreak is a RESTful application development platform with the goal of helping developers to build solutions for deploying Hadoop YARN clusters in different environments. Once it is deployed in your favourite servlet container it exposes a REST API allowing to span up Hadoop clusters of arbitary sizes and cloud providers. Provisioning Hadoop has never been easier. Cloudbreak is built on the foundation of cloud providers API (Amazon AWS, Microsoft Azure, Google Cloud Platform, Openstack), Apache Ambari, Docker lightweight containers, Swarm and Consul. For further product documentation follow the link: <a href=\"http://hortonworks.com/apache/cloudbreak/\">http://hortonworks.com/apache/cloudbreak/</a>

    OpenAPI spec version: 2.9.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class RestRequestDetails(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'request_uri': 'str',
        'media_type': 'str',
        'method': 'str',
        'headers': 'dict(str, str)',
        'cookies': 'dict(str, str)',
        'body': 'str'
    }

    attribute_map = {
        'request_uri': 'requestUri',
        'media_type': 'mediaType',
        'method': 'method',
        'headers': 'headers',
        'cookies': 'cookies',
        'body': 'body'
    }

    def __init__(self, request_uri=None, media_type=None, method=None, headers=None, cookies=None, body=None):
        """
        RestRequestDetails - a model defined in Swagger
        """

        self._request_uri = None
        self._media_type = None
        self._method = None
        self._headers = None
        self._cookies = None
        self._body = None

        if request_uri is not None:
          self.request_uri = request_uri
        if media_type is not None:
          self.media_type = media_type
        if method is not None:
          self.method = method
        if headers is not None:
          self.headers = headers
        if cookies is not None:
          self.cookies = cookies
        if body is not None:
          self.body = body

    @property
    def request_uri(self):
        """
        Gets the request_uri of this RestRequestDetails.

        :return: The request_uri of this RestRequestDetails.
        :rtype: str
        """
        return self._request_uri

    @request_uri.setter
    def request_uri(self, request_uri):
        """
        Sets the request_uri of this RestRequestDetails.

        :param request_uri: The request_uri of this RestRequestDetails.
        :type: str
        """

        self._request_uri = request_uri

    @property
    def media_type(self):
        """
        Gets the media_type of this RestRequestDetails.

        :return: The media_type of this RestRequestDetails.
        :rtype: str
        """
        return self._media_type

    @media_type.setter
    def media_type(self, media_type):
        """
        Sets the media_type of this RestRequestDetails.

        :param media_type: The media_type of this RestRequestDetails.
        :type: str
        """

        self._media_type = media_type

    @property
    def method(self):
        """
        Gets the method of this RestRequestDetails.

        :return: The method of this RestRequestDetails.
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """
        Sets the method of this RestRequestDetails.

        :param method: The method of this RestRequestDetails.
        :type: str
        """

        self._method = method

    @property
    def headers(self):
        """
        Gets the headers of this RestRequestDetails.

        :return: The headers of this RestRequestDetails.
        :rtype: dict(str, str)
        """
        return self._headers

    @headers.setter
    def headers(self, headers):
        """
        Sets the headers of this RestRequestDetails.

        :param headers: The headers of this RestRequestDetails.
        :type: dict(str, str)
        """

        self._headers = headers

    @property
    def cookies(self):
        """
        Gets the cookies of this RestRequestDetails.

        :return: The cookies of this RestRequestDetails.
        :rtype: dict(str, str)
        """
        return self._cookies

    @cookies.setter
    def cookies(self, cookies):
        """
        Sets the cookies of this RestRequestDetails.

        :param cookies: The cookies of this RestRequestDetails.
        :type: dict(str, str)
        """

        self._cookies = cookies

    @property
    def body(self):
        """
        Gets the body of this RestRequestDetails.

        :return: The body of this RestRequestDetails.
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """
        Sets the body of this RestRequestDetails.

        :param body: The body of this RestRequestDetails.
        :type: str
        """

        self._body = body

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, RestRequestDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

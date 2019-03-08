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


class StackDetailsJson(object):
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
        'mpacks': 'dict(str, list[ManagementPackEntry])',
        'version': 'str',
        'repo': 'StackRepoDetailsJson'
    }

    attribute_map = {
        'mpacks': 'mpacks',
        'version': 'version',
        'repo': 'repo'
    }

    def __init__(self, mpacks=None, version=None, repo=None):
        """
        StackDetailsJson - a model defined in Swagger
        """

        self._mpacks = None
        self._version = None
        self._repo = None

        if mpacks is not None:
          self.mpacks = mpacks
        if version is not None:
          self.version = version
        if repo is not None:
          self.repo = repo

    @property
    def mpacks(self):
        """
        Gets the mpacks of this StackDetailsJson.

        :return: The mpacks of this StackDetailsJson.
        :rtype: dict(str, list[ManagementPackEntry])
        """
        return self._mpacks

    @mpacks.setter
    def mpacks(self, mpacks):
        """
        Sets the mpacks of this StackDetailsJson.

        :param mpacks: The mpacks of this StackDetailsJson.
        :type: dict(str, list[ManagementPackEntry])
        """

        self._mpacks = mpacks

    @property
    def version(self):
        """
        Gets the version of this StackDetailsJson.

        :return: The version of this StackDetailsJson.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this StackDetailsJson.

        :param version: The version of this StackDetailsJson.
        :type: str
        """

        self._version = version

    @property
    def repo(self):
        """
        Gets the repo of this StackDetailsJson.

        :return: The repo of this StackDetailsJson.
        :rtype: StackRepoDetailsJson
        """
        return self._repo

    @repo.setter
    def repo(self, repo):
        """
        Sets the repo of this StackDetailsJson.

        :param repo: The repo of this StackDetailsJson.
        :type: StackRepoDetailsJson
        """

        self._repo = repo

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
        if not isinstance(other, StackDetailsJson):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

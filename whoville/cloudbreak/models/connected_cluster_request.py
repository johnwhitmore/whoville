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


class ConnectedClusterRequest(object):
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
        'source_cluster_id': 'int',
        'source_cluster_name': 'str'
    }

    attribute_map = {
        'source_cluster_id': 'sourceClusterId',
        'source_cluster_name': 'sourceClusterName'
    }

    def __init__(self, source_cluster_id=None, source_cluster_name=None):
        """
        ConnectedClusterRequest - a model defined in Swagger
        """

        self._source_cluster_id = None
        self._source_cluster_name = None

        if source_cluster_id is not None:
          self.source_cluster_id = source_cluster_id
        if source_cluster_name is not None:
          self.source_cluster_name = source_cluster_name

    @property
    def source_cluster_id(self):
        """
        Gets the source_cluster_id of this ConnectedClusterRequest.

        :return: The source_cluster_id of this ConnectedClusterRequest.
        :rtype: int
        """
        return self._source_cluster_id

    @source_cluster_id.setter
    def source_cluster_id(self, source_cluster_id):
        """
        Sets the source_cluster_id of this ConnectedClusterRequest.

        :param source_cluster_id: The source_cluster_id of this ConnectedClusterRequest.
        :type: int
        """

        self._source_cluster_id = source_cluster_id

    @property
    def source_cluster_name(self):
        """
        Gets the source_cluster_name of this ConnectedClusterRequest.

        :return: The source_cluster_name of this ConnectedClusterRequest.
        :rtype: str
        """
        return self._source_cluster_name

    @source_cluster_name.setter
    def source_cluster_name(self, source_cluster_name):
        """
        Sets the source_cluster_name of this ConnectedClusterRequest.

        :param source_cluster_name: The source_cluster_name of this ConnectedClusterRequest.
        :type: str
        """

        self._source_cluster_name = source_cluster_name

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
        if not isinstance(other, ConnectedClusterRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

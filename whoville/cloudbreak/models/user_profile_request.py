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


class UserProfileRequest(object):
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
        'credential_name': 'str',
        'credential_id': 'int',
        'image_catalog_name': 'str',
        'ui_properties': 'dict(str, object)'
    }

    attribute_map = {
        'credential_name': 'credentialName',
        'credential_id': 'credentialId',
        'image_catalog_name': 'imageCatalogName',
        'ui_properties': 'uiProperties'
    }

    def __init__(self, credential_name=None, credential_id=None, image_catalog_name=None, ui_properties=None):
        """
        UserProfileRequest - a model defined in Swagger
        """

        self._credential_name = None
        self._credential_id = None
        self._image_catalog_name = None
        self._ui_properties = None

        if credential_name is not None:
          self.credential_name = credential_name
        if credential_id is not None:
          self.credential_id = credential_id
        if image_catalog_name is not None:
          self.image_catalog_name = image_catalog_name
        if ui_properties is not None:
          self.ui_properties = ui_properties

    @property
    def credential_name(self):
        """
        Gets the credential_name of this UserProfileRequest.

        :return: The credential_name of this UserProfileRequest.
        :rtype: str
        """
        return self._credential_name

    @credential_name.setter
    def credential_name(self, credential_name):
        """
        Sets the credential_name of this UserProfileRequest.

        :param credential_name: The credential_name of this UserProfileRequest.
        :type: str
        """

        self._credential_name = credential_name

    @property
    def credential_id(self):
        """
        Gets the credential_id of this UserProfileRequest.

        :return: The credential_id of this UserProfileRequest.
        :rtype: int
        """
        return self._credential_id

    @credential_id.setter
    def credential_id(self, credential_id):
        """
        Sets the credential_id of this UserProfileRequest.

        :param credential_id: The credential_id of this UserProfileRequest.
        :type: int
        """

        self._credential_id = credential_id

    @property
    def image_catalog_name(self):
        """
        Gets the image_catalog_name of this UserProfileRequest.

        :return: The image_catalog_name of this UserProfileRequest.
        :rtype: str
        """
        return self._image_catalog_name

    @image_catalog_name.setter
    def image_catalog_name(self, image_catalog_name):
        """
        Sets the image_catalog_name of this UserProfileRequest.

        :param image_catalog_name: The image_catalog_name of this UserProfileRequest.
        :type: str
        """

        self._image_catalog_name = image_catalog_name

    @property
    def ui_properties(self):
        """
        Gets the ui_properties of this UserProfileRequest.

        :return: The ui_properties of this UserProfileRequest.
        :rtype: dict(str, object)
        """
        return self._ui_properties

    @ui_properties.setter
    def ui_properties(self, ui_properties):
        """
        Sets the ui_properties of this UserProfileRequest.

        :param ui_properties: The ui_properties of this UserProfileRequest.
        :type: dict(str, object)
        """

        self._ui_properties = ui_properties

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
        if not isinstance(other, UserProfileRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

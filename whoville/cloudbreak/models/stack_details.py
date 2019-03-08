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


class StackDetails(object):
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
        'id': 'int',
        'name': 'str',
        'description': 'str',
        'region': 'str',
        'availability_zone': 'str',
        'cloud_platform': 'str',
        'platform_variant': 'str',
        'status': 'str',
        'detailed_status': 'str',
        'status_reason': 'str',
        'cloudbreak_version': 'str',
        'image_identifier': 'str',
        'ambari_version': 'str',
        'cluster_type': 'str',
        'cluster_version': 'str',
        'prewarmed_image': 'bool',
        'existing_network': 'bool',
        'existing_subnet': 'bool',
        'instance_groups': 'list[InstanceGroupDetails]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'region': 'region',
        'availability_zone': 'availabilityZone',
        'cloud_platform': 'cloudPlatform',
        'platform_variant': 'platformVariant',
        'status': 'status',
        'detailed_status': 'detailedStatus',
        'status_reason': 'statusReason',
        'cloudbreak_version': 'cloudbreakVersion',
        'image_identifier': 'imageIdentifier',
        'ambari_version': 'ambariVersion',
        'cluster_type': 'clusterType',
        'cluster_version': 'clusterVersion',
        'prewarmed_image': 'prewarmedImage',
        'existing_network': 'existingNetwork',
        'existing_subnet': 'existingSubnet',
        'instance_groups': 'instanceGroups'
    }

    def __init__(self, id=None, name=None, description=None, region=None, availability_zone=None, cloud_platform=None, platform_variant=None, status=None, detailed_status=None, status_reason=None, cloudbreak_version=None, image_identifier=None, ambari_version=None, cluster_type=None, cluster_version=None, prewarmed_image=False, existing_network=False, existing_subnet=False, instance_groups=None):
        """
        StackDetails - a model defined in Swagger
        """

        self._id = None
        self._name = None
        self._description = None
        self._region = None
        self._availability_zone = None
        self._cloud_platform = None
        self._platform_variant = None
        self._status = None
        self._detailed_status = None
        self._status_reason = None
        self._cloudbreak_version = None
        self._image_identifier = None
        self._ambari_version = None
        self._cluster_type = None
        self._cluster_version = None
        self._prewarmed_image = None
        self._existing_network = None
        self._existing_subnet = None
        self._instance_groups = None

        if id is not None:
          self.id = id
        if name is not None:
          self.name = name
        if description is not None:
          self.description = description
        if region is not None:
          self.region = region
        if availability_zone is not None:
          self.availability_zone = availability_zone
        if cloud_platform is not None:
          self.cloud_platform = cloud_platform
        if platform_variant is not None:
          self.platform_variant = platform_variant
        if status is not None:
          self.status = status
        if detailed_status is not None:
          self.detailed_status = detailed_status
        if status_reason is not None:
          self.status_reason = status_reason
        if cloudbreak_version is not None:
          self.cloudbreak_version = cloudbreak_version
        if image_identifier is not None:
          self.image_identifier = image_identifier
        if ambari_version is not None:
          self.ambari_version = ambari_version
        if cluster_type is not None:
          self.cluster_type = cluster_type
        if cluster_version is not None:
          self.cluster_version = cluster_version
        if prewarmed_image is not None:
          self.prewarmed_image = prewarmed_image
        if existing_network is not None:
          self.existing_network = existing_network
        if existing_subnet is not None:
          self.existing_subnet = existing_subnet
        if instance_groups is not None:
          self.instance_groups = instance_groups

    @property
    def id(self):
        """
        Gets the id of this StackDetails.

        :return: The id of this StackDetails.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this StackDetails.

        :param id: The id of this StackDetails.
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this StackDetails.

        :return: The name of this StackDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this StackDetails.

        :param name: The name of this StackDetails.
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """
        Gets the description of this StackDetails.

        :return: The description of this StackDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this StackDetails.

        :param description: The description of this StackDetails.
        :type: str
        """

        self._description = description

    @property
    def region(self):
        """
        Gets the region of this StackDetails.

        :return: The region of this StackDetails.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """
        Sets the region of this StackDetails.

        :param region: The region of this StackDetails.
        :type: str
        """

        self._region = region

    @property
    def availability_zone(self):
        """
        Gets the availability_zone of this StackDetails.

        :return: The availability_zone of this StackDetails.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """
        Sets the availability_zone of this StackDetails.

        :param availability_zone: The availability_zone of this StackDetails.
        :type: str
        """

        self._availability_zone = availability_zone

    @property
    def cloud_platform(self):
        """
        Gets the cloud_platform of this StackDetails.

        :return: The cloud_platform of this StackDetails.
        :rtype: str
        """
        return self._cloud_platform

    @cloud_platform.setter
    def cloud_platform(self, cloud_platform):
        """
        Sets the cloud_platform of this StackDetails.

        :param cloud_platform: The cloud_platform of this StackDetails.
        :type: str
        """

        self._cloud_platform = cloud_platform

    @property
    def platform_variant(self):
        """
        Gets the platform_variant of this StackDetails.

        :return: The platform_variant of this StackDetails.
        :rtype: str
        """
        return self._platform_variant

    @platform_variant.setter
    def platform_variant(self, platform_variant):
        """
        Sets the platform_variant of this StackDetails.

        :param platform_variant: The platform_variant of this StackDetails.
        :type: str
        """

        self._platform_variant = platform_variant

    @property
    def status(self):
        """
        Gets the status of this StackDetails.

        :return: The status of this StackDetails.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this StackDetails.

        :param status: The status of this StackDetails.
        :type: str
        """

        self._status = status

    @property
    def detailed_status(self):
        """
        Gets the detailed_status of this StackDetails.

        :return: The detailed_status of this StackDetails.
        :rtype: str
        """
        return self._detailed_status

    @detailed_status.setter
    def detailed_status(self, detailed_status):
        """
        Sets the detailed_status of this StackDetails.

        :param detailed_status: The detailed_status of this StackDetails.
        :type: str
        """

        self._detailed_status = detailed_status

    @property
    def status_reason(self):
        """
        Gets the status_reason of this StackDetails.

        :return: The status_reason of this StackDetails.
        :rtype: str
        """
        return self._status_reason

    @status_reason.setter
    def status_reason(self, status_reason):
        """
        Sets the status_reason of this StackDetails.

        :param status_reason: The status_reason of this StackDetails.
        :type: str
        """

        self._status_reason = status_reason

    @property
    def cloudbreak_version(self):
        """
        Gets the cloudbreak_version of this StackDetails.

        :return: The cloudbreak_version of this StackDetails.
        :rtype: str
        """
        return self._cloudbreak_version

    @cloudbreak_version.setter
    def cloudbreak_version(self, cloudbreak_version):
        """
        Sets the cloudbreak_version of this StackDetails.

        :param cloudbreak_version: The cloudbreak_version of this StackDetails.
        :type: str
        """

        self._cloudbreak_version = cloudbreak_version

    @property
    def image_identifier(self):
        """
        Gets the image_identifier of this StackDetails.

        :return: The image_identifier of this StackDetails.
        :rtype: str
        """
        return self._image_identifier

    @image_identifier.setter
    def image_identifier(self, image_identifier):
        """
        Sets the image_identifier of this StackDetails.

        :param image_identifier: The image_identifier of this StackDetails.
        :type: str
        """

        self._image_identifier = image_identifier

    @property
    def ambari_version(self):
        """
        Gets the ambari_version of this StackDetails.

        :return: The ambari_version of this StackDetails.
        :rtype: str
        """
        return self._ambari_version

    @ambari_version.setter
    def ambari_version(self, ambari_version):
        """
        Sets the ambari_version of this StackDetails.

        :param ambari_version: The ambari_version of this StackDetails.
        :type: str
        """

        self._ambari_version = ambari_version

    @property
    def cluster_type(self):
        """
        Gets the cluster_type of this StackDetails.

        :return: The cluster_type of this StackDetails.
        :rtype: str
        """
        return self._cluster_type

    @cluster_type.setter
    def cluster_type(self, cluster_type):
        """
        Sets the cluster_type of this StackDetails.

        :param cluster_type: The cluster_type of this StackDetails.
        :type: str
        """

        self._cluster_type = cluster_type

    @property
    def cluster_version(self):
        """
        Gets the cluster_version of this StackDetails.

        :return: The cluster_version of this StackDetails.
        :rtype: str
        """
        return self._cluster_version

    @cluster_version.setter
    def cluster_version(self, cluster_version):
        """
        Sets the cluster_version of this StackDetails.

        :param cluster_version: The cluster_version of this StackDetails.
        :type: str
        """

        self._cluster_version = cluster_version

    @property
    def prewarmed_image(self):
        """
        Gets the prewarmed_image of this StackDetails.

        :return: The prewarmed_image of this StackDetails.
        :rtype: bool
        """
        return self._prewarmed_image

    @prewarmed_image.setter
    def prewarmed_image(self, prewarmed_image):
        """
        Sets the prewarmed_image of this StackDetails.

        :param prewarmed_image: The prewarmed_image of this StackDetails.
        :type: bool
        """

        self._prewarmed_image = prewarmed_image

    @property
    def existing_network(self):
        """
        Gets the existing_network of this StackDetails.

        :return: The existing_network of this StackDetails.
        :rtype: bool
        """
        return self._existing_network

    @existing_network.setter
    def existing_network(self, existing_network):
        """
        Sets the existing_network of this StackDetails.

        :param existing_network: The existing_network of this StackDetails.
        :type: bool
        """

        self._existing_network = existing_network

    @property
    def existing_subnet(self):
        """
        Gets the existing_subnet of this StackDetails.

        :return: The existing_subnet of this StackDetails.
        :rtype: bool
        """
        return self._existing_subnet

    @existing_subnet.setter
    def existing_subnet(self, existing_subnet):
        """
        Sets the existing_subnet of this StackDetails.

        :param existing_subnet: The existing_subnet of this StackDetails.
        :type: bool
        """

        self._existing_subnet = existing_subnet

    @property
    def instance_groups(self):
        """
        Gets the instance_groups of this StackDetails.

        :return: The instance_groups of this StackDetails.
        :rtype: list[InstanceGroupDetails]
        """
        return self._instance_groups

    @instance_groups.setter
    def instance_groups(self, instance_groups):
        """
        Sets the instance_groups of this StackDetails.

        :param instance_groups: The instance_groups of this StackDetails.
        :type: list[InstanceGroupDetails]
        """

        self._instance_groups = instance_groups

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
        if not isinstance(other, StackDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

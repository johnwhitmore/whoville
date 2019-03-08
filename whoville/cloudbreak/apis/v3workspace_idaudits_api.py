# coding: utf-8

"""
    Cloudbreak API

    Cloudbreak is a powerful left surf that breaks over a coral reef, a mile off southwest the island of Tavarua, Fiji. Cloudbreak is a cloud agnostic Hadoop as a Service API. Abstracts the provisioning and ease management and monitoring of on-demand clusters. SequenceIQ's Cloudbreak is a RESTful application development platform with the goal of helping developers to build solutions for deploying Hadoop YARN clusters in different environments. Once it is deployed in your favourite servlet container it exposes a REST API allowing to span up Hadoop clusters of arbitary sizes and cloud providers. Provisioning Hadoop has never been easier. Cloudbreak is built on the foundation of cloud providers API (Amazon AWS, Microsoft Azure, Google Cloud Platform, Openstack), Apache Ambari, Docker lightweight containers, Swarm and Consul. For further product documentation follow the link: <a href=\"http://hortonworks.com/apache/cloudbreak/\">http://hortonworks.com/apache/cloudbreak/</a>

    OpenAPI spec version: 2.9.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class V3workspaceIdauditsApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def get_audit_event_by_workspace(self, workspace_id, audit_id, **kwargs):
        """
        Get audit event in workspace
        Audit event operations
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_audit_event_by_workspace(workspace_id, audit_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int workspace_id: (required)
        :param int audit_id: (required)
        :return: AuditEvent
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_audit_event_by_workspace_with_http_info(workspace_id, audit_id, **kwargs)
        else:
            (data) = self.get_audit_event_by_workspace_with_http_info(workspace_id, audit_id, **kwargs)
            return data

    def get_audit_event_by_workspace_with_http_info(self, workspace_id, audit_id, **kwargs):
        """
        Get audit event in workspace
        Audit event operations
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_audit_event_by_workspace_with_http_info(workspace_id, audit_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int workspace_id: (required)
        :param int audit_id: (required)
        :return: AuditEvent
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['workspace_id', 'audit_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_audit_event_by_workspace" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'workspace_id' is set
        if ('workspace_id' not in params) or (params['workspace_id'] is None):
            raise ValueError("Missing the required parameter `workspace_id` when calling `get_audit_event_by_workspace`")
        # verify the required parameter 'audit_id' is set
        if ('audit_id' not in params) or (params['audit_id'] is None):
            raise ValueError("Missing the required parameter `audit_id` when calling `get_audit_event_by_workspace`")


        collection_formats = {}

        path_params = {}
        if 'workspace_id' in params:
            path_params['workspaceId'] = params['workspace_id']
        if 'audit_id' in params:
            path_params['auditId'] = params['audit_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['tokenAuth']

        return self.api_client.call_api('/v3/{workspaceId}/audits/event/{auditId}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='AuditEvent',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_audit_events_in_workspace(self, workspace_id, resource_type, resource_id, **kwargs):
        """
        list audit events for the given workspace
        Audit event operations
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_audit_events_in_workspace(workspace_id, resource_type, resource_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int workspace_id: (required)
        :param str resource_type: (required)
        :param int resource_id: (required)
        :return: list[AuditEvent]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_audit_events_in_workspace_with_http_info(workspace_id, resource_type, resource_id, **kwargs)
        else:
            (data) = self.get_audit_events_in_workspace_with_http_info(workspace_id, resource_type, resource_id, **kwargs)
            return data

    def get_audit_events_in_workspace_with_http_info(self, workspace_id, resource_type, resource_id, **kwargs):
        """
        list audit events for the given workspace
        Audit event operations
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_audit_events_in_workspace_with_http_info(workspace_id, resource_type, resource_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int workspace_id: (required)
        :param str resource_type: (required)
        :param int resource_id: (required)
        :return: list[AuditEvent]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['workspace_id', 'resource_type', 'resource_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_audit_events_in_workspace" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'workspace_id' is set
        if ('workspace_id' not in params) or (params['workspace_id'] is None):
            raise ValueError("Missing the required parameter `workspace_id` when calling `get_audit_events_in_workspace`")
        # verify the required parameter 'resource_type' is set
        if ('resource_type' not in params) or (params['resource_type'] is None):
            raise ValueError("Missing the required parameter `resource_type` when calling `get_audit_events_in_workspace`")
        # verify the required parameter 'resource_id' is set
        if ('resource_id' not in params) or (params['resource_id'] is None):
            raise ValueError("Missing the required parameter `resource_id` when calling `get_audit_events_in_workspace`")


        collection_formats = {}

        path_params = {}
        if 'workspace_id' in params:
            path_params['workspaceId'] = params['workspace_id']
        if 'resource_type' in params:
            path_params['resourceType'] = params['resource_type']
        if 'resource_id' in params:
            path_params['resourceId'] = params['resource_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['tokenAuth']

        return self.api_client.call_api('/v3/{workspaceId}/audits/events/{resourceType}/{resourceId}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='list[AuditEvent]',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_audit_events_zip_in_workspace(self, workspace_id, resource_type, resource_id, **kwargs):
        """
        list audit events for the given workspace in zip file
        Audit event operations
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_audit_events_zip_in_workspace(workspace_id, resource_type, resource_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int workspace_id: (required)
        :param str resource_type: (required)
        :param int resource_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_audit_events_zip_in_workspace_with_http_info(workspace_id, resource_type, resource_id, **kwargs)
        else:
            (data) = self.get_audit_events_zip_in_workspace_with_http_info(workspace_id, resource_type, resource_id, **kwargs)
            return data

    def get_audit_events_zip_in_workspace_with_http_info(self, workspace_id, resource_type, resource_id, **kwargs):
        """
        list audit events for the given workspace in zip file
        Audit event operations
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_audit_events_zip_in_workspace_with_http_info(workspace_id, resource_type, resource_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int workspace_id: (required)
        :param str resource_type: (required)
        :param int resource_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['workspace_id', 'resource_type', 'resource_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_audit_events_zip_in_workspace" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'workspace_id' is set
        if ('workspace_id' not in params) or (params['workspace_id'] is None):
            raise ValueError("Missing the required parameter `workspace_id` when calling `get_audit_events_zip_in_workspace`")
        # verify the required parameter 'resource_type' is set
        if ('resource_type' not in params) or (params['resource_type'] is None):
            raise ValueError("Missing the required parameter `resource_type` when calling `get_audit_events_zip_in_workspace`")
        # verify the required parameter 'resource_id' is set
        if ('resource_id' not in params) or (params['resource_id'] is None):
            raise ValueError("Missing the required parameter `resource_id` when calling `get_audit_events_zip_in_workspace`")


        collection_formats = {}

        path_params = {}
        if 'workspace_id' in params:
            path_params['workspaceId'] = params['workspace_id']
        if 'resource_type' in params:
            path_params['resourceType'] = params['resource_type']
        if 'resource_id' in params:
            path_params['resourceId'] = params['resource_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['tokenAuth']

        return self.api_client.call_api('/v3/{workspaceId}/audits/events/zip/{resourceType}/{resourceId}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

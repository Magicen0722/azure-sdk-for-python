# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING

from azure.core.pipeline.transport._base import _format_url_section
from azure.core.rest import HttpRequest
from msrest import Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Optional

_SERIALIZER = Serializer()

# fmt: off

def build_get_by_id_request(
    schema_id,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Get a registered schema by its unique ID reference.

    Gets a registered schema by its unique ID.  Azure Schema Registry guarantees that ID is unique
    within a namespace.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :param schema_id: References specific schema in registry namespace.
    :type schema_id: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    api_version = "2020-09-01-preview"
    accept = "text/plain; charset=utf-8"
    # Construct URL
    url = kwargs.pop("template_url", '/$schemagroups/getSchemaById/{schema-id}')
    path_format_arguments = {
        'schema-id': _SERIALIZER.url("schema_id", schema_id, 'str'),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_query_id_by_content_request(
    group_name,  # type: str
    schema_name,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Get ID for existing schema.

    Gets the ID referencing an existing schema within the specified schema group, as matched by
    schema content comparison.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :param group_name: Schema group under which schema is registered.  Group's serialization type
     should match the serialization type specified in the request.
    :type group_name: str
    :param schema_name: Name of the registered schema.
    :type schema_name: str
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). String representation (UTF-8) of the registered schema.
    :paramtype content: any
    :keyword serialization_type: Serialization type for the schema being registered. "avro"
    :paramtype serialization_type: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    content_type = kwargs.pop('content_type', None)  # type: Optional[str]
    serialization_type = kwargs.pop('serialization_type')  # type: str

    api_version = "2020-09-01-preview"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/$schemagroups/{group-name}/schemas/{schema-name}')
    path_format_arguments = {
        'group-name': _SERIALIZER.url("group_name", group_name, 'str'),
        'schema-name': _SERIALIZER.url("schema_name", schema_name, 'str'),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Serialization-Type'] = _SERIALIZER.header("serialization_type", serialization_type, 'str')
    if content_type is not None:
        header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_register_request(
    group_name,  # type: str
    schema_name,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Register new schema.

    Register new schema. If schema of specified name does not exist in specified group, schema is
    created at version 1. If schema of specified name exists already in specified group, schema is
    created at latest version + 1.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :param group_name: Schema group under which schema should be registered.  Group's serialization
     type should match the serialization type specified in the request.
    :type group_name: str
    :param schema_name: Name of schema being registered.
    :type schema_name: str
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). String representation (UTF-8) of the schema being
     registered.
    :paramtype content: any
    :keyword serialization_type: Serialization type for the schema being registered. "avro"
    :paramtype serialization_type: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    content_type = kwargs.pop('content_type', None)  # type: Optional[str]
    serialization_type = kwargs.pop('serialization_type')  # type: str

    api_version = "2020-09-01-preview"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/$schemagroups/{group-name}/schemas/{schema-name}')
    path_format_arguments = {
        'group-name': _SERIALIZER.url("group_name", group_name, 'str'),
        'schema-name': _SERIALIZER.url("schema_name", schema_name, 'str'),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Serialization-Type'] = _SERIALIZER.header("serialization_type", serialization_type, 'str')
    if content_type is not None:
        header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )

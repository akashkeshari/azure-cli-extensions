# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class SqlDatabaseGetPropertiesResource(Model):
    """SqlDatabaseGetPropertiesResource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param id: Required. Name of the Cosmos DB SQL database
    :type id: str
    :ivar _rid: A system generated property. A unique identifier.
    :vartype _rid: str
    :ivar _ts: A system generated property that denotes the last updated
     timestamp of the resource.
    :vartype _ts: object
    :ivar _etag: A system generated property representing the resource etag
     required for optimistic concurrency control.
    :vartype _etag: str
    :param _colls: A system generated property that specified the addressable
     path of the collections resource.
    :type _colls: str
    :param _users: A system generated property that specifies the addressable
     path of the users resource.
    :type _users: str
    """

    _validation = {
        'id': {'required': True},
        '_rid': {'readonly': True},
        '_ts': {'readonly': True},
        '_etag': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        '_rid': {'key': '_rid', 'type': 'str'},
        '_ts': {'key': '_ts', 'type': 'object'},
        '_etag': {'key': '_etag', 'type': 'str'},
        '_colls': {'key': '_colls', 'type': 'str'},
        '_users': {'key': '_users', 'type': 'str'},
    }

    def __init__(self, *, id: str, _colls: str=None, _users: str=None, **kwargs) -> None:
        super(SqlDatabaseGetPropertiesResource, self).__init__(**kwargs)
        self.id = id
        self._rid = None
        self._ts = None
        self._etag = None
        self._colls = _colls
        self._users = _users

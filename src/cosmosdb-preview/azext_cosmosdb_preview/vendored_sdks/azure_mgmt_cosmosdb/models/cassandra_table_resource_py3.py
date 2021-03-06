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


class CassandraTableResource(Model):
    """Cosmos DB Cassandra table resource object.

    All required parameters must be populated in order to send to Azure.

    :param id: Required. Name of the Cosmos DB Cassandra table
    :type id: str
    :param default_ttl: Time to live of the Cosmos DB Cassandra table
    :type default_ttl: int
    :param schema: Schema of the Cosmos DB Cassandra table
    :type schema: ~azure.mgmt.cosmosdb.models.CassandraSchema
    :param analytical_storage_ttl: Analytical TTL.
    :type analytical_storage_ttl: int
    """

    _validation = {
        'id': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'default_ttl': {'key': 'defaultTtl', 'type': 'int'},
        'schema': {'key': 'schema', 'type': 'CassandraSchema'},
        'analytical_storage_ttl': {'key': 'analyticalStorageTtl', 'type': 'int'},
    }

    def __init__(self, *, id: str, default_ttl: int=None, schema=None, analytical_storage_ttl: int=None, **kwargs) -> None:
        super(CassandraTableResource, self).__init__(**kwargs)
        self.id = id
        self.default_ttl = default_ttl
        self.schema = schema
        self.analytical_storage_ttl = analytical_storage_ttl

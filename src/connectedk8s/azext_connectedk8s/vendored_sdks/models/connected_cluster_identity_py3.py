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


class ConnectedClusterIdentity(Model):
    """Identity for the connected cluster.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar principal_id: The principal id of connected cluster identity. This
     property will only be provided for a system assigned identity.
    :vartype principal_id: str
    :ivar tenant_id: The tenant id associated with the connected cluster. This
     property will only be provided for a system assigned identity.
    :vartype tenant_id: str
    :param type: Required. The type of identity used for the connected
     cluster. The type 'SystemAssigned, includes a system created identity. The
     type 'None' means no identity is assigned to the connected cluster.
     Possible values include: 'SystemAssigned', 'None'
    :type type: str or
     ~azure.mgmt.hybridkubernetes.models.ResourceIdentityType
    """

    _validation = {
        'principal_id': {'readonly': True},
        'tenant_id': {'readonly': True},
        'type': {'required': True},
    }

    _attribute_map = {
        'principal_id': {'key': 'principalId', 'type': 'str'},
        'tenant_id': {'key': 'tenantId', 'type': 'str'},
        'type': {'key': 'type', 'type': 'ResourceIdentityType'},
    }

    def __init__(self, *, type, **kwargs) -> None:
        super(ConnectedClusterIdentity, self).__init__(**kwargs)
        self.principal_id = None
        self.tenant_id = None
        self.type = type

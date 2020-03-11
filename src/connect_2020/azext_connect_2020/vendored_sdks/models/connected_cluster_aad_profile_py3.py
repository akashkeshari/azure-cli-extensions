# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ConnectedClusterAADProfile(Model):
    """ConnectedClusterAADProfile.

    All required parameters must be populated in order to send to Azure.

    :param tenant_id: Required. The aad tenant id which is configured on
     target K8s cluster
    :type tenant_id: str
    :param client_app_id: Required. The client app id configured on target K8
     cluster
    :type client_app_id: str
    :param server_app_id: Required. The server app id to access AD server
    :type server_app_id: str
    """

    _validation = {
        'tenant_id': {'required': True},
        'client_app_id': {'required': True},
        'server_app_id': {'required': True},
    }

    _attribute_map = {
        'tenant_id': {'key': 'tenantId', 'type': 'str'},
        'client_app_id': {'key': 'clientAppId', 'type': 'str'},
        'server_app_id': {'key': 'serverAppId', 'type': 'str'},
    }

    def __init__(self, *, tenant_id: str, client_app_id: str, server_app_id: str, **kwargs) -> None:
        super(ConnectedClusterAADProfile, self).__init__(**kwargs)
        self.tenant_id = tenant_id
        self.client_app_id = client_app_id
        self.server_app_id = server_app_id

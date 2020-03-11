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

from msrest.service_client import SDKClient
from msrest import Serializer, Deserializer
from msrestazure import AzureConfiguration
from .version import VERSION
from .operations.connected_cluster_operations import ConnectedClusterOperations
from .operations.operations import Operations
from . import models


class K8ConnectRPConfiguration(AzureConfiguration):
    """Configuration for K8ConnectRP
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: The ID of the subscription to which the kubernetes
     cluster is registered.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        if subscription_id is None:
            raise ValueError("Parameter 'subscription_id' must not be None.")
        if not base_url:
            base_url = 'https://management.azure.com'

        super(K8ConnectRPConfiguration, self).__init__(base_url)

        self.add_user_agent('azure-mgmt-hybridkubernetes/{}'.format(VERSION))
        self.add_user_agent('Azure-SDK-For-Python')

        self.credentials = credentials
        self.subscription_id = subscription_id


class K8ConnectRP(SDKClient):
    """Azure Connected Cluster Resource Provider API for adopting any Kubernetes Cluster

    :ivar config: Configuration for client.
    :vartype config: K8ConnectRPConfiguration

    :ivar connected_cluster: ConnectedCluster operations
    :vartype connected_cluster: azure.mgmt.hybridkubernetes.operations.ConnectedClusterOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.hybridkubernetes.operations.Operations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: The ID of the subscription to which the kubernetes
     cluster is registered.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        self.config = K8ConnectRPConfiguration(credentials, subscription_id, base_url)
        super(K8ConnectRP, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2019-09-01-privatepreview'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.connected_cluster = ConnectedClusterOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.operations = Operations(
            self._client, self.config, self._serialize, self._deserialize)

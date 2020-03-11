# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ConnectedClusterProxyProfile(Model):
    """ConnectedClusterProxyProfile.

    :param proxy_connection: Endpoint and authentication details to connect to
     proxy
    :type proxy_connection: str
    """

    _attribute_map = {
        'proxy_connection': {'key': 'proxyConnection', 'type': 'str'},
    }

    def __init__(self, *, proxy_connection: str=None, **kwargs) -> None:
        super(ConnectedClusterProxyProfile, self).__init__(**kwargs)
        self.proxy_connection = proxy_connection

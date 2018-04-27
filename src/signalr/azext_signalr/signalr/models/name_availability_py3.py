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


class NameAvailability(Model):
    """Result of the request to check name availability. It contains a flag and
    possible reason of failure.

    :param name_available: Indicates whether the name is available or not.
    :type name_available: bool
    :param reason: The reason of the availability. Required if name is not
     available.
    :type reason: str
    :param message: The message of the operation.
    :type message: str
    """

    _attribute_map = {
        'name_available': {'key': 'nameAvailable', 'type': 'bool'},
        'reason': {'key': 'reason', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(self, *, name_available: bool=None, reason: str=None, message: str=None, **kwargs) -> None:
        super(NameAvailability, self).__init__(**kwargs)
        self.name_available = name_available
        self.reason = reason
        self.message = message
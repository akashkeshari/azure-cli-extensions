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


class LocationData(Model):
    """Metadata pertaining to the geographic location of the resource.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. A canonical name for the geographic or physical
     location.
    :type name: str
    :param city: The city or locality where the resource is located.
    :type city: str
    :param district: The district, state, or province where the resource is
     located.
    :type district: str
    :param country_or_region: The country or region where the resource is
     located
    :type country_or_region: str
    """

    _validation = {
        'name': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'city': {'key': 'city', 'type': 'str'},
        'district': {'key': 'district', 'type': 'str'},
        'country_or_region': {'key': 'countryOrRegion', 'type': 'str'},
    }

    def __init__(self, *, name: str, city: str=None, district: str=None, country_or_region: str=None, **kwargs) -> None:
        super(LocationData, self).__init__(**kwargs)
        self.name = name
        self.city = city
        self.district = district
        self.country_or_region = country_or_region

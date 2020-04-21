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

from enum import Enum


class ResourceIdentityType(str, Enum):

    none = "None"
    system_assigned = "SystemAssigned"


class ProvisioningState(str, Enum):

    accepted = "Accepted"
    running = "Running"
    ready = "Ready"
    creating = "Creating"
    created = "Created"
    deleting = "Deleting"
    deleted = "Deleted"
    canceled = "Canceled"
    failed = "Failed"
    succeeded = "Succeeded"
    updating = "Updating"
<<<<<<< HEAD:src/connectedk8s/azext_connectedk8s/vendored_sdks/models/kubernetes_connect_rp_client_enums.py
    deleting = "Deleting"
    accepted = "Accepted"
=======
>>>>>>> master:src/databricks/azext_databricks/vendored_sdks/databricks/models/databricks_client_enums.py

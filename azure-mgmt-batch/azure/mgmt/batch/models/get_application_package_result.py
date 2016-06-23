# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft and contributors.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class GetApplicationPackageResult(Model):
    """Response to an ApplicationOperations.GetApplicationPackage request.

    :param id: The id of the application.
    :type id: str
    :param version: The version of the application package.
    :type version: str
    :param state: The current state of the application package. Possible
     values include: 'pending', 'active', 'unmapped'
    :type state: str or :class:`PackageState
     <azure.mgmt.batch.models.PackageState>`
    :param format: The format of the application package, if the package is
     active.
    :type format: str
    :param storage_url: The storage URL at which the application package is
     stored.
    :type storage_url: str
    :param storage_url_expiry: The UTC time at which the storage URL will
     expire.
    :type storage_url_expiry: datetime
    :param last_activation_time: The time at which the package was last
     activated, if the package is active.
    :type last_activation_time: datetime
    """ 

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'},
        'state': {'key': 'state', 'type': 'PackageState'},
        'format': {'key': 'format', 'type': 'str'},
        'storage_url': {'key': 'storageUrl', 'type': 'str'},
        'storage_url_expiry': {'key': 'storageUrlExpiry', 'type': 'iso-8601'},
        'last_activation_time': {'key': 'lastActivationTime', 'type': 'iso-8601'},
    }

    def __init__(self, id=None, version=None, state=None, format=None, storage_url=None, storage_url_expiry=None, last_activation_time=None):
        self.id = id
        self.version = version
        self.state = state
        self.format = format
        self.storage_url = storage_url
        self.storage_url_expiry = storage_url_expiry
        self.last_activation_time = last_activation_time

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


class AutoScaleRunError(Model):
    """An error that occurred when autoscaling a pool.

    :param code: An identifier for the error. Codes are invariant and are
     intended to be consumed programmatically.
    :type code: str
    :param message: A message describing the error, intended to be suitable
     for display in a user interface.
    :type message: str
    :param details: Additional details about the error.
    :type details: list[~azure.mgmt.batch.models.AutoScaleRunError]
    """

    _validation = {
        'code': {'required': True},
        'message': {'required': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'details': {'key': 'details', 'type': '[AutoScaleRunError]'},
    }

    def __init__(self, code, message, details=None):
        super(AutoScaleRunError, self).__init__()
        self.code = code
        self.message = message
        self.details = details

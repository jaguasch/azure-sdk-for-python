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

from msrest.pipeline import ClientRawResponse
import uuid

from .. import models


class CertificateOperations(object):
    """CertificateOperations operations.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An objec model deserializer.
    """

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer

        self.config = config

    def add(
            self, certificate, certificate_add_options=None, custom_headers=None, raw=False, **operation_config):
        """Adds a certificate to the specified account.

        :param certificate: The certificate to be added.
        :type certificate: :class:`CertificateAddParameter
         <azure.batch.models.CertificateAddParameter>`
        :param certificate_add_options: Additional parameters for the
         operation
        :type certificate_add_options: :class:`CertificateAddOptions
         <azure.batch.models.CertificateAddOptions>`
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :rtype: None
        :rtype: :class:`ClientRawResponse<msrest.pipeline.ClientRawResponse>`
         if raw=true
        """
        timeout = None
        if certificate_add_options is not None:
            timeout = certificate_add_options.timeout
        client_request_id = None
        if certificate_add_options is not None:
            client_request_id = certificate_add_options.client_request_id
        return_client_request_id = None
        if certificate_add_options is not None:
            return_client_request_id = certificate_add_options.return_client_request_id
        ocp_date = None
        if certificate_add_options is not None:
            ocp_date = certificate_add_options.ocp_date

        # Construct URL
        url = '/certificates'

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.config.api_version", self.config.api_version, 'str')
        if timeout is not None:
            query_parameters['timeout'] = self._serialize.query("timeout", timeout, 'int')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; odata=minimalmetadata; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')
        if client_request_id is not None:
            header_parameters['client-request-id'] = self._serialize.header("client_request_id", client_request_id, 'str')
        if return_client_request_id is not None:
            header_parameters['return-client-request-id'] = self._serialize.header("return_client_request_id", return_client_request_id, 'bool')
        if ocp_date is not None:
            header_parameters['ocp-date'] = self._serialize.header("ocp_date", ocp_date, 'rfc-1123')

        # Construct body
        body_content = self._serialize.body(certificate, 'CertificateAddParameter')

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, **operation_config)

        if response.status_code not in [201]:
            raise models.BatchErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            client_raw_response.add_headers({
                'client-request-id': 'str',
                'request-id': 'str',
                'ETag': 'str',
                'Last-Modified': 'rfc-1123',
                'DataServiceId': 'str',
            })
            return client_raw_response

    def list(
            self, certificate_list_options=None, custom_headers=None, raw=False, **operation_config):
        """Lists all of the certificates that have been added to the specified
        account.

        :param certificate_list_options: Additional parameters for the
         operation
        :type certificate_list_options: :class:`CertificateListOptions
         <azure.batch.models.CertificateListOptions>`
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :rtype: :class:`CertificatePaged
         <azure.batch.models.CertificatePaged>`
        """
        filter = None
        if certificate_list_options is not None:
            filter = certificate_list_options.filter
        select = None
        if certificate_list_options is not None:
            select = certificate_list_options.select
        max_results = None
        if certificate_list_options is not None:
            max_results = certificate_list_options.max_results
        timeout = None
        if certificate_list_options is not None:
            timeout = certificate_list_options.timeout
        client_request_id = None
        if certificate_list_options is not None:
            client_request_id = certificate_list_options.client_request_id
        return_client_request_id = None
        if certificate_list_options is not None:
            return_client_request_id = certificate_list_options.return_client_request_id
        ocp_date = None
        if certificate_list_options is not None:
            ocp_date = certificate_list_options.ocp_date

        def internal_paging(next_link=None, raw=False):

            if not next_link:
                # Construct URL
                url = '/certificates'

                # Construct parameters
                query_parameters = {}
                query_parameters['api-version'] = self._serialize.query("self.config.api_version", self.config.api_version, 'str')
                if filter is not None:
                    query_parameters['$filter'] = self._serialize.query("filter", filter, 'str')
                if select is not None:
                    query_parameters['$select'] = self._serialize.query("select", select, 'str')
                if max_results is not None:
                    query_parameters['maxresults'] = self._serialize.query("max_results", max_results, 'int')
                if timeout is not None:
                    query_parameters['timeout'] = self._serialize.query("timeout", timeout, 'int')

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Content-Type'] = 'application/json; odata=minimalmetadata; charset=utf-8'
            if self.config.generate_client_request_id:
                header_parameters['client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')
            if client_request_id is not None:
                header_parameters['client-request-id'] = self._serialize.header("client_request_id", client_request_id, 'str')
            if return_client_request_id is not None:
                header_parameters['return-client-request-id'] = self._serialize.header("return_client_request_id", return_client_request_id, 'bool')
            if ocp_date is not None:
                header_parameters['ocp-date'] = self._serialize.header("ocp_date", ocp_date, 'rfc-1123')

            # Construct and send request
            request = self._client.get(url, query_parameters)
            response = self._client.send(
                request, header_parameters, **operation_config)

            if response.status_code not in [200]:
                raise models.BatchErrorException(self._deserialize, response)

            return response

        # Deserialize response
        deserialized = models.CertificatePaged(internal_paging, self._deserialize.dependencies)

        if raw:
            header_dict = {}
            client_raw_response = models.CertificatePaged(internal_paging, self._deserialize.dependencies, header_dict)
            return client_raw_response

        return deserialized

    def cancel_deletion(
            self, thumbprint_algorithm, thumbprint, certificate_cancel_deletion_options=None, custom_headers=None, raw=False, **operation_config):
        """Cancels a failed deletion of a certificate from the specified account.

        :param thumbprint_algorithm: The algorithm used to derive the
         thumbprint parameter. This must be sha1.
        :type thumbprint_algorithm: str
        :param thumbprint: The thumbprint of the certificate being deleted.
        :type thumbprint: str
        :param certificate_cancel_deletion_options: Additional parameters for
         the operation
        :type certificate_cancel_deletion_options:
         :class:`CertificateCancelDeletionOptions
         <azure.batch.models.CertificateCancelDeletionOptions>`
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :rtype: None
        :rtype: :class:`ClientRawResponse<msrest.pipeline.ClientRawResponse>`
         if raw=true
        """
        timeout = None
        if certificate_cancel_deletion_options is not None:
            timeout = certificate_cancel_deletion_options.timeout
        client_request_id = None
        if certificate_cancel_deletion_options is not None:
            client_request_id = certificate_cancel_deletion_options.client_request_id
        return_client_request_id = None
        if certificate_cancel_deletion_options is not None:
            return_client_request_id = certificate_cancel_deletion_options.return_client_request_id
        ocp_date = None
        if certificate_cancel_deletion_options is not None:
            ocp_date = certificate_cancel_deletion_options.ocp_date

        # Construct URL
        url = '/certificates(thumbprintAlgorithm={thumbprintAlgorithm},thumbprint={thumbprint})/canceldelete'
        path_format_arguments = {
            'thumbprintAlgorithm': self._serialize.url("thumbprint_algorithm", thumbprint_algorithm, 'str'),
            'thumbprint': self._serialize.url("thumbprint", thumbprint, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.config.api_version", self.config.api_version, 'str')
        if timeout is not None:
            query_parameters['timeout'] = self._serialize.query("timeout", timeout, 'int')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; odata=minimalmetadata; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')
        if client_request_id is not None:
            header_parameters['client-request-id'] = self._serialize.header("client_request_id", client_request_id, 'str')
        if return_client_request_id is not None:
            header_parameters['return-client-request-id'] = self._serialize.header("return_client_request_id", return_client_request_id, 'bool')
        if ocp_date is not None:
            header_parameters['ocp-date'] = self._serialize.header("ocp_date", ocp_date, 'rfc-1123')

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(request, header_parameters, **operation_config)

        if response.status_code not in [204]:
            raise models.BatchErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            client_raw_response.add_headers({
                'client-request-id': 'str',
                'request-id': 'str',
                'ETag': 'str',
                'Last-Modified': 'rfc-1123',
                'DataServiceId': 'str',
            })
            return client_raw_response

    def delete(
            self, thumbprint_algorithm, thumbprint, certificate_delete_options=None, custom_headers=None, raw=False, **operation_config):
        """Deletes a certificate from the specified account.

        :param thumbprint_algorithm: The algorithm used to derive the
         thumbprint parameter. This must be sha1.
        :type thumbprint_algorithm: str
        :param thumbprint: The thumbprint of the certificate to be deleted.
        :type thumbprint: str
        :param certificate_delete_options: Additional parameters for the
         operation
        :type certificate_delete_options: :class:`CertificateDeleteOptions
         <azure.batch.models.CertificateDeleteOptions>`
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :rtype: None
        :rtype: :class:`ClientRawResponse<msrest.pipeline.ClientRawResponse>`
         if raw=true
        """
        timeout = None
        if certificate_delete_options is not None:
            timeout = certificate_delete_options.timeout
        client_request_id = None
        if certificate_delete_options is not None:
            client_request_id = certificate_delete_options.client_request_id
        return_client_request_id = None
        if certificate_delete_options is not None:
            return_client_request_id = certificate_delete_options.return_client_request_id
        ocp_date = None
        if certificate_delete_options is not None:
            ocp_date = certificate_delete_options.ocp_date

        # Construct URL
        url = '/certificates(thumbprintAlgorithm={thumbprintAlgorithm},thumbprint={thumbprint})'
        path_format_arguments = {
            'thumbprintAlgorithm': self._serialize.url("thumbprint_algorithm", thumbprint_algorithm, 'str'),
            'thumbprint': self._serialize.url("thumbprint", thumbprint, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.config.api_version", self.config.api_version, 'str')
        if timeout is not None:
            query_parameters['timeout'] = self._serialize.query("timeout", timeout, 'int')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; odata=minimalmetadata; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')
        if client_request_id is not None:
            header_parameters['client-request-id'] = self._serialize.header("client_request_id", client_request_id, 'str')
        if return_client_request_id is not None:
            header_parameters['return-client-request-id'] = self._serialize.header("return_client_request_id", return_client_request_id, 'bool')
        if ocp_date is not None:
            header_parameters['ocp-date'] = self._serialize.header("ocp_date", ocp_date, 'rfc-1123')

        # Construct and send request
        request = self._client.delete(url, query_parameters)
        response = self._client.send(request, header_parameters, **operation_config)

        if response.status_code not in [202]:
            raise models.BatchErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            client_raw_response.add_headers({
                'client-request-id': 'str',
                'request-id': 'str',
                'ETag': 'str',
                'Last-Modified': 'rfc-1123',
            })
            return client_raw_response

    def get(
            self, thumbprint_algorithm, thumbprint, certificate_get_options=None, custom_headers=None, raw=False, **operation_config):
        """Gets information about the specified certificate.

        :param thumbprint_algorithm: The algorithm used to derive the
         thumbprint parameter. This must be sha1.
        :type thumbprint_algorithm: str
        :param thumbprint: The thumbprint of the certificate to get.
        :type thumbprint: str
        :param certificate_get_options: Additional parameters for the
         operation
        :type certificate_get_options: :class:`CertificateGetOptions
         <azure.batch.models.CertificateGetOptions>`
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :rtype: :class:`Certificate <azure.batch.models.Certificate>`
        :rtype: :class:`ClientRawResponse<msrest.pipeline.ClientRawResponse>`
         if raw=true
        """
        select = None
        if certificate_get_options is not None:
            select = certificate_get_options.select
        timeout = None
        if certificate_get_options is not None:
            timeout = certificate_get_options.timeout
        client_request_id = None
        if certificate_get_options is not None:
            client_request_id = certificate_get_options.client_request_id
        return_client_request_id = None
        if certificate_get_options is not None:
            return_client_request_id = certificate_get_options.return_client_request_id
        ocp_date = None
        if certificate_get_options is not None:
            ocp_date = certificate_get_options.ocp_date

        # Construct URL
        url = '/certificates(thumbprintAlgorithm={thumbprintAlgorithm},thumbprint={thumbprint})'
        path_format_arguments = {
            'thumbprintAlgorithm': self._serialize.url("thumbprint_algorithm", thumbprint_algorithm, 'str'),
            'thumbprint': self._serialize.url("thumbprint", thumbprint, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.config.api_version", self.config.api_version, 'str')
        if select is not None:
            query_parameters['$select'] = self._serialize.query("select", select, 'str')
        if timeout is not None:
            query_parameters['timeout'] = self._serialize.query("timeout", timeout, 'int')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; odata=minimalmetadata; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')
        if client_request_id is not None:
            header_parameters['client-request-id'] = self._serialize.header("client_request_id", client_request_id, 'str')
        if return_client_request_id is not None:
            header_parameters['return-client-request-id'] = self._serialize.header("return_client_request_id", return_client_request_id, 'bool')
        if ocp_date is not None:
            header_parameters['ocp-date'] = self._serialize.header("ocp_date", ocp_date, 'rfc-1123')

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, **operation_config)

        if response.status_code not in [200]:
            raise models.BatchErrorException(self._deserialize, response)

        deserialized = None
        header_dict = {}

        if response.status_code == 200:
            deserialized = self._deserialize('Certificate', response)
            header_dict = {
                'client-request-id': 'str',
                'request-id': 'str',
                'ETag': 'str',
                'Last-Modified': 'rfc-1123',
            }

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            client_raw_response.add_headers(header_dict)
            return client_raw_response

        return deserialized

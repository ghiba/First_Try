#!/usr/bin/python

# Copyright (c) 2018 Cisco Systems, Inc.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)


ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'network'}

DOCUMENTATION = """
---
module: ftd_certificate
short_description: Manages Certificate objects on Cisco FTD devices
version_added: "2.7"
author: "Cisco Systems, Inc."
options:
  operation:
    description:
      - Specified the name of the operation to execute in the task.
    required: true
  register_as:
    description:
      - Specifies Ansible fact name that is used to register received response from the FTD device.
  cert
    description:
      - PEM formatted X.509v3 certificate.
  certType
    description:
      - An mandatory enum value that specifies the type of internal certificate. Values can be one of the following. <br> UPLOAD - Certificate is already defined and certificate and private string will be uploaded. <br> SELFSIGNED - Generate an internal certificate using the provided values. <br>
  id
    description:
      - A unique string identifier assigned by the system when the object is created. No assumption can be made on the format or content of this identifier. The identifier must be provided whenever attempting to modify/delete (or reference) an existing object.<br>Field level constraints: must match pattern ^((?!;).)*$, cannot have HTML. (Note: Additional constraints might exist)
  isSystemDefined
    description:
      - A boolean value, TRUE and FALSE (the default). The TRUE value indicates that certificate is created by system and cannot be deleted. FALSE indicates that the certificate can be deleted.
  issuerCommonName
    description:
      - Common Name, typically product name/brand, of the Authority (issuer) that signed and issued the certificate.  This is automatically extracted from the uploaded certificate.<br>Field level constraints: cannot have HTML, must match pattern ^((?!;).)*$. (Note: Additional constraints might exist)
  issuerCountry
    description:
      - An ISO3166 two character country code of the Authority (issuer) that signed and issued the certificate.  This is automatically extracted from the uploaded certificate.<br>Field level constraints: cannot have HTML, must match pattern ^((?!;).)*$. (Note: Additional constraints might exist)
  issuerLocality
    description:
      - Locality, city name, of the Authority (issuer) that signed and issued the certificate. This is automatically extracted from the uploaded certificate.<br>Field level constraints: cannot have HTML, must match pattern ^((?!;).)*$. (Note: Additional constraints might exist)
  issuerOrganization
    description:
      - Organization, company name, of the Authority (issuer) that signed and issued the certificate. This is automatically extracted from the uploaded certificate.<br>Field level constraints: cannot have HTML, must match pattern ^((?!;).)*$. (Note: Additional constraints might exist)
  issuerOrganizationUnit
    description:
      - The Organization Unit, division or unit, of the Authority (issuer) that signed and issued the certificate. This is automatically extracted from the uploaded certificate.<br>Field level constraints: cannot have HTML, must match pattern ^((?!;).)*$. (Note: Additional constraints might exist)
  issuerState
    description:
      - State or the province of the Authority (issuer) that signed and issued the certificate. This is automatically extracted from the uploaded certificate.<br>Field level constraints: cannot have HTML, must match pattern ^((?!;).)*$. (Note: Additional constraints might exist)
  name
    description:
      - A mandatory UTF string containing the name for the certificate. The string can be up to 128 characters. The name is used in the configuration as an object name only, it is not part of the certificate itself.
  passPhrase
    description:
      - Password used for encrypted private key. Encrypted keys are not supported yet.<br>Field level constraints: cannot have HTML. (Note: Additional constraints might exist)
  privateKey
    description:
      - PEM formatted private key. Only unencrypted keys are supported.
  subjectCommonName
    description:
      - An Unicode alphanumeric string containing the Common Name, typically product name/brand, of the entity (subject) being certified or authenticated in the given certificate. This is mandatory input value for Self-Signed certificate and extracted from an uploaded certificate.<br>Field level constraints: cannot have HTML, must match pattern ^((?!;).)*$. (Note: Additional constraints might exist)
  subjectCommonName
    description:
      - Common Name, typically product name/brand, of the entity (subject) being certified or authenticated in the given certificate.  This is automatically extracted from the uploaded certificate.<br>Field level constraints: cannot have HTML, must match pattern ^((?!;).)*$. (Note: Additional constraints might exist)
  subjectCountry
    description:
      - An ISO3166 two character country code of the Authority (issuer) that signed and issued the certificate. This is mandatory input value for Self-Signed certificate and extracted from an uploaded certificate.<br>Field level constraints: cannot have HTML, must match pattern ^((?!;).)*$. (Note: Additional constraints might exist)
  subjectCountry
    description:
      - An ISO3166 two character country code of the entity (subject) being certified or authenticated in the given certificate. This is automatically extracted from the uploaded certificate.<br>Field level constraints: cannot have HTML, must match pattern ^((?!;).)*$. (Note: Additional constraints might exist)
  subjectDistinguishedName
    description:
      - A DN (Distinguished Name) defining the entity (subject) being certified or authenticated in the given certificate. For a root certificate the issuer and subject will be the same DN.  This is automatically extracted from the uploaded certificate.<br>Field level constraints: cannot have HTML, must match pattern ^((?!;).)*$. (Note: Additional constraints might exist)
  subjectLocality
    description:
      - An Unicode alphanumeric string containing the locality, city name, of the entity (subject) being certified or authenticated in the given certificate. This is mandatory input value for Self-Signed certificate and extracted from an uploaded certificate.<br>Field level constraints: cannot have HTML, must match pattern ^((?!;).)*$. (Note: Additional constraints might exist)
  subjectLocality
    description:
      - Locality, city name, of the entity (subject) being certified or authenticated in the given certificate. This is automatically extracted from the uploaded certificate.<br>Field level constraints: cannot have HTML, must match pattern ^((?!;).)*$. (Note: Additional constraints might exist)
  subjectOrganization
    description:
      - An Unicode alphanumeric string containing the organization, company name, of the entity (subject) being certified or authenticated in the given certificate. This is mandatory input value for Self-Signed certificate and extracted from an uploaded certificate.<br>Field level constraints: cannot have HTML, must match pattern ^((?!;).)*$. (Note: Additional constraints might exist)
  subjectOrganization
    description:
      - Organization, company name, of the entity (subject) being certified or authenticated in the given certificate.  This is automatically extracted from the uploaded certificate.<br>Field level constraints: cannot have HTML, must match pattern ^((?!;).)*$. (Note: Additional constraints might exist)
  subjectOrganizationUnit
    description:
      - An Unicode alphanumeric string containing the Organization Unit, division or unit, of the entity (subject) being certified or authenticated in the given certificate. This is mandatory input value for Self-Signed certificate and extracted from an uploaded certificate.<br>Field level constraints: cannot have HTML, must match pattern ^((?!;).)*$. (Note: Additional constraints might exist)
  subjectOrganizationUnit
    description:
      - The Organization Unit, division or unit, of the entity (subject) being certified or authenticated in the given certificate. This is automatically extracted from the uploaded certificate.<br>Field level constraints: cannot have HTML, must match pattern ^((?!;).)*$. (Note: Additional constraints might exist)
  subjectState
    description:
      - An Unicode alphanumeric string containing the state or the province of the entity (subject) being certified or authenticated in the given certificate. This is mandatory input value for Self-Signed certificate and extracted from an uploaded certificate.<br>Field level constraints: cannot have HTML, must match pattern ^((?!;).)*$. (Note: Additional constraints might exist)
  subjectState
    description:
      - State or the province of the entity (subject) being certified or authenticated in the given certificate.  This is automatically extracted from the uploaded certificate.<br>Field level constraints: cannot have HTML, must match pattern ^((?!;).)*$. (Note: Additional constraints might exist)
  type
    description:
      - A UTF8 string, all letters lower-case, that represents the class-type. This corresponds to the class name.
  validityEndDate
    description:
      - This is set to five years in UTC format from the current date for Self-Signed certificate.<br>Field level constraints: cannot have HTML, must match pattern ^((?!;).)*$. (Note: Additional constraints might exist)
  validityEndDate
    description:
      - UTC formatted end or expiry date for the given certificate. This is automatically extracted from the uploaded certificate.<br>Field level constraints: cannot have HTML, must match pattern ^((?!;).)*$. (Note: Additional constraints might exist)
  validityStartDate
    description:
      - This is current date in UTC format for Self-Signed certificate.<br>Field level constraints: cannot have HTML, must match pattern ^((?!;).)*$. (Note: Additional constraints might exist)
  validityStartDate
    description:
      - UTC formatted begin date, for the given certificate. This is automatically extracted from the uploaded certificate.<br>Field level constraints: cannot have HTML, must match pattern ^((?!;).)*$. (Note: Additional constraints might exist)
  version
    description:
      - A unique string version assigned by the system when the object is created or modified. No assumption can be made on the format or content of this identifier. The identifier must be provided whenever attempting to modify/delete an existing object. As the version will change every time the object is modified, the value provided in this identifier must match exactly what is present in the system or the request will be rejected.

extends_documentation_fragment: ftd
"""

EXAMPLES = """
"""

RETURN = """
response:
  description: HTTP response returned from the API call.
  returned: success
  type: dict
error_code:
  description: HTTP error code returned from the server.
  returned: error
  type: int
msg:
  description: Error message returned from the server.
  returned: error
  type: dict
"""
import json

from ansible.module_utils.authorization import retry_on_token_expiration
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.http import construct_url, base_headers, iterate_over_pageable_resource
from ansible.module_utils.misc import dict_subset, construct_module_result, copy_identity_properties
from ansible.module_utils.six.moves.urllib.error import HTTPError
from ansible.module_utils.urls import open_url


class CertificateResource(object):
    
    @staticmethod
    @retry_on_token_expiration
    def addExternalCACertificate(params):
        body_params = dict_subset(params, ['version', 'name', 'cert', 'privateKey', 'passPhrase', 'issuerCommonName', 'issuerCountry', 'issuerLocality', 'issuerOrganization', 'issuerOrganizationUnit', 'issuerState', 'subjectCommonName', 'subjectCountry', 'subjectDistinguishedName', 'subjectLocality', 'subjectOrganization', 'subjectOrganizationUnit', 'subjectState', 'validityStartDate', 'validityEndDate', 'isSystemDefined', 'id', 'type'])

        url = construct_url(params['hostname'], '/object/externalcacertificates')
        request_params = dict(
            headers=base_headers(params['access_token']),
            method='POST',
            data=json.dumps(body_params)
        )

        response = open_url(url, **request_params).read()
        return json.loads(response) if response else response

    @staticmethod
    @retry_on_token_expiration
    def addExternalCertificate(params):
        body_params = dict_subset(params, ['version', 'name', 'cert', 'privateKey', 'passPhrase', 'issuerCommonName', 'issuerCountry', 'issuerLocality', 'issuerOrganization', 'issuerOrganizationUnit', 'issuerState', 'subjectCommonName', 'subjectCountry', 'subjectDistinguishedName', 'subjectLocality', 'subjectOrganization', 'subjectOrganizationUnit', 'subjectState', 'validityStartDate', 'validityEndDate', 'isSystemDefined', 'id', 'type'])

        url = construct_url(params['hostname'], '/object/externalcertificates')
        request_params = dict(
            headers=base_headers(params['access_token']),
            method='POST',
            data=json.dumps(body_params)
        )

        response = open_url(url, **request_params).read()
        return json.loads(response) if response else response

    @staticmethod
    @retry_on_token_expiration
    def addInternalCACertificate(params):
        body_params = dict_subset(params, ['version', 'name', 'cert', 'privateKey', 'passPhrase', 'issuerCommonName', 'issuerCountry', 'issuerLocality', 'issuerOrganization', 'issuerOrganizationUnit', 'issuerState', 'subjectCommonName', 'subjectCountry', 'subjectDistinguishedName', 'subjectLocality', 'subjectOrganization', 'subjectOrganizationUnit', 'subjectState', 'validityStartDate', 'validityEndDate', 'isSystemDefined', 'certType', 'id', 'type'])

        url = construct_url(params['hostname'], '/object/internalcacertificates')
        request_params = dict(
            headers=base_headers(params['access_token']),
            method='POST',
            data=json.dumps(body_params)
        )

        response = open_url(url, **request_params).read()
        return json.loads(response) if response else response

    @staticmethod
    @retry_on_token_expiration
    def addInternalCertificate(params):
        body_params = dict_subset(params, ['version', 'name', 'cert', 'privateKey', 'passPhrase', 'issuerCommonName', 'issuerCountry', 'issuerLocality', 'issuerOrganization', 'issuerOrganizationUnit', 'issuerState', 'subjectCommonName', 'subjectCountry', 'subjectDistinguishedName', 'subjectLocality', 'subjectOrganization', 'subjectOrganizationUnit', 'subjectState', 'validityStartDate', 'validityEndDate', 'isSystemDefined', 'certType', 'id', 'type'])

        url = construct_url(params['hostname'], '/object/internalcertificates')
        request_params = dict(
            headers=base_headers(params['access_token']),
            method='POST',
            data=json.dumps(body_params)
        )

        response = open_url(url, **request_params).read()
        return json.loads(response) if response else response

    @staticmethod
    @retry_on_token_expiration
    def deleteExternalCACertificate(params):
        path_params = dict_subset(params, ['objId'])

        url = construct_url(params['hostname'], '/object/externalcacertificates/{objId}', path_params=path_params)
        request_params = dict(
            headers=base_headers(params['access_token']),
            method='DELETE',
        )

        response = open_url(url, **request_params).read()
        return json.loads(response) if response else response

    @staticmethod
    @retry_on_token_expiration
    def deleteExternalCertificate(params):
        path_params = dict_subset(params, ['objId'])

        url = construct_url(params['hostname'], '/object/externalcertificates/{objId}', path_params=path_params)
        request_params = dict(
            headers=base_headers(params['access_token']),
            method='DELETE',
        )

        response = open_url(url, **request_params).read()
        return json.loads(response) if response else response

    @staticmethod
    @retry_on_token_expiration
    def deleteInternalCACertificate(params):
        path_params = dict_subset(params, ['objId'])

        url = construct_url(params['hostname'], '/object/internalcacertificates/{objId}', path_params=path_params)
        request_params = dict(
            headers=base_headers(params['access_token']),
            method='DELETE',
        )

        response = open_url(url, **request_params).read()
        return json.loads(response) if response else response

    @staticmethod
    @retry_on_token_expiration
    def deleteInternalCertificate(params):
        path_params = dict_subset(params, ['objId'])

        url = construct_url(params['hostname'], '/object/internalcertificates/{objId}', path_params=path_params)
        request_params = dict(
            headers=base_headers(params['access_token']),
            method='DELETE',
        )

        response = open_url(url, **request_params).read()
        return json.loads(response) if response else response

    @staticmethod
    @retry_on_token_expiration
    def editExternalCACertificate(params):
        path_params = dict_subset(params, ['objId'])
        body_params = dict_subset(params, ['version', 'name', 'cert', 'privateKey', 'passPhrase', 'issuerCommonName', 'issuerCountry', 'issuerLocality', 'issuerOrganization', 'issuerOrganizationUnit', 'issuerState', 'subjectCommonName', 'subjectCountry', 'subjectDistinguishedName', 'subjectLocality', 'subjectOrganization', 'subjectOrganizationUnit', 'subjectState', 'validityStartDate', 'validityEndDate', 'isSystemDefined', 'id', 'type'])

        url = construct_url(params['hostname'], '/object/externalcacertificates/{objId}', path_params=path_params)
        request_params = dict(
            headers=base_headers(params['access_token']),
            method='PUT',
            data=json.dumps(body_params)
        )

        response = open_url(url, **request_params).read()
        return json.loads(response) if response else response

    @staticmethod
    @retry_on_token_expiration
    def editExternalCertificate(params):
        path_params = dict_subset(params, ['objId'])
        body_params = dict_subset(params, ['version', 'name', 'cert', 'privateKey', 'passPhrase', 'issuerCommonName', 'issuerCountry', 'issuerLocality', 'issuerOrganization', 'issuerOrganizationUnit', 'issuerState', 'subjectCommonName', 'subjectCountry', 'subjectDistinguishedName', 'subjectLocality', 'subjectOrganization', 'subjectOrganizationUnit', 'subjectState', 'validityStartDate', 'validityEndDate', 'isSystemDefined', 'id', 'type'])

        url = construct_url(params['hostname'], '/object/externalcertificates/{objId}', path_params=path_params)
        request_params = dict(
            headers=base_headers(params['access_token']),
            method='PUT',
            data=json.dumps(body_params)
        )

        response = open_url(url, **request_params).read()
        return json.loads(response) if response else response

    @staticmethod
    @retry_on_token_expiration
    def editInternalCACertificate(params):
        path_params = dict_subset(params, ['objId'])
        body_params = dict_subset(params, ['version', 'name', 'cert', 'privateKey', 'passPhrase', 'issuerCommonName', 'issuerCountry', 'issuerLocality', 'issuerOrganization', 'issuerOrganizationUnit', 'issuerState', 'subjectCommonName', 'subjectCountry', 'subjectDistinguishedName', 'subjectLocality', 'subjectOrganization', 'subjectOrganizationUnit', 'subjectState', 'validityStartDate', 'validityEndDate', 'isSystemDefined', 'certType', 'id', 'type'])

        url = construct_url(params['hostname'], '/object/internalcacertificates/{objId}', path_params=path_params)
        request_params = dict(
            headers=base_headers(params['access_token']),
            method='PUT',
            data=json.dumps(body_params)
        )

        response = open_url(url, **request_params).read()
        return json.loads(response) if response else response

    @staticmethod
    @retry_on_token_expiration
    def editInternalCertificate(params):
        path_params = dict_subset(params, ['objId'])
        body_params = dict_subset(params, ['version', 'name', 'cert', 'privateKey', 'passPhrase', 'issuerCommonName', 'issuerCountry', 'issuerLocality', 'issuerOrganization', 'issuerOrganizationUnit', 'issuerState', 'subjectCommonName', 'subjectCountry', 'subjectDistinguishedName', 'subjectLocality', 'subjectOrganization', 'subjectOrganizationUnit', 'subjectState', 'validityStartDate', 'validityEndDate', 'isSystemDefined', 'certType', 'id', 'type'])

        url = construct_url(params['hostname'], '/object/internalcertificates/{objId}', path_params=path_params)
        request_params = dict(
            headers=base_headers(params['access_token']),
            method='PUT',
            data=json.dumps(body_params)
        )

        response = open_url(url, **request_params).read()
        return json.loads(response) if response else response

    @staticmethod
    @retry_on_token_expiration
    def getExternalCACertificate(params):
        path_params = dict_subset(params, ['objId'])

        url = construct_url(params['hostname'], '/object/externalcacertificates/{objId}', path_params=path_params)
        request_params = dict(
            headers=base_headers(params['access_token']),
            method='GET',
        )

        response = open_url(url, **request_params).read()
        return json.loads(response) if response else response

    @staticmethod
    @retry_on_token_expiration
    def getExternalCertificate(params):
        path_params = dict_subset(params, ['objId'])

        url = construct_url(params['hostname'], '/object/externalcertificates/{objId}', path_params=path_params)
        request_params = dict(
            headers=base_headers(params['access_token']),
            method='GET',
        )

        response = open_url(url, **request_params).read()
        return json.loads(response) if response else response

    @staticmethod
    @retry_on_token_expiration
    def getInternalCACertificate(params):
        path_params = dict_subset(params, ['objId'])

        url = construct_url(params['hostname'], '/object/internalcacertificates/{objId}', path_params=path_params)
        request_params = dict(
            headers=base_headers(params['access_token']),
            method='GET',
        )

        response = open_url(url, **request_params).read()
        return json.loads(response) if response else response

    @staticmethod
    @retry_on_token_expiration
    def getInternalCertificate(params):
        path_params = dict_subset(params, ['objId'])

        url = construct_url(params['hostname'], '/object/internalcertificates/{objId}', path_params=path_params)
        request_params = dict(
            headers=base_headers(params['access_token']),
            method='GET',
        )

        response = open_url(url, **request_params).read()
        return json.loads(response) if response else response


def main():
    fields = dict(
        hostname=dict(type='str', required=True),
        access_token=dict(type='str', required=True),
        refresh_token=dict(type='str', required=True),

        operation=dict(choices=['addExternalCACertificate', 'addExternalCertificate', 'addInternalCACertificate', 'addInternalCertificate', 'deleteExternalCACertificate', 'deleteExternalCertificate', 'deleteInternalCACertificate', 'deleteInternalCertificate', 'editExternalCACertificate', 'editExternalCertificate', 'editInternalCACertificate', 'editInternalCertificate', 'getExternalCACertificate', 'getExternalCertificate', 'getInternalCACertificate', 'getInternalCertificate'], required=True),
        register_as=dict(type='str'),

        cert=dict(type='str'),
        certType=dict(type='str'),
        id=dict(type='str'),
        isSystemDefined=dict(type='bool'),
        issuerCommonName=dict(type='str'),
        issuerCountry=dict(type='str'),
        issuerLocality=dict(type='str'),
        issuerOrganization=dict(type='str'),
        issuerOrganizationUnit=dict(type='str'),
        issuerState=dict(type='str'),
        name=dict(type='str'),
        objId=dict(type='str'),
        passPhrase=dict(type='str'),
        privateKey=dict(type='str'),
        subjectCommonName=dict(type='str'),
        subjectCommonName=dict(type='str'),
        subjectCountry=dict(type='str'),
        subjectCountry=dict(type='str'),
        subjectDistinguishedName=dict(type='str'),
        subjectLocality=dict(type='str'),
        subjectLocality=dict(type='str'),
        subjectOrganization=dict(type='str'),
        subjectOrganization=dict(type='str'),
        subjectOrganizationUnit=dict(type='str'),
        subjectOrganizationUnit=dict(type='str'),
        subjectState=dict(type='str'),
        subjectState=dict(type='str'),
        type=dict(type='str'),
        validityEndDate=dict(type='str'),
        validityEndDate=dict(type='str'),
        validityStartDate=dict(type='str'),
        validityStartDate=dict(type='str'),
        version=dict(type='str'),
    )

    module = AnsibleModule(argument_spec=fields)
    params = module.params

    try:
        method_to_call = getattr(CertificateResource, params['operation'])
        response = method_to_call(params)
        result = construct_module_result(response, params)
        module.exit_json(**result)
    except HTTPError as e:
        err_msg = e.read()
        module.fail_json(changed=False, msg=json.loads(err_msg) if err_msg else {}, error_code=e.code)
    except Exception as e:
        module.fail_json(changed=False, msg=str(e))


if __name__ == '__main__':
    main()
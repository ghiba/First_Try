#!/usr/bin/python

# Copyright (c) 2018 Cisco Systems, Inc.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)


ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'network'}

DOCUMENTATION = """
---
module: ftd_ikev_one_policy
short_description: Manages IkevOnePolicy objects on Cisco FTD devices
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
  authenticationType
    description:
      - An enum value that specifies how the peers in the VPN are authenticated. Possible values are:<br>PRE_SHARE - The peers use a single pre-shared key. Specify the key string in the SToSConnectionProfile object.<br>RSA_SIG - Not supported.<br>Field level constraints: cannot be null. (Note: Additional constraints might exist)
  cryptoRestricted
    description:
      - A system-provided Boolean value, TRUE or FALSE. The TRUE value indicates that the policy uses strong cryptography, which is controlled by export regulations. A device must be registered export-controlled functionality to use a strong encryption policy.
  enabled
    description:
      - A mandatory Boolean value, TRUE or FALSE (the default). The TRUE value enables the policy, which means remote peers can use it when negotiating a site-to-site VPN connection. FALSE indicates that although the policy is defined, remote peers cannot negotiate connections based on the policy.<br>Field level constraints: cannot be null. (Note: Additional constraints might exist)
  encryptionType
    description:
      - An enum value that specifies the encryption algorithm used to establish the Phase 1 security association (SA) for protecting Phase 2 negotiations. Possible values are, in order of strength:<br>DES - Data Encryption Standard, which encrypts using 56-bit keys, is a symmetric secret-key block algorithm.<br>THREE_DES - Triple DES, which encrypts three times using 56-bit keys.<br>AES - Advanced Encryption Standard is a symmetric cipher algorithm. AES uses 128-bit keys.<br>AES192 - An Advanced Encryption Standard algorithm that uses 192-bit keys.<br>AES256 - An Advanced Encryption Standard algorithm that uses 256-bit keys.<br>Field level constraints: cannot be null. (Note: Additional constraints might exist)
  filter
    description:
      - The criteria used to filter the models you are requesting. It should have the following format: {field}{operator}{value}[;{field}{operator}{value}]. Supported operators are: "!"(not equals), ":"(equals), "<"(null), "~"(similar), ">"(null). Supported fields are: "name".
  groupType
    description:
      - An enum value that specifies the Diffie-Hellman group to use for deriving a shared secret between the two IPsec peers without transmitting it to each other. A larger modulus provides higher security but requires more processing time. The two peers must have a matching modulus group. Possible values are:<br>GROUP1 - 768-bit modulus.<br>GROUP2 - 1024-bit modulus.<br>GROUP5 - 1536-bit modulus.<br>Field level constraints: cannot be null. (Note: Additional constraints might exist)
  hashType
    description:
      - An enum value that specifies the hash algorithm for creating a message digest, which is used to ensure message integrity. Possible values are:<br>MD5 - The Message Digest 5 algorithm, which produces a 128-bit digest.<br>SHA - The Secure Hash Algorithm, which produces a 160-bit digest.<br>Field level constraints: cannot be null. (Note: Additional constraints might exist)
  id
    description:
      - A unique string identifier assigned by the system when the object is created. No assumption can be made on the format or content of this identifier. The identifier must be provided whenever attempting to modify/delete (or reference) an existing object.<br>Field level constraints: must match pattern ^((?!;).)*$, cannot have HTML. (Note: Additional constraints might exist)
  isSystemDefined
    description:
      - A Boolean value, TRUE or FALSE (the default). The TRUE value indicates that the system created the object. FALSE indicates that the object is user-defined.
  lifeTime
    description:
      - An optional integer that defines the lifetime of the security association (SA), in seconds, from 120 to 2147483647, with the typical limit being 86400. When the lifetime is exceeded, the SA expires and must be renegotiated between the two peers. Leave the option as null to specify no lifetime limit.
  limit
    description:
      - An integer representing the maximum amount of objects to return. If not specified, the maximum amount is 10
  name
    description:
      - The name of the object, up to 128 characters.
  offset
    description:
      - An integer representing the index of the first requested object. Index starts from 0. If not specified, the returned objects will start from index 0
  priority
    description:
      - A required integer that determines the relative priority of the IKE policy, from 1 to 65535. The priority determines the order of the IKE policy compared by the two negotiating peers when attempting to find a common security association (SA). If the remote IPsec peer does not support the parameters selected in your highest priority policy, it tries to use the parameters defined in the next lowest priority. The lower the number, the higher the priority. A given number is meaningful only in relation to the priority numbers defined on the other IKE policies.<br>Field level constraints: cannot be null. (Note: Additional constraints might exist)
  sort
    description:
      - The field used to sort the requested object list
  summaryLabel
    description:
      - A system-provided string that describes the IKE policy.
  type
    description:
      - A UTF8 string, all letters lower-case, that represents the class-type. This corresponds to the class name.
  version
    description:
      - A unique string version assigned by the system when the object is created or modified. No assumption can be made on the format or content of this identifier. The identifier must be provided whenever attempting to modify/delete an existing object. As the version will change every time the object is modified, the value provided in this identifier must match exactly what is present in the system or the request will be rejected.

extends_documentation_fragment: ftd
"""

EXAMPLES = """
- name: Fetch IkevOnePolicy with a given name
  ftd_ikev_one_policy:
    hostname: "https://127.0.0.1:8585"
    access_token: 'ACCESS_TOKEN'
    refresh_token: 'REFRESH_TOKEN'
    operation: "getIkevOnePolicyByName"
    name: "Ansible IkevOnePolicy"

- name: Create a IkevOnePolicy
  ftd_ikev_one_policy:
    hostname: "https://127.0.0.1:8585"
    access_token: 'ACCESS_TOKEN'
    refresh_token: 'REFRESH_TOKEN'
    operation: 'addIkevOnePolicy'

    name: "Ansible IkevOnePolicy"
    type: "ikevonepolicy"
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


class IkevOnePolicyResource(object):
    
    @staticmethod
    @retry_on_token_expiration
    def addIkevOnePolicy(params):
        body_params = dict_subset(params, ['authenticationType', 'cryptoRestricted', 'enabled', 'encryptionType', 'groupType', 'hashType', 'id', 'isSystemDefined', 'lifeTime', 'name', 'priority', 'summaryLabel', 'type', 'version'])

        url = construct_url(params['hostname'], '/object/ikev1policies')
        request_params = dict(
            headers=base_headers(params['access_token']),
            method='POST',
            data=json.dumps(body_params)
        )

        response = open_url(url, **request_params).read()
        return json.loads(response) if response else response

    @staticmethod
    @retry_on_token_expiration
    def deleteIkevOnePolicy(params):
        path_params = dict_subset(params, ['objId'])

        url = construct_url(params['hostname'], '/object/ikev1policies/{objId}', path_params=path_params)
        request_params = dict(
            headers=base_headers(params['access_token']),
            method='DELETE',
        )

        response = open_url(url, **request_params).read()
        return json.loads(response) if response else response

    @staticmethod
    @retry_on_token_expiration
    def editIkevOnePolicy(params):
        path_params = dict_subset(params, ['objId'])
        body_params = dict_subset(params, ['authenticationType', 'cryptoRestricted', 'enabled', 'encryptionType', 'groupType', 'hashType', 'id', 'isSystemDefined', 'lifeTime', 'name', 'priority', 'summaryLabel', 'type', 'version'])

        url = construct_url(params['hostname'], '/object/ikev1policies/{objId}', path_params=path_params)
        request_params = dict(
            headers=base_headers(params['access_token']),
            method='PUT',
            data=json.dumps(body_params)
        )

        response = open_url(url, **request_params).read()
        return json.loads(response) if response else response

    @staticmethod
    @retry_on_token_expiration
    def getIkevOnePolicy(params):
        path_params = dict_subset(params, ['objId'])

        url = construct_url(params['hostname'], '/object/ikev1policies/{objId}', path_params=path_params)
        request_params = dict(
            headers=base_headers(params['access_token']),
            method='GET',
        )

        response = open_url(url, **request_params).read()
        return json.loads(response) if response else response

    @staticmethod
    @retry_on_token_expiration
    def getIkevOnePolicyList(params):
        query_params = dict_subset(params, ['filter', 'limit', 'offset', 'sort'])

        url = construct_url(params['hostname'], '/object/ikev1policies', query_params=query_params)
        request_params = dict(
            headers=base_headers(params['access_token']),
            method='GET',
        )

        response = open_url(url, **request_params).read()
        return json.loads(response) if response else response

    @staticmethod
    @retry_on_token_expiration
    def getIkevOnePolicyByName(params):
        search_params = params.copy()
        search_params['filter'] = 'name:%s' % params['name']
        item_generator = iterate_over_pageable_resource(IkevOnePolicyResource.getIkevOnePolicyList, search_params)
        return next(item for item in item_generator if item['name'] == params['name'])

    @staticmethod
    @retry_on_token_expiration
    def upsertIkevOnePolicy(params):
        def is_duplicate_name_error(err):
            return err.code == 422 and "Validation failed due to a duplicate name" in str(err.read())

        try:
            return IkevOnePolicyResource.addIkevOnePolicy(params)
        except HTTPError as e:
            if is_duplicate_name_error(e):
                existing_object = IkevOnePolicyResource.getIkevOnePolicyByName(params)
                params = copy_identity_properties(existing_object, params)
                return IkevOnePolicyResource.editIkevOnePolicy(params)
            else:
                raise e

    @staticmethod
    @retry_on_token_expiration
    def editIkevOnePolicyByName(params):
        existing_object = IkevOnePolicyResource.getIkevOnePolicyByName(params)
        params = copy_identity_properties(existing_object, params)
        return IkevOnePolicyResource.editIkevOnePolicy(params)

    @staticmethod
    @retry_on_token_expiration
    def deleteIkevOnePolicyByName(params):
        existing_object = IkevOnePolicyResource.getIkevOnePolicyByName(params)
        params = copy_identity_properties(existing_object, params)
        return IkevOnePolicyResource.deleteIkevOnePolicy(params)


def main():
    fields = dict(
        hostname=dict(type='str', required=True),
        access_token=dict(type='str', required=True),
        refresh_token=dict(type='str', required=True),

        operation=dict(type='str', default='upsertIkevOnePolicy', choices=['addIkevOnePolicy', 'deleteIkevOnePolicy', 'editIkevOnePolicy', 'getIkevOnePolicy', 'getIkevOnePolicyList', 'getIkevOnePolicyByName', 'upsertIkevOnePolicy', 'editIkevOnePolicyByName', 'deleteIkevOnePolicyByName']),
        register_as=dict(type='str'),

        authenticationType=dict(type='str'),
        cryptoRestricted=dict(type='bool'),
        enabled=dict(type='bool'),
        encryptionType=dict(type='str'),
        filter=dict(type='str'),
        groupType=dict(type='str'),
        hashType=dict(type='str'),
        id=dict(type='str'),
        isSystemDefined=dict(type='bool'),
        lifeTime=dict(type='int'),
        limit=dict(type='int'),
        name=dict(type='str'),
        objId=dict(type='str'),
        offset=dict(type='int'),
        priority=dict(type='int'),
        sort=dict(type='str'),
        summaryLabel=dict(type='str'),
        type=dict(type='str'),
        version=dict(type='str'),
    )

    module = AnsibleModule(argument_spec=fields)
    params = module.params

    try:
        method_to_call = getattr(IkevOnePolicyResource, params['operation'])
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
#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Copyright 2021 A10 Networks
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

REQUIRED_NOT_SET = (False, "One of ({}) must be set.")
REQUIRED_MUTEX = (False, "Only one of ({}) can be set.")
REQUIRED_VALID = (True, "")

DOCUMENTATION = r'''
module: a10_file_inspection_global_stat
description:
    - global stats
author: A10 Networks 2021
options:
    state:
        description:
        - State of the object to be created.
        choices:
          - noop
          - present
          - absent
        type: str
        required: True
    ansible_host:
        description:
        - Host for AXAPI authentication
        type: str
        required: True
    ansible_username:
        description:
        - Username for AXAPI authentication
        type: str
        required: True
    ansible_password:
        description:
        - Password for AXAPI authentication
        type: str
        required: True
    ansible_port:
        description:
        - Port for AXAPI authentication
        type: int
        required: True
    a10_device_context_id:
        description:
        - Device ID for aVCS configuration
        choices: [1-8]
        type: int
        required: False
    a10_partition:
        description:
        - Destination/target partition for object/command
        type: str
        required: False
    file_path:
        description:
        - Path to the file
        type: str
        required: False
    uuid:
        description:
        - "uuid of the object"
        type: str
        required: False
    sampling_enable:
        description:
        - "Field sampling_enable"
        type: list
        required: False
        suboptions:
            counters1:
                description:
                - "'all'= all; 'download_bad_blocked'= Download malware blocked;
          'download_bad_allowed'= Download malware allowed; 'download_bad_ext_inspect'=
          Download malware extrnal inspect; 'download_suspect_blocked'= Download suspect
          blocked; 'download_suspect_ext_inspect'= Download suspect extrnal inspect;
          'download_suspect_allowed'= Download suspect allowed; 'download_good_blocked'=
          Download safe blocked; 'download_good_allowed'= Download safe external inspect;
          'download_good_ext_inspect'= Download safe allowed; 'upload_bad_blocked'=
          Upload malware blocked; 'upload_bad_allowed'= Upload malware allowed;
          'upload_bad_ext_inspect'= Upload malware extrnal inspect;
          'upload_suspect_blocked'= Upload suspect blocked; 'upload_suspect_ext_inspect'=
          Upload suspect extrnal inspect; 'upload_suspect_allowed'= Upload suspect
          allowed; 'upload_good_blocked'= Upload safe blocked; 'upload_good_ext_inspect'=
          Upload safe external inspect; 'upload_good_allowed'= Upload safe allowed;
          'icap_200'= Receive icap status 200; 'icap_204'= Receive icap status 204;
          'icap_500'= Receive icap status 500; 'icap_other_status_code'= Receive icap
          other status code; 'icap_connect_fail'= Icap connect fail;
          'icap_connection_created'= Icap connection created;
          'icap_connection_established'= Icap connection established;
          'icap_connection_closed'= Icap connection closed; 'icap_connection_rst'= Icap
          connection rst; 'icap_bytes_sent'= Icap bytes sent; 'icap_bytes_received'= Icap
          bytes received; 'bypass_aflex'= Bypassed by aflex; 'bypass_large_file'=
          Bypassed - large file size; 'bypass_service_disabled'= Bypassed - Internal
          service disabled; 'bypass_service_down'= Bypassed - Internal service down;
          'reset_service_down'= Reset - Internal service down;
          'bypass_max_concurrent_files_reached'= Bypassed - max concurrent files on
          server reached; 'bypass_non_inspection'= Bypassed non inspection data;
          'non_supported_file'= Non supported file type; 'transactions_alloc'= Total
          transactions allocated; 'transactions_free'= Total transactions freed;
          'transactions_failure'= Total transactions failure; 'transactions_aborted'=
          Total transactions aborted; 'orig_conn_bytes_received'= Original connection
          bytes received; 'orig_conn_bytes_sent'= Original connection bytes sent;
          'orig_conn_bytes_bypassed'= Original connection bytes bypassed;
          'bypass_buffered_overlimit'= Total Bytes Buffered Overlimit; 'total_bandwidth'=
          Total File Bytes; 'total_suspect_bandwidth'= Total Suspected Files Bytes;
          'total_bad_bandwidth'= Total Bad Files Bytes; 'total_good_bandwidth'= Total
          Good Files Bytes; 'total_file_size_less_1m'= Total Files Less than 1Mb;
          'total_file_size_1_5m'= Total Files Between 1-5Mb; 'total_file_size_5_8m'=
          Total Files Between 5-8Mb; 'total_file_size_8_32m'= Total Files Between 8-32Mb;
          'total_file_size_over_32m'= Total Files over 32Mb; 'suspect_file_size_less_1m'=
          Suspect Files Less than 1Mb; 'suspect_file_size_1_5m'= Suspect Files Between
          1-5Mb; 'suspect_file_size_5_8m'= Suspect Files Between 5-8Mb;
          'suspect_file_size_8_32m'= Suspect Files Between 8-32Mb;
          'suspect_file_size_over_32m'= Suspect Files over 32Mb;
          'good_file_size_less_1m'= Good Files Less than 1Mb; 'good_file_size_1_5m'= Good
          Files Between 1-5Mb; 'good_file_size_5_8m'= Good Files Between 5-8Mb;
          'good_file_size_8_32m'= Good Files Between 8-32Mb; 'good_file_size_over_32m'=
          Good Files over 32Mb; 'bad_file_size_less_1m'= Bad Files Less than 1Mb;
          'bad_file_size_1_5m'= Bad Files Between 1-5Mb; 'bad_file_size_5_8m'= Bad Files
          Between 5-8Mb; 'bad_file_size_8_32m'= Bad Files Between 8-32Mb;
          'bad_file_size_over_32m'= Bad Files over 32Mb;"
                type: str
    stats:
        description:
        - "Field stats"
        type: dict
        required: False
        suboptions:
            download_bad_blocked:
                description:
                - "Download malware blocked"
                type: str
            download_bad_allowed:
                description:
                - "Download malware allowed"
                type: str
            download_bad_ext_inspect:
                description:
                - "Download malware extrnal inspect"
                type: str
            download_suspect_blocked:
                description:
                - "Download suspect blocked"
                type: str
            download_suspect_ext_inspect:
                description:
                - "Download suspect extrnal inspect"
                type: str
            download_suspect_allowed:
                description:
                - "Download suspect allowed"
                type: str
            download_good_blocked:
                description:
                - "Download safe blocked"
                type: str
            download_good_allowed:
                description:
                - "Download safe external inspect"
                type: str
            download_good_ext_inspect:
                description:
                - "Download safe allowed"
                type: str
            upload_bad_blocked:
                description:
                - "Upload malware blocked"
                type: str
            upload_bad_allowed:
                description:
                - "Upload malware allowed"
                type: str
            upload_bad_ext_inspect:
                description:
                - "Upload malware extrnal inspect"
                type: str
            upload_suspect_blocked:
                description:
                - "Upload suspect blocked"
                type: str
            upload_suspect_ext_inspect:
                description:
                - "Upload suspect extrnal inspect"
                type: str
            upload_suspect_allowed:
                description:
                - "Upload suspect allowed"
                type: str
            upload_good_blocked:
                description:
                - "Upload safe blocked"
                type: str
            upload_good_ext_inspect:
                description:
                - "Upload safe external inspect"
                type: str
            upload_good_allowed:
                description:
                - "Upload safe allowed"
                type: str
            icap_200:
                description:
                - "Receive icap status 200"
                type: str
            icap_204:
                description:
                - "Receive icap status 204"
                type: str
            icap_500:
                description:
                - "Receive icap status 500"
                type: str
            icap_other_status_code:
                description:
                - "Receive icap other status code"
                type: str
            icap_connect_fail:
                description:
                - "Icap connect fail"
                type: str
            icap_connection_created:
                description:
                - "Icap connection created"
                type: str
            icap_connection_established:
                description:
                - "Icap connection established"
                type: str
            icap_connection_closed:
                description:
                - "Icap connection closed"
                type: str
            icap_connection_rst:
                description:
                - "Icap connection rst"
                type: str
            icap_bytes_sent:
                description:
                - "Icap bytes sent"
                type: str
            icap_bytes_received:
                description:
                - "Icap bytes received"
                type: str
            bypass_aflex:
                description:
                - "Bypassed by aflex"
                type: str
            bypass_large_file:
                description:
                - "Bypassed - large file size"
                type: str
            bypass_service_disabled:
                description:
                - "Bypassed - Internal service disabled"
                type: str
            bypass_service_down:
                description:
                - "Bypassed - Internal service down"
                type: str
            reset_service_down:
                description:
                - "Reset - Internal service down"
                type: str
            bypass_max_concurrent_files_reached:
                description:
                - "Bypassed - max concurrent files on server reached"
                type: str
            bypass_non_inspection:
                description:
                - "Bypassed non inspection data"
                type: str
            non_supported_file:
                description:
                - "Non supported file type"
                type: str
            transactions_alloc:
                description:
                - "Total transactions allocated"
                type: str
            transactions_free:
                description:
                - "Total transactions freed"
                type: str
            transactions_failure:
                description:
                - "Total transactions failure"
                type: str
            transactions_aborted:
                description:
                - "Total transactions aborted"
                type: str
            orig_conn_bytes_received:
                description:
                - "Original connection bytes received"
                type: str
            orig_conn_bytes_sent:
                description:
                - "Original connection bytes sent"
                type: str
            orig_conn_bytes_bypassed:
                description:
                - "Original connection bytes bypassed"
                type: str
            bypass_buffered_overlimit:
                description:
                - "Total Bytes Buffered Overlimit"
                type: str
            total_bandwidth:
                description:
                - "Total File Bytes"
                type: str
            total_suspect_bandwidth:
                description:
                - "Total Suspected Files Bytes"
                type: str
            total_bad_bandwidth:
                description:
                - "Total Bad Files Bytes"
                type: str
            total_good_bandwidth:
                description:
                - "Total Good Files Bytes"
                type: str
            total_file_size_less_1m:
                description:
                - "Total Files Less than 1Mb"
                type: str
            total_file_size_1_5m:
                description:
                - "Total Files Between 1-5Mb"
                type: str
            total_file_size_5_8m:
                description:
                - "Total Files Between 5-8Mb"
                type: str
            total_file_size_8_32m:
                description:
                - "Total Files Between 8-32Mb"
                type: str
            total_file_size_over_32m:
                description:
                - "Total Files over 32Mb"
                type: str
            suspect_file_size_less_1m:
                description:
                - "Suspect Files Less than 1Mb"
                type: str
            suspect_file_size_1_5m:
                description:
                - "Suspect Files Between 1-5Mb"
                type: str
            suspect_file_size_5_8m:
                description:
                - "Suspect Files Between 5-8Mb"
                type: str
            suspect_file_size_8_32m:
                description:
                - "Suspect Files Between 8-32Mb"
                type: str
            suspect_file_size_over_32m:
                description:
                - "Suspect Files over 32Mb"
                type: str
            good_file_size_less_1m:
                description:
                - "Good Files Less than 1Mb"
                type: str
            good_file_size_1_5m:
                description:
                - "Good Files Between 1-5Mb"
                type: str
            good_file_size_5_8m:
                description:
                - "Good Files Between 5-8Mb"
                type: str
            good_file_size_8_32m:
                description:
                - "Good Files Between 8-32Mb"
                type: str
            good_file_size_over_32m:
                description:
                - "Good Files over 32Mb"
                type: str
            bad_file_size_less_1m:
                description:
                - "Bad Files Less than 1Mb"
                type: str
            bad_file_size_1_5m:
                description:
                - "Bad Files Between 1-5Mb"
                type: str
            bad_file_size_5_8m:
                description:
                - "Bad Files Between 5-8Mb"
                type: str
            bad_file_size_8_32m:
                description:
                - "Bad Files Between 8-32Mb"
                type: str
            bad_file_size_over_32m:
                description:
                - "Bad Files over 32Mb"
                type: str

'''

RETURN = r'''
modified_values:
    description:
    - Values modified (or potential changes if using check_mode) as a result of task operation
    returned: changed
    type: dict
axapi_calls:
    description: Sequential list of AXAPI calls made by the task
    returned: always
    type: list
    elements: dict
    contains:
        endpoint:
            description: The AXAPI endpoint being accessed.
            type: str
            sample:
                - /axapi/v3/slb/virtual_server
                - /axapi/v3/file/ssl-cert
        http_method:
            description:
            - HTTP method being used by the primary task to interact with the AXAPI endpoint.
            type: str
            sample:
                - POST
                - GET
        request_body:
            description: Params used to query the AXAPI
            type: complex
        response_body:
            description: Response from the AXAPI
            type: complex
'''

EXAMPLES = """
"""

import copy

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.a10.acos_axapi.plugins.module_utils import \
    errors as a10_ex
from ansible_collections.a10.acos_axapi.plugins.module_utils import \
    wrapper as api_client
from ansible_collections.a10.acos_axapi.plugins.module_utils import \
    utils
from ansible_collections.a10.acos_axapi.plugins.module_utils.client import \
    client_factory
from ansible_collections.a10.acos_axapi.plugins.module_utils.kwbl import \
    KW_OUT, translate_blacklist as translateBlacklist

# Hacky way of having access to object properties for evaluation
AVAILABLE_PROPERTIES = [
    "sampling_enable",
    "stats",
    "uuid",
]


def get_default_argspec():
    return dict(
        ansible_host=dict(type='str', required=True),
        ansible_username=dict(type='str', required=True),
        ansible_password=dict(type='str', required=True, no_log=True),
        state=dict(type='str',
                   default="present",
                   choices=['noop', 'present', 'absent']),
        ansible_port=dict(type='int', choices=[80, 443], required=True),
        a10_partition=dict(
            type='str',
            required=False,
        ),
        a10_device_context_id=dict(
            type='int',
            choices=[1, 2, 3, 4, 5, 6, 7, 8],
            required=False,
        ),
        get_type=dict(type='str', choices=["single", "list", "oper", "stats"]),
    )


def get_argspec():
    rv = get_default_argspec()
    rv.update({
        'file_path': {
            'type': 'str',
        },
        'uuid': {
            'type': 'str',
        },
        'sampling_enable': {
            'type': 'list',
            'counters1': {
                'type':
                'str',
                'choices': [
                    'all', 'download_bad_blocked', 'download_bad_allowed',
                    'download_bad_ext_inspect', 'download_suspect_blocked',
                    'download_suspect_ext_inspect', 'download_suspect_allowed',
                    'download_good_blocked', 'download_good_allowed',
                    'download_good_ext_inspect', 'upload_bad_blocked',
                    'upload_bad_allowed', 'upload_bad_ext_inspect',
                    'upload_suspect_blocked', 'upload_suspect_ext_inspect',
                    'upload_suspect_allowed', 'upload_good_blocked',
                    'upload_good_ext_inspect', 'upload_good_allowed',
                    'icap_200', 'icap_204', 'icap_500',
                    'icap_other_status_code', 'icap_connect_fail',
                    'icap_connection_created', 'icap_connection_established',
                    'icap_connection_closed', 'icap_connection_rst',
                    'icap_bytes_sent', 'icap_bytes_received', 'bypass_aflex',
                    'bypass_large_file', 'bypass_service_disabled',
                    'bypass_service_down', 'reset_service_down',
                    'bypass_max_concurrent_files_reached',
                    'bypass_non_inspection', 'non_supported_file',
                    'transactions_alloc', 'transactions_free',
                    'transactions_failure', 'transactions_aborted',
                    'orig_conn_bytes_received', 'orig_conn_bytes_sent',
                    'orig_conn_bytes_bypassed', 'bypass_buffered_overlimit',
                    'total_bandwidth', 'total_suspect_bandwidth',
                    'total_bad_bandwidth', 'total_good_bandwidth',
                    'total_file_size_less_1m', 'total_file_size_1_5m',
                    'total_file_size_5_8m', 'total_file_size_8_32m',
                    'total_file_size_over_32m', 'suspect_file_size_less_1m',
                    'suspect_file_size_1_5m', 'suspect_file_size_5_8m',
                    'suspect_file_size_8_32m', 'suspect_file_size_over_32m',
                    'good_file_size_less_1m', 'good_file_size_1_5m',
                    'good_file_size_5_8m', 'good_file_size_8_32m',
                    'good_file_size_over_32m', 'bad_file_size_less_1m',
                    'bad_file_size_1_5m', 'bad_file_size_5_8m',
                    'bad_file_size_8_32m', 'bad_file_size_over_32m'
                ]
            }
        },
        'stats': {
            'type': 'dict',
            'download_bad_blocked': {
                'type': 'str',
            },
            'download_bad_allowed': {
                'type': 'str',
            },
            'download_bad_ext_inspect': {
                'type': 'str',
            },
            'download_suspect_blocked': {
                'type': 'str',
            },
            'download_suspect_ext_inspect': {
                'type': 'str',
            },
            'download_suspect_allowed': {
                'type': 'str',
            },
            'download_good_blocked': {
                'type': 'str',
            },
            'download_good_allowed': {
                'type': 'str',
            },
            'download_good_ext_inspect': {
                'type': 'str',
            },
            'upload_bad_blocked': {
                'type': 'str',
            },
            'upload_bad_allowed': {
                'type': 'str',
            },
            'upload_bad_ext_inspect': {
                'type': 'str',
            },
            'upload_suspect_blocked': {
                'type': 'str',
            },
            'upload_suspect_ext_inspect': {
                'type': 'str',
            },
            'upload_suspect_allowed': {
                'type': 'str',
            },
            'upload_good_blocked': {
                'type': 'str',
            },
            'upload_good_ext_inspect': {
                'type': 'str',
            },
            'upload_good_allowed': {
                'type': 'str',
            },
            'icap_200': {
                'type': 'str',
            },
            'icap_204': {
                'type': 'str',
            },
            'icap_500': {
                'type': 'str',
            },
            'icap_other_status_code': {
                'type': 'str',
            },
            'icap_connect_fail': {
                'type': 'str',
            },
            'icap_connection_created': {
                'type': 'str',
            },
            'icap_connection_established': {
                'type': 'str',
            },
            'icap_connection_closed': {
                'type': 'str',
            },
            'icap_connection_rst': {
                'type': 'str',
            },
            'icap_bytes_sent': {
                'type': 'str',
            },
            'icap_bytes_received': {
                'type': 'str',
            },
            'bypass_aflex': {
                'type': 'str',
            },
            'bypass_large_file': {
                'type': 'str',
            },
            'bypass_service_disabled': {
                'type': 'str',
            },
            'bypass_service_down': {
                'type': 'str',
            },
            'reset_service_down': {
                'type': 'str',
            },
            'bypass_max_concurrent_files_reached': {
                'type': 'str',
            },
            'bypass_non_inspection': {
                'type': 'str',
            },
            'non_supported_file': {
                'type': 'str',
            },
            'transactions_alloc': {
                'type': 'str',
            },
            'transactions_free': {
                'type': 'str',
            },
            'transactions_failure': {
                'type': 'str',
            },
            'transactions_aborted': {
                'type': 'str',
            },
            'orig_conn_bytes_received': {
                'type': 'str',
            },
            'orig_conn_bytes_sent': {
                'type': 'str',
            },
            'orig_conn_bytes_bypassed': {
                'type': 'str',
            },
            'bypass_buffered_overlimit': {
                'type': 'str',
            },
            'total_bandwidth': {
                'type': 'str',
            },
            'total_suspect_bandwidth': {
                'type': 'str',
            },
            'total_bad_bandwidth': {
                'type': 'str',
            },
            'total_good_bandwidth': {
                'type': 'str',
            },
            'total_file_size_less_1m': {
                'type': 'str',
            },
            'total_file_size_1_5m': {
                'type': 'str',
            },
            'total_file_size_5_8m': {
                'type': 'str',
            },
            'total_file_size_8_32m': {
                'type': 'str',
            },
            'total_file_size_over_32m': {
                'type': 'str',
            },
            'suspect_file_size_less_1m': {
                'type': 'str',
            },
            'suspect_file_size_1_5m': {
                'type': 'str',
            },
            'suspect_file_size_5_8m': {
                'type': 'str',
            },
            'suspect_file_size_8_32m': {
                'type': 'str',
            },
            'suspect_file_size_over_32m': {
                'type': 'str',
            },
            'good_file_size_less_1m': {
                'type': 'str',
            },
            'good_file_size_1_5m': {
                'type': 'str',
            },
            'good_file_size_5_8m': {
                'type': 'str',
            },
            'good_file_size_8_32m': {
                'type': 'str',
            },
            'good_file_size_over_32m': {
                'type': 'str',
            },
            'bad_file_size_less_1m': {
                'type': 'str',
            },
            'bad_file_size_1_5m': {
                'type': 'str',
            },
            'bad_file_size_5_8m': {
                'type': 'str',
            },
            'bad_file_size_8_32m': {
                'type': 'str',
            },
            'bad_file_size_over_32m': {
                'type': 'str',
            }
        }
    })
    return rv


def existing_url(module):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/file-inspection/global-stat"

    f_dict = {}

    return url_base.format(**f_dict)


def new_url(module):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/file-inspection/global-stat"

    f_dict = {}

    return url_base.format(**f_dict)


def report_changes(module, result, existing_config, payload):
    change_results = copy.deepcopy(result)
    if not existing_config:
        change_results["modified_values"].update(**payload)
        return change_results

    file_check = ['file-handle', 'file']
    config_changes = copy.deepcopy(existing_config)
    for k, v in payload["global-stat"].items():
        if k not in file_check:
            continue
        v = 1 if str(v).lower() == "true" else v
        v = 0 if str(v).lower() == "false" else v

        if config_changes["global-stat"].get(k) != v:
            change_results["changed"] = True
            config_changes["global-stat"][k] = v

    change_results["modified_values"].update(**config_changes)
    return change_results


def create(module, result, payload={}):
    if module.params["action"] == "import":
        call_result = api_client.post_file(
            module.client,
            new_url(module),
            payload,
            file_path=module.params["file_path"],
            file_name=module.params["file"])
    else:
        call_result = api_client.post(module.client, new_url(module), payload)
    result["axapi_calls"].append(call_result)
    result["modified_values"].update(**call_result["response_body"])
    result["changed"] = True
    return result


def update(module, result, existing_config, payload={}):
    if module.params["action"] == "import":
        call_result = api_client.post_file(
            module.client,
            existing_url(module),
            payload,
            file_path=module.params["file_path"],
            file_name=module.params["file"])
    else:
        call_result = api_client.post(module.client, existing_url(module),
                                      payload)
    result["axapi_calls"].append(call_result)
    if call_result["response_body"] == existing_config:
        result["changed"] = False
    else:
        result["modified_values"].update(**call_result["response_body"])
        result["changed"] = True
    return result


def present(module, result, existing_config):
    payload = utils.build_json("global-stat", module.params,
                               AVAILABLE_PROPERTIES)
    change_results = report_changes(module, result, existing_config, payload)
    if module.check_mode:
        return change_results
    elif not existing_config:
        return create(module, result, payload)
    elif existing_config and change_results.get('changed'):
        return update(module, result, existing_config, payload)
    return result


def delete(module, result):
    try:
        call_result = api_client.delete(module.client, existing_url(module))
        result["axapi_calls"].append(call_result)
        result["changed"] = True
    except a10_ex.NotFound:
        result["changed"] = False
    return result


def absent(module, result, existing_config):
    if not existing_config:
        result["changed"] = False
        return result

    if module.check_mode:
        result["changed"] = True
        return result

    return delete(module, result)


def run_command(module):
    result = dict(changed=False,
                  messages="",
                  modified_values={},
                  axapi_calls=[],
                  ansible_facts={},
                  acos_info={})

    state = module.params["state"]
    ansible_host = module.params["ansible_host"]
    ansible_username = module.params["ansible_username"]
    ansible_password = module.params["ansible_password"]
    ansible_port = module.params["ansible_port"]
    a10_partition = module.params["a10_partition"]
    a10_device_context_id = module.params["a10_device_context_id"]

    if ansible_port == 80:
        protocol = "http"
    elif ansible_port == 443:
        protocol = "https"

    module.client = client_factory(ansible_host, ansible_port, protocol,
                                   ansible_username, ansible_password)

    valid = True

    run_errors = []
    if state == 'present':
        requires_one_of = sorted([])
        valid, validation_errors = utils.validate(module.params,
                                                  requires_one_of)
        for ve in validation_errors:
            run_errors.append(ve)

    if not valid:
        err_msg = "\n".join(run_errors)
        result["messages"] = "Validation failure: " + str(run_errors)
        module.fail_json(msg=err_msg, **result)

    try:
        if a10_partition:
            result["axapi_calls"].append(
                api_client.active_partition(module.client, a10_partition))

        if a10_device_context_id:
            result["axapi_calls"].append(
                api_client.switch_device_context(module.client,
                                                 a10_device_context_id))

        file_url = api_client.oper_url(existing_url(module))
        existing_config, file_exists = api_client.get_file(
            module.client, "global-stat", file_url, module.params['file'])
        result["axapi_calls"].append(existing_config)

        if file_exists:
            existing_config = existing_config["response_body"]
        else:
            existing_config = None

        if state == 'present':
            result = present(module, result, existing_config)

        if state == 'absent':
            result = absent(module, result, existing_config)

        if state == 'noop':
            if module.params.get("get_type") == "single":
                get_result = api_client.get(module.client,
                                            existing_url(module))
                result["axapi_calls"].append(get_result)
                info = get_result["response_body"]
                result["acos_info"] = info[
                    "global-stat"] if info != "NotFound" else info
            elif module.params.get("get_type") == "list":
                get_list_result = api_client.get_list(module.client,
                                                      existing_url(module))
                result["axapi_calls"].append(get_list_result)

                info = get_list_result["response_body"]
                result["acos_info"] = info[
                    "global-stat-list"] if info != "NotFound" else info
            elif module.params.get("get_type") == "stats":
                get_type_result = api_client.get_stats(module.client,
                                                       existing_url(module),
                                                       params=module.params)
                result["axapi_calls"].append(get_type_result)
                info = get_type_result["response_body"]
                result["acos_info"] = info["global-stat"][
                    "stats"] if info != "NotFound" else info
    except a10_ex.ACOSException as ex:
        module.fail_json(msg=ex.msg, **result)
    except Exception as gex:
        raise gex
    finally:
        if module.client.auth_session.session_id:
            module.client.auth_session.close()

    return result


def main():
    module = AnsibleModule(argument_spec=get_argspec(),
                           supports_check_mode=True)
    result = run_command(module)
    module.exit_json(**result)


if __name__ == '__main__':
    main()

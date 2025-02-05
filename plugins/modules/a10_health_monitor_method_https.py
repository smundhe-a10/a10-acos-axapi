#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Copyright 2021 A10 Networks
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

REQUIRED_NOT_SET = (False, "One of ({}) must be set.")
REQUIRED_MUTEX = (False, "Only one of ({}) can be set.")
REQUIRED_VALID = (True, "")

DOCUMENTATION = r'''
module: a10_health_monitor_method_https
description:
    - HTTPS type
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
    monitor_name:
        description:
        - Key to identify parent object
        type: str
        required: True
    https:
        description:
        - "HTTPS type"
        type: bool
        required: False
    web_port:
        description:
        - "Specify HTTPS port (Port Number (default 443))"
        type: int
        required: False
    https_expect:
        description:
        - "Specify what you expect from the response message"
        type: bool
        required: False
    https_response_code:
        description:
        - "Specify response code range (e.g. 200,400-430) (Format is xx,xx-xx (xx between
          [100, 899])"
        type: str
        required: False
    response_code_regex:
        description:
        - "Specify response code range with Regex (code with Regex, such as
          [2-5][0-9][0-9])"
        type: str
        required: False
    https_text:
        description:
        - "Specify text expected"
        type: str
        required: False
    text_regex:
        description:
        - "Specify text expected  with Regex"
        type: str
        required: False
    https_host:
        description:
        - "Specify 'Host=' header used in request (enclose IPv6 address in [])"
        type: str
        required: False
    https_maintenance_code:
        description:
        - "Specify response code for maintenance (Format is xx,xx-xx (xx between [100,
          899])"
        type: str
        required: False
    https_url:
        description:
        - "Specify URL string, default is GET /"
        type: bool
        required: False
    url_type:
        description:
        - "'GET'= HTTP GET method; 'POST'= HTTP POST method; 'HEAD'= HTTP HEAD method;"
        type: str
        required: False
    url_path:
        description:
        - "Specify URL path, default is '/'"
        type: str
        required: False
    post_path:
        description:
        - "Specify URL path, default is '/'"
        type: str
        required: False
    post_type:
        description:
        - "'postdata'= Specify the HTTP post data; 'postfile'= Specify the HTTP post data;"
        type: str
        required: False
    https_postdata:
        description:
        - "Specify the HTTP post data (Input post data here)"
        type: str
        required: False
    https_postfile:
        description:
        - "Specify the HTTP post data (Input post data file name here)"
        type: str
        required: False
    https_username:
        description:
        - "Specify the username"
        type: str
        required: False
    https_password:
        description:
        - "Specify the user password"
        type: bool
        required: False
    https_password_string:
        description:
        - "Configure password, '' means empty password"
        type: str
        required: False
    https_encrypted:
        description:
        - "Do NOT use this option manually. (This is an A10 reserved keyword.) (The
          ENCRYPTED password string)"
        type: str
        required: False
    disable_sslv2hello:
        description:
        - "Disable SSLv2Hello for HTTPs"
        type: bool
        required: False
    https_kerberos_auth:
        description:
        - "Https Kerberos Auth"
        type: bool
        required: False
    https_kerberos_realm:
        description:
        - "Specify realm of Kerberos server"
        type: str
        required: False
    https_kerberos_kdc:
        description:
        - "Field https_kerberos_kdc"
        type: dict
        required: False
        suboptions:
            https_kerberos_hostip:
                description:
                - "Kdc's hostname(length=1-31) or IP address"
                type: str
            https_kerberos_hostipv6:
                description:
                - "Server's IPV6 address"
                type: str
            https_kerberos_port:
                description:
                - "Specify the kdc port"
                type: int
            https_kerberos_portv6:
                description:
                - "Specify the kdc port"
                type: int
    cert_key_shared:
        description:
        - "Select shared partition"
        type: bool
        required: False
    cert:
        description:
        - "Specify client certificate (Certificate name)"
        type: str
        required: False
    key:
        description:
        - "Specify client private key (Key name)"
        type: str
        required: False
    key_pass_phrase:
        description:
        - "Client private key password phrase"
        type: bool
        required: False
    key_phrase:
        description:
        - "Password Phrase"
        type: str
        required: False
    https_key_encrypted:
        description:
        - "Do NOT use this option manually. (This is an A10 reserved keyword.) (The
          ENCRYPTED password string)"
        type: str
        required: False
    uuid:
        description:
        - "uuid of the object"
        type: str
        required: False

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
    "cert",
    "cert_key_shared",
    "disable_sslv2hello",
    "https",
    "https_encrypted",
    "https_expect",
    "https_host",
    "https_kerberos_auth",
    "https_kerberos_kdc",
    "https_kerberos_realm",
    "https_key_encrypted",
    "https_maintenance_code",
    "https_password",
    "https_password_string",
    "https_postdata",
    "https_postfile",
    "https_response_code",
    "https_text",
    "https_url",
    "https_username",
    "key",
    "key_pass_phrase",
    "key_phrase",
    "post_path",
    "post_type",
    "response_code_regex",
    "text_regex",
    "url_path",
    "url_type",
    "uuid",
    "web_port",
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
        'https': {
            'type': 'bool',
        },
        'web_port': {
            'type': 'int',
        },
        'https_expect': {
            'type': 'bool',
        },
        'https_response_code': {
            'type': 'str',
        },
        'response_code_regex': {
            'type': 'str',
        },
        'https_text': {
            'type': 'str',
        },
        'text_regex': {
            'type': 'str',
        },
        'https_host': {
            'type': 'str',
        },
        'https_maintenance_code': {
            'type': 'str',
        },
        'https_url': {
            'type': 'bool',
        },
        'url_type': {
            'type': 'str',
            'choices': ['GET', 'POST', 'HEAD']
        },
        'url_path': {
            'type': 'str',
        },
        'post_path': {
            'type': 'str',
        },
        'post_type': {
            'type': 'str',
            'choices': ['postdata', 'postfile']
        },
        'https_postdata': {
            'type': 'str',
        },
        'https_postfile': {
            'type': 'str',
        },
        'https_username': {
            'type': 'str',
        },
        'https_password': {
            'type': 'bool',
        },
        'https_password_string': {
            'type': 'str',
        },
        'https_encrypted': {
            'type': 'str',
        },
        'disable_sslv2hello': {
            'type': 'bool',
        },
        'https_kerberos_auth': {
            'type': 'bool',
        },
        'https_kerberos_realm': {
            'type': 'str',
        },
        'https_kerberos_kdc': {
            'type': 'dict',
            'https_kerberos_hostip': {
                'type': 'str',
            },
            'https_kerberos_hostipv6': {
                'type': 'str',
            },
            'https_kerberos_port': {
                'type': 'int',
            },
            'https_kerberos_portv6': {
                'type': 'int',
            }
        },
        'cert_key_shared': {
            'type': 'bool',
        },
        'cert': {
            'type': 'str',
        },
        'key': {
            'type': 'str',
        },
        'key_pass_phrase': {
            'type': 'bool',
        },
        'key_phrase': {
            'type': 'str',
        },
        'https_key_encrypted': {
            'type': 'str',
        },
        'uuid': {
            'type': 'str',
        }
    })
    # Parent keys
    rv.update(dict(monitor_name=dict(type='str', required=True), ))
    return rv


def existing_url(module):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/health/monitor/{monitor_name}/method/https"

    f_dict = {}
    f_dict["monitor_name"] = module.params["monitor_name"]

    return url_base.format(**f_dict)


def new_url(module):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/health/monitor/{monitor_name}/method/https"

    f_dict = {}
    f_dict["monitor_name"] = module.params["monitor_name"]

    return url_base.format(**f_dict)


def report_changes(module, result, existing_config, payload):
    change_results = copy.deepcopy(result)
    if not existing_config:
        change_results["modified_values"].update(**payload)
        return change_results

    config_changes = copy.deepcopy(existing_config)
    for k, v in payload["https"].items():
        v = 1 if str(v).lower() == "true" else v
        v = 0 if str(v).lower() == "false" else v

        if config_changes["https"].get(k) != v:
            change_results["changed"] = True
            config_changes["https"][k] = v

    change_results["modified_values"].update(**config_changes)
    return change_results


def create(module, result, payload={}):
    call_result = api_client.post(module.client, new_url(module), payload)
    result["axapi_calls"].append(call_result)
    result["modified_values"].update(**call_result["response_body"])
    result["changed"] = True
    return result


def update(module, result, existing_config, payload={}):
    call_result = api_client.post(module.client, existing_url(module), payload)
    result["axapi_calls"].append(call_result)
    if call_result["response_body"] == existing_config:
        result["changed"] = False
    else:
        result["modified_values"].update(**call_result["response_body"])
        result["changed"] = True
    return result


def present(module, result, existing_config):
    payload = utils.build_json("https", module.params, AVAILABLE_PROPERTIES)
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

        existing_config = api_client.get(module.client, existing_url(module))
        result["axapi_calls"].append(existing_config)
        if existing_config['response_body'] != 'NotFound':
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
                    "https"] if info != "NotFound" else info
            elif module.params.get("get_type") == "list":
                get_list_result = api_client.get_list(module.client,
                                                      existing_url(module))
                result["axapi_calls"].append(get_list_result)

                info = get_list_result["response_body"]
                result["acos_info"] = info[
                    "https-list"] if info != "NotFound" else info
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

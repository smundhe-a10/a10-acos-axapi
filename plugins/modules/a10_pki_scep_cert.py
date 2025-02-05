#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Copyright 2021 A10 Networks
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

REQUIRED_NOT_SET = (False, "One of ({}) must be set.")
REQUIRED_MUTEX = (False, "Only one of ({}) can be set.")
REQUIRED_VALID = (True, "")

DOCUMENTATION = r'''
module: a10_pki_scep_cert
description:
    - SCEP Certificate enrollment object
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
    name:
        description:
        - "Specify Certificate name to be enrolled"
        type: str
        required: True
    url:
        description:
        - "Specify the Enrollment Agent's absolute URL (Format= http=//host/path)"
        type: str
        required: False
    dn:
        description:
        - "Specify the Distinguished-Name to use while enrolling the certificate (Format=
          'cn=user, dc=example, dc=com')"
        type: str
        required: False
    subject_alternate_name:
        description:
        - "Field subject_alternate_name"
        type: dict
        required: False
        suboptions:
            san_type:
                description:
                - "'email'= Enter e-mail address of the subject; 'dns'= Enter hostname of the
          subject; 'ip'= Enter IP address of the subject;"
                type: str
            san_value:
                description:
                - "Value of subject-alternate-name"
                type: str
    enroll:
        description:
        - "Initiates enrollment of device with the CA"
        type: bool
        required: False
    log_level:
        description:
        - "level for logging output of scepclient commands(default 1 and detailed 4)"
        type: int
        required: False
    password:
        description:
        - "Specify the password used to enroll the device's certificate"
        type: bool
        required: False
    secret_string:
        description:
        - "secret password"
        type: str
        required: False
    encrypted:
        description:
        - "Do NOT use this option manually. (This is an A10 reserved keyword.) (The
          ENCRYPTED secret string)"
        type: str
        required: False
    renew_before:
        description:
        - "Specify interval before certificate expiry to renew the certificate"
        type: bool
        required: False
    renew_before_type:
        description:
        - "'hour'= Number of hours before cert expiry; 'day'= Number of days before cert
          expiry; 'week'= Number of weeks before cert expiry; 'month'= Number of months
          before cert expiry(1 month=30 days);"
        type: str
        required: False
    renew_before_value:
        description:
        - "Value of renewal period"
        type: int
        required: False
    renew_every:
        description:
        - "Specify periodic interval in which to renew the certificate"
        type: bool
        required: False
    minute:
        description:
        - "Periodic interval in minutes"
        type: int
        required: False
    renew_every_type:
        description:
        - "'hour'= Periodic interval in hours; 'day'= Periodic interval in days; 'week'=
          Periodic interval in weeks; 'month'= Periodic interval in months(1 month=30
          days);"
        type: str
        required: False
    renew_every_value:
        description:
        - "Value of renewal period"
        type: int
        required: False
    key_length:
        description:
        - "'1024'= Key size 1024 bits; '2048'= Key size 2048 bits(default); '4096'= Key
          size 4096 bits; '8192'= Key size 8192 bits;"
        type: str
        required: False
    method:
        description:
        - "'GET'= GET request; 'POST'= POST request;"
        type: str
        required: False
    interval:
        description:
        - "Interval time in seconds to poll when SCEP response is PENDING (default 5)"
        type: int
        required: False
    max_polltime:
        description:
        - "Maximum time in seconds to poll when SCEP response is PENDING (default 180)"
        type: int
        required: False
    uuid:
        description:
        - "uuid of the object"
        type: str
        required: False
    user_tag:
        description:
        - "Customized tag"
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
    "dn",
    "encrypted",
    "enroll",
    "interval",
    "key_length",
    "log_level",
    "max_polltime",
    "method",
    "minute",
    "name",
    "password",
    "renew_before",
    "renew_before_type",
    "renew_before_value",
    "renew_every",
    "renew_every_type",
    "renew_every_value",
    "secret_string",
    "subject_alternate_name",
    "url",
    "user_tag",
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
        'name': {
            'type': 'str',
            'required': True,
        },
        'url': {
            'type': 'str',
        },
        'dn': {
            'type': 'str',
        },
        'subject_alternate_name': {
            'type': 'dict',
            'san_type': {
                'type': 'str',
                'choices': ['email', 'dns', 'ip']
            },
            'san_value': {
                'type': 'str',
            }
        },
        'enroll': {
            'type': 'bool',
        },
        'log_level': {
            'type': 'int',
        },
        'password': {
            'type': 'bool',
        },
        'secret_string': {
            'type': 'str',
        },
        'encrypted': {
            'type': 'str',
        },
        'renew_before': {
            'type': 'bool',
        },
        'renew_before_type': {
            'type': 'str',
            'choices': ['hour', 'day', 'week', 'month']
        },
        'renew_before_value': {
            'type': 'int',
        },
        'renew_every': {
            'type': 'bool',
        },
        'minute': {
            'type': 'int',
        },
        'renew_every_type': {
            'type': 'str',
            'choices': ['hour', 'day', 'week', 'month']
        },
        'renew_every_value': {
            'type': 'int',
        },
        'key_length': {
            'type': 'str',
            'choices': ['1024', '2048', '4096', '8192']
        },
        'method': {
            'type': 'str',
            'choices': ['GET', 'POST']
        },
        'interval': {
            'type': 'int',
        },
        'max_polltime': {
            'type': 'int',
        },
        'uuid': {
            'type': 'str',
        },
        'user_tag': {
            'type': 'str',
        }
    })
    return rv


def existing_url(module):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/pki/scep-cert/{name}"

    f_dict = {}
    f_dict["name"] = module.params["name"]

    return url_base.format(**f_dict)


def new_url(module):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/pki/scep-cert/{name}"

    f_dict = {}
    f_dict["name"] = ""

    return url_base.format(**f_dict)


def report_changes(module, result, existing_config, payload):
    change_results = copy.deepcopy(result)
    if not existing_config:
        change_results["modified_values"].update(**payload)
        return change_results

    config_changes = copy.deepcopy(existing_config)
    for k, v in payload["scep-cert"].items():
        v = 1 if str(v).lower() == "true" else v
        v = 0 if str(v).lower() == "false" else v

        if config_changes["scep-cert"].get(k) != v:
            change_results["changed"] = True
            config_changes["scep-cert"][k] = v

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
    payload = utils.build_json("scep-cert", module.params,
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
                    "scep-cert"] if info != "NotFound" else info
            elif module.params.get("get_type") == "list":
                get_list_result = api_client.get_list(module.client,
                                                      existing_url(module))
                result["axapi_calls"].append(get_list_result)

                info = get_list_result["response_body"]
                result["acos_info"] = info[
                    "scep-cert-list"] if info != "NotFound" else info
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

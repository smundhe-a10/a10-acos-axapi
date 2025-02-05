#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Copyright 2021 A10 Networks
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

REQUIRED_NOT_SET = (False, "One of ({}) must be set.")
REQUIRED_MUTEX = (False, "Only one of ({}) can be set.")
REQUIRED_VALID = (True, "")

DOCUMENTATION = r'''
module: a10_slb_template_dns
description:
    - DNS template
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
        - "DNS Template Name"
        type: str
        required: True
    default_policy:
        description:
        - "'nocache'= Cache disable; 'cache'= Cache enable;"
        type: str
        required: False
    disable_dns_template:
        description:
        - "Disable DNS template"
        type: bool
        required: False
    period:
        description:
        - "Period in minutes"
        type: int
        required: False
    drop:
        description:
        - "Drop the malformed query"
        type: bool
        required: False
    forward:
        description:
        - "Forward to service group (Service group name)"
        type: str
        required: False
    max_query_length:
        description:
        - "Define Maximum DNS Query Length, default is unlimited (Specify Maximum Length)"
        type: int
        required: False
    max_cache_entry_size:
        description:
        - "Define maximum cache entry size (Maximum cache entry size per VIP)"
        type: int
        required: False
    max_cache_size:
        description:
        - "Define maximum cache size (Maximum cache entry per VIP)"
        type: int
        required: False
    enable_cache_sharing:
        description:
        - "Enable DNS cache sharing"
        type: bool
        required: False
    redirect_to_tcp_port:
        description:
        - "Direct the client to retry with TCP for DNS UDP request"
        type: bool
        required: False
    query_id_switch:
        description:
        - "Use DNS query ID to create sesion"
        type: bool
        required: False
    dnssec_service_group:
        description:
        - "Use different service group if DNSSEC DO bit set (Service Group Name)"
        type: str
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
    class_list:
        description:
        - "Field class_list"
        type: dict
        required: False
        suboptions:
            name:
                description:
                - "Specify a class list name"
                type: str
            uuid:
                description:
                - "uuid of the object"
                type: str
            lid_list:
                description:
                - "Field lid_list"
                type: list
    response_rate_limiting:
        description:
        - "Field response_rate_limiting"
        type: dict
        required: False
        suboptions:
            response_rate:
                description:
                - "Responses exceeding this rate within the window will be dropped (default 5 per
          second)"
                type: int
            filter_response_rate:
                description:
                - "Maximum allowed request rate for the filter. This should match average traffic.
          (default 20 per two seconds)"
                type: int
            slip_rate:
                description:
                - "Every n'th response that would be rate-limited will be let through instead"
                type: int
            window:
                description:
                - "Rate-Limiting Interval in Seconds (default is one)"
                type: int
            enable_log:
                description:
                - "Enable logging"
                type: bool
            action:
                description:
                - "'log-only'= Only log rate-limiting, do not actually rate limit. Requires
          enable-log configuration; 'rate-limit'= Rate-Limit based on configuration
          (Default); 'whitelist'= Whitelist, disable rate-limiting;"
                type: str
            uuid:
                description:
                - "uuid of the object"
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
    "class_list",
    "default_policy",
    "disable_dns_template",
    "dnssec_service_group",
    "drop",
    "enable_cache_sharing",
    "forward",
    "max_cache_entry_size",
    "max_cache_size",
    "max_query_length",
    "name",
    "period",
    "query_id_switch",
    "redirect_to_tcp_port",
    "response_rate_limiting",
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
        'default_policy': {
            'type': 'str',
            'choices': ['nocache', 'cache']
        },
        'disable_dns_template': {
            'type': 'bool',
        },
        'period': {
            'type': 'int',
        },
        'drop': {
            'type': 'bool',
        },
        'forward': {
            'type': 'str',
        },
        'max_query_length': {
            'type': 'int',
        },
        'max_cache_entry_size': {
            'type': 'int',
        },
        'max_cache_size': {
            'type': 'int',
        },
        'enable_cache_sharing': {
            'type': 'bool',
        },
        'redirect_to_tcp_port': {
            'type': 'bool',
        },
        'query_id_switch': {
            'type': 'bool',
        },
        'dnssec_service_group': {
            'type': 'str',
        },
        'uuid': {
            'type': 'str',
        },
        'user_tag': {
            'type': 'str',
        },
        'class_list': {
            'type': 'dict',
            'name': {
                'type': 'str',
            },
            'uuid': {
                'type': 'str',
            },
            'lid_list': {
                'type': 'list',
                'lidnum': {
                    'type': 'int',
                    'required': True,
                },
                'conn_rate_limit': {
                    'type': 'int',
                },
                'per': {
                    'type': 'int',
                },
                'over_limit_action': {
                    'type': 'bool',
                },
                'action_value': {
                    'type': 'str',
                    'choices':
                    ['dns-cache-disable', 'dns-cache-enable', 'forward']
                },
                'lockout': {
                    'type': 'int',
                },
                'log': {
                    'type': 'bool',
                },
                'log_interval': {
                    'type': 'int',
                },
                'dns': {
                    'type': 'dict',
                    'cache_action': {
                        'type': 'str',
                        'choices': ['cache-disable', 'cache-enable']
                    },
                    'ttl': {
                        'type': 'int',
                    },
                    'weight': {
                        'type': 'int',
                    },
                    'honor_server_response_ttl': {
                        'type': 'bool',
                    }
                },
                'uuid': {
                    'type': 'str',
                },
                'user_tag': {
                    'type': 'str',
                }
            }
        },
        'response_rate_limiting': {
            'type': 'dict',
            'response_rate': {
                'type': 'int',
            },
            'filter_response_rate': {
                'type': 'int',
            },
            'slip_rate': {
                'type': 'int',
            },
            'window': {
                'type': 'int',
            },
            'enable_log': {
                'type': 'bool',
            },
            'action': {
                'type': 'str',
                'choices': ['log-only', 'rate-limit', 'whitelist']
            },
            'uuid': {
                'type': 'str',
            }
        }
    })
    return rv


def existing_url(module):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/slb/template/dns/{name}"

    f_dict = {}
    f_dict["name"] = module.params["name"]

    return url_base.format(**f_dict)


def new_url(module):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/slb/template/dns/{name}"

    f_dict = {}
    f_dict["name"] = ""

    return url_base.format(**f_dict)


def report_changes(module, result, existing_config, payload):
    change_results = copy.deepcopy(result)
    if not existing_config:
        change_results["modified_values"].update(**payload)
        return change_results

    config_changes = copy.deepcopy(existing_config)
    for k, v in payload["dns"].items():
        v = 1 if str(v).lower() == "true" else v
        v = 0 if str(v).lower() == "false" else v

        if config_changes["dns"].get(k) != v:
            change_results["changed"] = True
            config_changes["dns"][k] = v

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
    payload = utils.build_json("dns", module.params, AVAILABLE_PROPERTIES)
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
                result[
                    "acos_info"] = info["dns"] if info != "NotFound" else info
            elif module.params.get("get_type") == "list":
                get_list_result = api_client.get_list(module.client,
                                                      existing_url(module))
                result["axapi_calls"].append(get_list_result)

                info = get_list_result["response_body"]
                result["acos_info"] = info[
                    "dns-list"] if info != "NotFound" else info
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

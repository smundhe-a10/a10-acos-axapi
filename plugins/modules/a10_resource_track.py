#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Copyright 2021 A10 Networks
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

REQUIRED_NOT_SET = (False, "One of ({}) must be set.")
REQUIRED_MUTEX = (False, "Only one of ({}) can be set.")
REQUIRED_VALID = (True, "")

DOCUMENTATION = r'''
module: a10_resource_track
description:
    - Define a resource track policy template
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
        - "resource track policy template name"
        type: str
        required: True
    interface:
        description:
        - "Field interface"
        type: list
        required: False
        suboptions:
            ethernet:
                description:
                - "Ethernet Interface (Ethernet interface number)"
                type: str
            weight:
                description:
                - "The failover event weight"
                type: int
    gateway:
        description:
        - "Field gateway"
        type: dict
        required: False
        suboptions:
            gw_ipv4_address_cfg:
                description:
                - "Field gw_ipv4_address_cfg"
                type: list
            gw_ipv6_address_cfg:
                description:
                - "Field gw_ipv6_address_cfg"
                type: list
    bgp:
        description:
        - "Field bgp"
        type: dict
        required: False
        suboptions:
            bgp_ipv4_address_cfg:
                description:
                - "Field bgp_ipv4_address_cfg"
                type: list
            bgp_ipv6_address_cfg:
                description:
                - "Field bgp_ipv6_address_cfg"
                type: list
    trunk_cfg:
        description:
        - "Field trunk_cfg"
        type: list
        required: False
        suboptions:
            trunk:
                description:
                - "trunk tracking (trunk id)"
                type: int
            weight:
                description:
                - "failover event weight"
                type: int
            per_port_weight:
                description:
                - "Per port failover weight"
                type: int
    route:
        description:
        - "Field route"
        type: dict
        required: False
        suboptions:
            ip_destination_cfg:
                description:
                - "Field ip_destination_cfg"
                type: list
            ipv6_destination_cfg:
                description:
                - "Field ipv6_destination_cfg"
                type: list
    vlan_cfg:
        description:
        - "Field vlan_cfg"
        type: list
        required: False
        suboptions:
            vlan:
                description:
                - "VLAN tracking (VLAN id)"
                type: int
            timeout:
                description:
                - "Field timeout"
                type: int
            weight:
                description:
                - "The failover event weight"
                type: int
    scaleout_cfg:
        description:
        - "Field scaleout_cfg"
        type: dict
        required: False
        suboptions:
            scaleout:
                description:
                - "scaleout tracking"
                type: bool
            weight:
                description:
                - "The failover event weight"
                type: int
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
    "bgp",
    "gateway",
    "interface",
    "name",
    "route",
    "scaleout_cfg",
    "trunk_cfg",
    "user_tag",
    "uuid",
    "vlan_cfg",
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
        'interface': {
            'type': 'list',
            'ethernet': {
                'type': 'str',
            },
            'weight': {
                'type': 'int',
            }
        },
        'gateway': {
            'type': 'dict',
            'gw_ipv4_address_cfg': {
                'type': 'list',
                'gw_ipv4_address': {
                    'type': 'str',
                },
                'weight': {
                    'type': 'int',
                }
            },
            'gw_ipv6_address_cfg': {
                'type': 'list',
                'gw_ipv6_address': {
                    'type': 'str',
                },
                'weight': {
                    'type': 'int',
                }
            }
        },
        'bgp': {
            'type': 'dict',
            'bgp_ipv4_address_cfg': {
                'type': 'list',
                'bgp_ipv4_address': {
                    'type': 'str',
                },
                'weight': {
                    'type': 'int',
                }
            },
            'bgp_ipv6_address_cfg': {
                'type': 'list',
                'bgp_ipv6_address': {
                    'type': 'str',
                },
                'weight': {
                    'type': 'int',
                }
            }
        },
        'trunk_cfg': {
            'type': 'list',
            'trunk': {
                'type': 'int',
            },
            'weight': {
                'type': 'int',
            },
            'per_port_weight': {
                'type': 'int',
            }
        },
        'route': {
            'type': 'dict',
            'ip_destination_cfg': {
                'type': 'list',
                'ip_destination': {
                    'type': 'str',
                },
                'mask': {
                    'type': 'str',
                },
                'weight': {
                    'type': 'int',
                },
                'gateway': {
                    'type': 'str',
                },
                'distance': {
                    'type': 'int',
                },
                'protocol': {
                    'type': 'str',
                    'choices': ['any', 'static', 'dynamic']
                }
            },
            'ipv6_destination_cfg': {
                'type': 'list',
                'ipv6_destination': {
                    'type': 'str',
                },
                'weight': {
                    'type': 'int',
                },
                'gatewayv6': {
                    'type': 'str',
                },
                'distance': {
                    'type': 'int',
                },
                'protocol': {
                    'type': 'str',
                    'choices': ['any', 'static', 'dynamic']
                }
            }
        },
        'vlan_cfg': {
            'type': 'list',
            'vlan': {
                'type': 'int',
            },
            'timeout': {
                'type': 'int',
            },
            'weight': {
                'type': 'int',
            }
        },
        'scaleout_cfg': {
            'type': 'dict',
            'scaleout': {
                'type': 'bool',
            },
            'weight': {
                'type': 'int',
            }
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
    url_base = "/axapi/v3/resource-track/{name}"

    f_dict = {}
    f_dict["name"] = module.params["name"]

    return url_base.format(**f_dict)


def new_url(module):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/resource-track/{name}"

    f_dict = {}
    f_dict["name"] = ""

    return url_base.format(**f_dict)


def report_changes(module, result, existing_config, payload):
    change_results = copy.deepcopy(result)
    if not existing_config:
        change_results["modified_values"].update(**payload)
        return change_results

    config_changes = copy.deepcopy(existing_config)
    for k, v in payload["resource-track"].items():
        v = 1 if str(v).lower() == "true" else v
        v = 0 if str(v).lower() == "false" else v

        if config_changes["resource-track"].get(k) != v:
            change_results["changed"] = True
            config_changes["resource-track"][k] = v

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
    payload = utils.build_json("resource-track", module.params,
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
                    "resource-track"] if info != "NotFound" else info
            elif module.params.get("get_type") == "list":
                get_list_result = api_client.get_list(module.client,
                                                      existing_url(module))
                result["axapi_calls"].append(get_list_result)

                info = get_list_result["response_body"]
                result["acos_info"] = info[
                    "resource-track-list"] if info != "NotFound" else info
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

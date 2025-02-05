#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Copyright 2021 A10 Networks
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

REQUIRED_NOT_SET = (False, "One of ({}) must be set.")
REQUIRED_MUTEX = (False, "Only one of ({}) can be set.")
REQUIRED_VALID = (True, "")

DOCUMENTATION = r'''
module: a10_axdebug
description:
    - Packet Trace Options
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
    count:
        description:
        - "Maximum packets to capture per cpu. Default is 3000. (Maximum packets to
          capture. For umlimited, specify 0)"
        type: int
        required: False
    incoming:
        description:
        - "Incoming interface. (For all ports, don't specify port number.)"
        type: bool
        required: False
    inc_port_num:
        description:
        - "Port Numbers separated by commas(,) and hyphens(-) without spaces. ex=
          4,5,10-30, or separated by spaces and double-quoted(')"
        type: str
        required: False
    outgoing:
        description:
        - "Outgoing interface (For all ports, don't specify port number.)"
        type: bool
        required: False
    out_port_num:
        description:
        - "Port Numbers separated by commas(,) and hyphens(-) without spaces. ex=
          4,5,10-30, or separated by spaces and double-quoted(')"
        type: str
        required: False
    length:
        description:
        - "Packet length to capture"
        type: int
        required: False
    maxfile:
        description:
        - "Maximum number of debug packet files. Default is 100"
        type: int
        required: False
    sess_filter_dis:
        description:
        - "Disable session based filter"
        type: bool
        required: False
    timeout:
        description:
        - "Maximum number of minutes for a capture. Default is 5 minutes. For unlimited,
          specify 0"
        type: int
        required: False
    uuid:
        description:
        - "uuid of the object"
        type: str
        required: False
    apply_config:
        description:
        - "Field apply_config"
        type: dict
        required: False
        suboptions:
            config_file:
                description:
                - "config file name"
                type: str
    save_config:
        description:
        - "Field save_config"
        type: dict
        required: False
        suboptions:
            config_file:
                description:
                - "config file name"
                type: str
            default:
                description:
                - "save to default config file"
                type: bool
    delete:
        description:
        - "Field delete"
        type: dict
        required: False
        suboptions:
            capture_file:
                description:
                - "Delete a capture file (Specify target filename to change)"
                type: str
            config_file:
                description:
                - "Delete AXDebug config file (Specify target filename to change)"
                type: str
    exit:
        description:
        - "Field exit"
        type: dict
        required: False
        suboptions:
            stop_capture:
                description:
                - "stop capture traffic"
                type: bool
    capture:
        description:
        - "Field capture"
        type: dict
        required: False
        suboptions:
            brief:
                description:
                - "Print basic packet information"
                type: bool
            detail:
                description:
                - "Include packet payload"
                type: bool
            save:
                description:
                - "Save packets into file (Specify filename to save packets)"
                type: str
            current_slot:
                description:
                - "Only for current-slot of chassis"
                type: bool
    filter_config_list:
        description:
        - "Field filter_config_list"
        type: list
        required: False
        suboptions:
            number:
                description:
                - "Specify filter id"
                type: int
            l3_proto:
                description:
                - "'arp'= arp; 'neighbor'= neighbor;"
                type: str
            dst:
                description:
                - "Destination"
                type: bool
            src:
                description:
                - "Src"
                type: bool
            ip:
                description:
                - "IP"
                type: bool
            ipv4_address:
                description:
                - "ip address"
                type: str
            ipv4_netmask:
                description:
                - "IP subnet mask"
                type: str
            ipv6:
                description:
                - "IPV6"
                type: bool
            ipv6_address:
                description:
                - "ipv6 address"
                type: str
            mac:
                description:
                - "mac address"
                type: bool
            mac_addr:
                description:
                - "mac address"
                type: str
            port:
                description:
                - "port configurations"
                type: bool
            dst_ip:
                description:
                - "dest IP"
                type: bool
            dst_ipv4_address:
                description:
                - "dest ip address"
                type: str
            src_ip:
                description:
                - "src IP"
                type: bool
            src_ipv4_address:
                description:
                - "src ip address"
                type: str
            dst_mac:
                description:
                - "dest mac address"
                type: bool
            dst_mac_addr:
                description:
                - "dest mac address"
                type: str
            src_mac:
                description:
                - "src mac address"
                type: bool
            src_mac_addr:
                description:
                - "src mac address"
                type: str
            dst_port:
                description:
                - "dest port number"
                type: bool
            dst_port_num:
                description:
                - "dest Port number"
                type: int
            src_port:
                description:
                - "src port number"
                type: bool
            src_port_num:
                description:
                - "src Port number"
                type: int
            port_num_min:
                description:
                - "min port number"
                type: int
            port_num_max:
                description:
                - "max port number"
                type: int
            proto:
                description:
                - "ip protocol number"
                type: bool
            proto_val:
                description:
                - "'icmp'= icmp; 'icmpv6'= icmpv6; 'tcp'= tcp; 'udp'= udp;"
                type: str
            prot_num:
                description:
                - "protocol number"
                type: int
            offset:
                description:
                - "byte offset"
                type: int
            length:
                description:
                - "byte length"
                type: int
            oper_range:
                description:
                - "'gt'= greater than; 'gte'= greater than or equal to; 'se'= smaller than or
          equal to; 'st'= smaller than; 'eq'= equal to; 'range'= select a range;"
                type: str
            hex:
                description:
                - "Define hex value"
                type: bool
            min_hex:
                description:
                - " min value"
                type: str
            max_hex:
                description:
                - " max value"
                type: str
            comp_hex:
                description:
                - "value to compare"
                type: str
            integer:
                description:
                - "Define decimal value"
                type: bool
            integer_min:
                description:
                - "min value"
                type: int
            integer_max:
                description:
                - "max value"
                type: int
            integer_comp:
                description:
                - "value to compare"
                type: int
            word:
                description:
                - "Define hex value"
                type: bool
            WORD0:
                description:
                - "WORD0 to compare"
                type: str
            WORD1:
                description:
                - "WORD min value"
                type: str
            WORD2:
                description:
                - "WORD max value"
                type: str
            exit:
                description:
                - "Exit from axdebug mode"
                type: bool
            uuid:
                description:
                - "uuid of the object"
                type: str
            user_tag:
                description:
                - "Customized tag"
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
    "apply_config",
    "capture",
    "count",
    "delete",
    "exit",
    "filter_config_list",
    "inc_port_num",
    "incoming",
    "length",
    "maxfile",
    "out_port_num",
    "outgoing",
    "save_config",
    "sess_filter_dis",
    "timeout",
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
        'count': {
            'type': 'int',
        },
        'incoming': {
            'type': 'bool',
        },
        'inc_port_num': {
            'type': 'str',
        },
        'outgoing': {
            'type': 'bool',
        },
        'out_port_num': {
            'type': 'str',
        },
        'length': {
            'type': 'int',
        },
        'maxfile': {
            'type': 'int',
        },
        'sess_filter_dis': {
            'type': 'bool',
        },
        'timeout': {
            'type': 'int',
        },
        'uuid': {
            'type': 'str',
        },
        'apply_config': {
            'type': 'dict',
            'config_file': {
                'type': 'str',
            }
        },
        'save_config': {
            'type': 'dict',
            'config_file': {
                'type': 'str',
            },
            'default': {
                'type': 'bool',
            }
        },
        'delete': {
            'type': 'dict',
            'capture_file': {
                'type': 'str',
            },
            'config_file': {
                'type': 'str',
            }
        },
        'exit': {
            'type': 'dict',
            'stop_capture': {
                'type': 'bool',
            }
        },
        'capture': {
            'type': 'dict',
            'brief': {
                'type': 'bool',
            },
            'detail': {
                'type': 'bool',
            },
            'save': {
                'type': 'str',
            },
            'current_slot': {
                'type': 'bool',
            }
        },
        'filter_config_list': {
            'type': 'list',
            'number': {
                'type': 'int',
                'required': True,
            },
            'l3_proto': {
                'type': 'str',
                'choices': ['arp', 'neighbor']
            },
            'dst': {
                'type': 'bool',
            },
            'src': {
                'type': 'bool',
            },
            'ip': {
                'type': 'bool',
            },
            'ipv4_address': {
                'type': 'str',
            },
            'ipv4_netmask': {
                'type': 'str',
            },
            'ipv6': {
                'type': 'bool',
            },
            'ipv6_address': {
                'type': 'str',
            },
            'mac': {
                'type': 'bool',
            },
            'mac_addr': {
                'type': 'str',
            },
            'port': {
                'type': 'bool',
            },
            'dst_ip': {
                'type': 'bool',
            },
            'dst_ipv4_address': {
                'type': 'str',
            },
            'src_ip': {
                'type': 'bool',
            },
            'src_ipv4_address': {
                'type': 'str',
            },
            'dst_mac': {
                'type': 'bool',
            },
            'dst_mac_addr': {
                'type': 'str',
            },
            'src_mac': {
                'type': 'bool',
            },
            'src_mac_addr': {
                'type': 'str',
            },
            'dst_port': {
                'type': 'bool',
            },
            'dst_port_num': {
                'type': 'int',
            },
            'src_port': {
                'type': 'bool',
            },
            'src_port_num': {
                'type': 'int',
            },
            'port_num_min': {
                'type': 'int',
            },
            'port_num_max': {
                'type': 'int',
            },
            'proto': {
                'type': 'bool',
            },
            'proto_val': {
                'type': 'str',
                'choices': ['icmp', 'icmpv6', 'tcp', 'udp']
            },
            'prot_num': {
                'type': 'int',
            },
            'offset': {
                'type': 'int',
            },
            'length': {
                'type': 'int',
            },
            'oper_range': {
                'type': 'str',
                'choices': ['gt', 'gte', 'se', 'st', 'eq', 'range']
            },
            'hex': {
                'type': 'bool',
            },
            'min_hex': {
                'type': 'str',
            },
            'max_hex': {
                'type': 'str',
            },
            'comp_hex': {
                'type': 'str',
            },
            'integer': {
                'type': 'bool',
            },
            'integer_min': {
                'type': 'int',
            },
            'integer_max': {
                'type': 'int',
            },
            'integer_comp': {
                'type': 'int',
            },
            'word': {
                'type': 'bool',
            },
            'WORD0': {
                'type': 'str',
            },
            'WORD1': {
                'type': 'str',
            },
            'WORD2': {
                'type': 'str',
            },
            'exit': {
                'type': 'bool',
            },
            'uuid': {
                'type': 'str',
            },
            'user_tag': {
                'type': 'str',
            }
        }
    })
    return rv


def existing_url(module):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/axdebug"

    f_dict = {}

    return url_base.format(**f_dict)


def new_url(module):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/axdebug"

    f_dict = {}

    return url_base.format(**f_dict)


def report_changes(module, result, existing_config, payload):
    change_results = copy.deepcopy(result)
    if not existing_config:
        change_results["modified_values"].update(**payload)
        return change_results

    config_changes = copy.deepcopy(existing_config)
    for k, v in payload["axdebug"].items():
        v = 1 if str(v).lower() == "true" else v
        v = 0 if str(v).lower() == "false" else v

        if config_changes["axdebug"].get(k) != v:
            change_results["changed"] = True
            config_changes["axdebug"][k] = v

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
    payload = utils.build_json("axdebug", module.params, AVAILABLE_PROPERTIES)
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
                    "axdebug"] if info != "NotFound" else info
            elif module.params.get("get_type") == "list":
                get_list_result = api_client.get_list(module.client,
                                                      existing_url(module))
                result["axapi_calls"].append(get_list_result)

                info = get_list_result["response_body"]
                result["acos_info"] = info[
                    "axdebug-list"] if info != "NotFound" else info
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

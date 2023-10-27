## Table of Contents
1. [Overview](#Overview)

2. [How to install Ansbile on Ubuntu](#How-to-install-Ansbile-on-Ubuntu)

3. [How to install Ansbile on MacOS](#How-to-install-Ansbile-on-MacOS)

4. [How to install A10 Ansible modules](#How-to-install-A10-Ansible-modules)

5. [How to configure A10 Ansible modules](#How-to-A10-Ansible-modules)

6. [How to use A10 Ansible module collections](#How-to-use-A10-Ansible-module-collections)

7. [How to search Ansible module configuration](#How-to-search-Ansible-module-configuration)

8. [How to create new Ansible playbook example](#How-to-create-new-Ansible-playbook-example)

9. [How to execute Ansible playbooks from CLI](#How-to-execute-Ansible-playbooks-from-CLI)

10. [How to verify on Thunder](#How-to-verify-on-Thunder)

11. [How to change Thunder Password](#How-to-change-Thunder-Password)

12. [How to contribute](#How-to-contribute)

13. [Documentation](#Documentation)

14. [Test cases](#Test-cases)

15. [License](#License)

16. [Open Source Disclaimer](#Open-Source-Disclaimer)

17. [Report a issue](#Report-a-Issue)

18. [Support](#Support)

## Overview

#### Summary
This repository is a set of Ansible modules and example playbooks for interacting with AXAPI v3 for configuration of A10 ACOS-based hardware and virtual appliances. The module code and example playbooks are generated using a combination of Python code and Jinja templates.

We only support Ansible version >=2.9

This code is now being generated using the SDK generator at https://github.com/a10networks/sdkgenerator

## How to install Ansbile on Ubuntu
To install Ansible on Ubuntu, Run the following command to download and install the latest version of Ansible:

```
apt install ansible
```

## How to install Ansbile on MacOS
To install Ansible on MacOS, Run the following command to download and install the latest version of Ansible:

```
brew install ansible
```

## How to install A10 Ansible modules
a10-acos-axapi is collection of custom ansible modules crated by a10Networks. It can be installed using following ways, it is assumed that ansible is already installed and configured.

### 1. Install from galaxy hub

`ansible-galaxy collection install a10.acos_axapi`

Be sure to note the collection path found within the output of the above command. For example:
```bash
$ ansible-galaxy collection install a10.acos_axapi
Process install dependency map
Starting collection install process
Installing 'a10.acos_axapi:1.0.0' to '/opt/.ansible/collections/ansible_collections/a10/acos_axapi'
```

In this example the collection directory path is: `/opt/.ansible/collections/ansible_collections/`

### 2. Install from the Github repository

  ~~~
  git clone https://github.com/a10networks/a10-acos-axapi
  cd a10-acos-axapi
  ansible-galaxy collection build
  ansible-galaxy collection install a10-acos_axapi*.tar.gz -p ./collections
  ~~~

## How to configure A10 Ansible Modules

#### 1. Set plugin path

Add below line in the `/etc/ansible/ansible.cfg` file

```bash
action_plugins  = <collection-dir-path>/a10/acos_axapi/plugins/action
```

#### 2. Alternative methods to set path

  1. Copy action plugin into one of the following
     - ~/.ansible/plugins
     - /usr/share/ansible/plugins folder

  2. Export following environment variables for new session

  ```bash
  export ANSIBLE_ACTION_PLUGINS=<collection-dir-path>/a10/acos_axapi/plugins/action
  ```

  3. Save this variable in .bashrc File

  ```bash
  export ANSIBLE_ACTION_PLUGINS=<collection-dir-path>/a10/acos_axapi/plugins/action
  ```



## How to use A10 Ansible module collections
Ansible collections are a powerful way to organize and distribute Ansible content, such as roles, modules, and plugins.

Action and module names are formatted based upon their API endpoint. For example, the virtual server endpoint is as follows: /axapi/v3/slb/virtual-server. As such, the action name is a10_slb_virtual_server and the module is a10_slb_virtual_server.py.

**Note that when getting information, changes made to the playbook will not result in a create, update or delete as the state has been put into no-op.

### Creating / updating a resource
Any of the following method can be used to create and run playbooks.

#### 1: Use the 'collections' keyword

```yaml
collections:
  - a10.acos_axapi

tasks:
  - module_name:
    - argument
  - module_name:
    - argument
```

#### 2: Use the Fully Qualified Collection Name (namespace.collection_name.module_name)

```yaml
tasks:
  - a10.acos_axapi.module_name:
    - argument
  - a10.acos_axapi.module_name:
    - argument
```

### Deleting a resource
<pre>
- name: &lt;Description of playbook&gt;
  connection: local
  hosts: &lt;inventory_hostname&gt;
  tasks:
    - name: &lt;Description of task&gt;
      &lt;a10.acos_axapi.module_name&gt;:
        &lt;resource_key&gt;: &lt;resource_val&gt;
        &lt;another_resource_key&gt;: &lt;another_resource_val&gt;
        <b>state: absent</b>
</pre>

### Getting information about a single object
<pre>
- name: &lt;Description of playbook&gt;
  connection: local
  hosts: &lt;inventory_hostname&gt;
  tasks:
    - name: &lt;Description of task&gt;
      &lt;a10.acos_axapi.module_name&gt;:
        &lt;resource_key&gt;: &lt;resource_val&gt;
        &lt;another_resource_key&gt;: &lt;another_resource_val&gt;
        <b>state: noop</b>
        <b>get_type: single</b>
</pre>

### Getting information about a collection
<pre>
- name: &lt;Description of playbook&gt;
  connection: local
  hosts: &lt;inventory_hostname&gt;
  tasks:
    - name: &lt;Description of task&gt;
      &lt;a10.acos_axapi.module_name&gt;:
        &lt;resource_key&gt;: &lt;resource_val&gt;
        &lt;another_resource_key&gt;: &lt;another_resource_val&gt;
        <b>state: noop</b>
        <b>get_type: list</b>
</pre>

### Getting operational information
<pre>
- name: &lt;Description of playbook&gt;
  connection: local
  hosts: &lt;inventory_hostname&gt;
  tasks:
    - name: &lt;Description of task&gt;
      &lt;a10.acos_axapi.module_name&gt;:
        &lt;resource_key&gt;: &lt;resource_val&gt;
        &lt;another_resource_key&gt;: &lt;another_resource_val&gt;
        <b>state: noop</b>
        <b>get_type: oper</b>
</pre>

### Getting statistic information
<pre>
- name: &lt;Description of playbook&gt;
  connection: local
  hosts: &lt;inventory_hostname&gt;
  tasks:
    - name: &lt;Description of task&gt;
      &lt;a10.acos_axapi.module_name&gt;:
        &lt;resource_key&gt;: &lt;resource_val&gt;
        &lt;another_resource_key&gt;: &lt;another_resource_val&gt;
        <b>state: noop</b>
        <b>get_type: stats</b>
</pre>

### Configuring a resource on a partition
<pre>
- name: &lt;Description of playbook&gt;
  connection: local
  hosts: &lt;inventory_hostname&gt;
  tasks:
    - name: &lt;Description of task&gt;
      &lt;a10.acos_axapi.module_name&gt;:
        <b>a10_partition: {{ partition_name }}</b>
        &lt;resource_key&gt;: &lt;resource_val&gt;
        &lt;another_resource_key&gt;: &lt;another_resource_val&gt;
</pre>

### Configuring a resource in a different device context
<pre>
- name: &lt;Description of playbook&gt;
  connection: local
  hosts: &lt;inventory_hostname&gt;
  tasks:
    - name: &lt;Description of task&gt;
      &lt;a10.acos_axapi.module_name&gt;:
        <b>a10_device_context_id: {{ device_context_id }}</b>
        &lt;resource_key&gt;: &lt;resource_val&gt;
        &lt;another_resource_key&gt;: &lt;another_resource_val&gt;
</pre>

### Uploading a file directly
*Note: Only available in modules with `file_path` argument*

<pre>
- name: &lt;Description of playbook&gt;
  connection: local
  hosts: &lt;inventory_hostname&gt;
  tasks:
    - name: &lt;Description of task&gt;
      &lt;a10.acos_axapi.module_name&gt;:
        <b>file_path: "/path/to/file"</b>
        &lt;resource_key&gt;: &lt;resource_val&gt;
        &lt;another_resource_key&gt;: &lt;another_resource_val&gt;
</pre>

### Check Mode
Check mode can be specified in two ways:

<pre>
- name: &lt;Description of playbook&gt;
  connection: local
  hosts: &lt;inventory_hostname&gt;
  tasks:
    - name: &lt;Description of task&gt;
      &lt;a10.acos_axapi.module_name&gt;:
        &lt;resource_key&gt;: &lt;resource_val&gt;
        &lt;another_resource_key&gt;: &lt;another_resource_val&gt;
        <b>check_mode: yes</b>
</pre>

or

```bash
$ ansible-playbook -i <path_to_inventory> <playbook_name>.yml --check-mode
```


## How to search Ansible module configuration
To search for a Ansible Module Configuration in the existing examples, perform the following steps:

  1. Search the required Ansible Module configuration script directory navigate to examples > single_task directory.

     **Example:**

      If you want to apply the bgp router configuration on Thunder, search for the bgp directory under the single_task directory.

  2. Open the Ansible playbook from the directory.

     **Example:**

      Open a10_bgp_create.yaml playbook under the single_task directory.

  3. Update the **hosts** parameter in playbook and add, modify, or remove the Ansible module configuration parameters and their corresponding values as appropriate.

  ```
  - name: Create bgp example playbook
    connection: local
    hosts: "{{desired_inventory_group}}"
    tasks:
    - name: Create router bgp for acos
      a10.acos_axapi.a10_router_bgp:
        as_number: 106
  ```

  4. Save the playbook.

## How to create new Ansible playbook example

Here are step-by-step instructions for creating ansible playbook example.
For example if you want to apply bgp router configuration on thunder and which doesn't exist in examples.

1. Create a new directory to house your ansible playbook files.

```
  mkdir bgp
  cd bgp
```

2. Create a `.yaml` file, such as `a10_bgp_create.yaml`, in your "bgp" directory. In this file, define the ROUTER BGP configurations. Refer to the official documentation: https://documentation.a10networks.com/docs/IaC/Ansible/ansible/  for the required parameters.

  Here is basic example:

    - name: Create bgp example playbook
      connection: local
      hosts: "{{desired_inventory_group}}"        # Replace with your desired hosts
      tasks:
      - name: Create router bgp for acos
        a10.acos_axapi.a10_router_bgp:            # Replace with your desired module name
          as_number: 106                          # Replace with your desired bgp number

Adjust the BGP configuration parameters as needed.


## How to execute Ansible playbooks from CLI

### 1. With Inventory file
Sample Inventory file:

```shell
[vthunder]
<vthunder host_name/ip_address>

[vthunder:vars]
ansible_username=<username>
ansible_password=<password>
ansible_port=<port>
```

If you want to use an Inventory file to perform respective configurations through a playbook, you don't need to specify `ansible_host`, `ansible_username`, `ansible_password` and `ansible_port` in the playbook.

For example,
```
- name: <Description of playbook>
  connection: local
  hosts: <inventory_hostname>
  collections:
    <a10.acos_axapi>
  tasks:
    - name: <Description of task>
      <module_name>:
        <resource_key>: <resource_val>
        <another_resource_key>: <another_resource_val>
```

Use the following command to run playbook using an Inventory file parameters:
```shell
ansible-playbook -i <path_to_inventory> <name_of_playbook>
```

### 2. Without Inventory file
If you don't want to use Inventory file, then specify `ansible_host`, `ansible_username`, `ansible_password` and `ansible_port` arguments into playbook itself with hosts as `localhost`. And then the configurations will be performed on provided `ansible_host`.

For example,
```
- name: <Description of playbook>
  connection: local
  hosts: localhost
  collections:
    <a10.acos_axapi>
  tasks:
    - name: <Description of task>
      <module_name>:
        ansible_host: {{ ansible_host }}
        ansible_username: {{ ansible_username }}
        ansible_password: {{ ansible_password }}
        ansible_port: {{ ansible_port }}
        <resource_key>: <resource_val>
        <another_resource_key>: <another_resource_val>
```

Use the following command to run the playbook with local arguments:
```shell
ansible-playbook <name_of_playbook>
```

Use the following command to run the playbook:
```shell
ansible-playbook -i <path_to_inventory> <name_of_playbook>
```


## How to verify on Thunder

  To verify the applied configurations, follow below steps:

  1. SSH into the Thunder device using your username and password.
  2. Once connected, enter the following commands:

     1. `enable`

        ![image](https://github.com/smundhe-a10/terraform-provider-thunder/assets/107971633/7e532cee-fa8e-4af7-aa50-da56a24dd4c3)


     3. `show running-config`

        ![image](https://github.com/smundhe-a10/terraform-provider-thunder/assets/107971633/ae37e53d-c650-43f0-b71f-2416f4e5d65a)

## How to change Thunder password
```
Please refer : /examples/single_task/admin/adminPassword/README.md
```

## How to contribute

If you have created a new example, please save the playbook file with a module-specific name, such as 'a10_bgp_create.yaml,' in a module name directory, like 'bgp'.

1. Clone the repository.
2. Copy the newly created playbook directory and place it under the /examples/single_task directory.
3. Create a MR against the master branch.

## Documentation

A10 Thunder AXAPI support documentation available at https://documentation.a10networks.com/docs/IaC/Ansible/ansible/

## Test Cases
Sample test cases added for the following configurations:
  - Bgp
  - Check Mode
  - Class List
  - Default Gateway
  - files
  - Gslb
  - Health
  - Network
  - Slb
  - Slb Template

### Run test cases
To test configurations on the acos using ansible playbooks goto ``` test ``` directory and use the following command:
```bash
sh run_test_playbooks.sh

```

## License
[APACHE LICENSE VERSION 2.0](LICENSE.txt)

All rights reserved @A10 Networks Inc.

## Open Source Disclaimer

	For more information, please refer [/OPEN-SOURCE-DISCLAIMER.pdf]
	For more open source licenses, please refer [/LICENSES]


## Report a Issue

Please raise issue in github repository. Please include the Ansible playbook or ansible module files that demonstrates the bug and the command output and stack traces will be helpful.

## Support
For all issues, please send an email to support@a10networks.com

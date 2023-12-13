#!/usr/bin/python


#  Copyright (c) 2023 Indijas Subašić (@BosnaZmaj).
#
#  This file is part of dns_query_module.
#
#  dns_query_module is licensed under the MIT License; you may not use this file except in compliance with the License.
#
#  You may obtain a copy of the License at
#
#      https://opensource.org/licenses/MIT
#
#  For the full license text, see LICENSE.

from ansible.module_utils.basic import AnsibleModule
import dns.resolver
import dns.reversename


def forward_dns_query(name, dns_server=None):
    resolver = dns.resolver.Resolver()
    if dns_server:
        resolver.nameservers = [dns_server]

    try:
        answer = resolver.resolve(name)
        ip_add = [ip.address for ip in answer]
        return {
            'name': name,
            'ip_address': ip_add,
            'error': None
        }
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
        return {
            'name': name,
            'ip_address': [],
            'error': None
        }
    except Exception as e:
        return {
            'name': name,
            'ip_address': [],
            'error': str(e)
        }


def reverse_dns_query(ip, dns_server=None):
    resolver = dns.resolver.Resolver()
    if dns_server:
        resolver.nameservers = [dns_server]

    try:
        reverse_name = dns.reversename.from_address(ip)
        answer = resolver.resolve(reverse_name, "PTR")
        hostnames = [str(rdata) for rdata in answer]
        return {
            'ip': ip,
            'hostnames': hostnames,
            'error': None
        }
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
        return {
            'ip': ip,
            'hostnames': [],
            'error': None
        }
    except Exception as e:
        return {
            'ip': ip,
            'hostnames': [],
            'error': str(e)
        }


# Ansible function
def run_module():
    module_args = dict(
        host=dict(type='str', required=False, default=None),
        dns_server=dict(type='str', required=False, default=None),
        ip=dict(type='str', required=False, default=None)
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    if (module.params['host'] is None and module.params['ip'] is None) or \
       (module.params['host'] is not None and module.params['ip'] is not None):
        module.fail_json(msg="Only one parameter (host or ip) must be provided not both")

    if module.params['host']:
        response = forward_dns_query(module.params['host'], module.params['dns_server'])
    else:
        response = reverse_dns_query(module.params['ip'], module.params['dns_server'])

    if response['error']:
        module.fail_json(msg=response['error'], **response)
    else:
        module.exit_json(**response)


def main():
    run_module()


if __name__ == '__main__':
    main()

# DNS Query Ansible Standalone Module

## Overview

The `dns_query` module permits users to do a simple dns query, using either IP or hostname, as part of a learning opportunity.

## Requirements

- Ansible 2.9 or later.
- Python 3.5 or later.
- `dnspython` library. Install it using pip:
  ```bash
  pip install dnspython
  ```
## Features

- Resolve domain names to IP addresses and IP addresses to hostnames.
- Optionally specify a custom DNS server for the query.
- Error handling.

## Installation

### Automated Installation

To simplify few steps and as a good learning opportunity a Bash script is provided.
This script will download the `dns_query.py` module and place it within `~/.ansible/plugins/modules/` directory where Ansible
by default looks for standalone modules. If the directories do not exist, the script will create them for the user.

1. **Download and Run the Script**
   ```bash
   curl -O https://github.com/BosnaZmaj/dns_query_module/get_dns_query.sh
   chmod +x get_dns_query.sh
   ./get_dns_query.sh
   ```
2. **Script Features**  
   * Checks if `curl` command exists and creates `~/.ansible/plugins/modules/` directories if not existing.
   * Checks if `dns_query.py` modules is already installed and warns users of such.

### Manual Installation

If your preference is manual or need to customize the installation:

1. **Download the Module**
   ```bash
   wget https://raw.githubusercontent.com/BosnaZmaj/AnsibleDNSLookup/main/plugins/modules/dns_query.py
   ```
2. **Place the Module**:  
Place the `dns_query.py` file in your Ansible library path, which typically is `~/.ansible/plugins/modules`

## Usage

### Resolving Domain Name to IP Address

To resolve a domain name to its IP address(es):
```yaml
- hosts: localhost
  gather_facts: no
  tasks:
    - name: Resolve domain name to IP
      dns_query:
        host: "example.com"
      register: query_result
```
### Resolving IP Address to Domain Name

To resolve an IP address to its associated domain name(s):
```yaml
- hosts: localhost
  gather_facts: no
  tasks:
    - name: Resolve IP address to domain name
      dns_query:
        ip: "8.8.8.8"
      register: query_result

    - name: Display the domain names
      debug:
        var: query_result
```

### Using a Custom DNS Server
Specify a custom DNS server for the query:
```yaml
- hosts: localhost
  gather_facts: no
  tasks:
    - name: Custom DNS server query
      dns_query:
        host: "example.com"
        dns_server: "8.8.8.8"  # Google's public DNS server
      register: query_result

    - name: Display the query result
      debug:
        var: query_result
```
If there are no DNS records found for either search, an empty list for the query will be returned.

### Parameters

| Parameter | Required | Description                                        | Default |
|-----------|----------|----------------------------------------------------|---------|
| `host`    | No       | The hostname to query (for IP resolution).         | None    |
| `ip`      | No       | The IP address to query (for hostname resolution). | None    |
| `dns`     | No       | Optional custom DNS server IP address.             | None    |

>*Note: Either* `host` *or* `ip` *must be provided.*


## Contributing

Contributions to the `dns_query` module are welcome. Please ensure that your code adheres to the existing style and that all new features
or bug fixes are accompanied by appropriate tests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

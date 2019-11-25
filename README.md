[![Build Status](https://travis-ci.com/frite/ansible-role-recon-python2-tools.svg?branch=master)](https://travis-ci.com/frite/ansible-role-recon-python2-tools)

recon_python2_tools
=========

Ansible role to install python 2 tools.

Role Variables
--------------
The following variables need to be set.

```
clone_tools:
          altdns:
            name: altdns
            url: https://github.com/infosec-au/altdns.git
          censys:
            name: censys-enumeration
            url: https://github.com/0xbharath/censys-enumeration.git
``` 
Handles the tools that you want to `git clone` in the server. 
```
pip_args:
          - altdns
          - censys-enumeration
```
Tools that offer `requirements.txt` files. 

```
        setup_files:
          - altdns
```
Tools that offer `setup.py` files
```
        soft_links:
          censys:
            repo: censys-enumeration
            soft_link: censys-enumeration
            file: censys_enumeration.py
```
Tools that are soft linked `ln`.

Dependencies
------------

It depends on `frite.recon_package_manager`.
If you run it on CentOS, you also need `geerlingguy.repo-epel` to deal with the EPEL release repo.


 Playbook
----------------

    - hosts: servers
      roles:
         - { role: ansible-role-recon-python2-tools, whatever_vars_here }

License
-------

BSD

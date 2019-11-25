import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_altdns(host):
    ''' Test that altdns and the mode is proper.'''
    f = host.file('/usr/local/bin/altdns')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
    assert oct(f.mode) == '0o755'

#!/usr/bin/python
from __future__ import print_function
import sys
import libvirt
from pprint import pprint as pp
import xml.etree.ElementTree as ET


def get_vm_hostnames():
    ns = {'url': 'http://openstack.org/xmlns/libvirt/nova/1.0'}
    conn = libvirt.open('qemu:///system')
    if conn == None:
        print('Failed to open connection to qemu:///system', file=sys.stderr)
        exit(1)

    for i in conn.listAllDomains():
        raw_xml = i.XMLDesc(0)
        root = ET.fromstring(raw_xml)
        for child in root.findall('metadata'):
            for c in child.findall('url:instance', ns):
                for cc in c:
                    if cc.tag == '{%s}name' % ns['url']:
                        print(cc.text)


if __name__ == '__main__':
    get_vm_hostnames()

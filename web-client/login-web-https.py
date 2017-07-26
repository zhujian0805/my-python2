#!/usr/bin/env python
# coding=utf-8
import sys
import requests
from lxml import html, etree
from pprint import pprint
import re
import binascii
import sys

reload(sys)
sys.setdefaultencoding('utf8')


LOGIN_URL = 'https://www.battlenet.com.cn/login/zh/?ref=https://www.battlenet.com.cn/account/management/&app=bam&cr=true'

PAYLOAD = {
    "accountName": sys.argv[1],
    "password": sys.argv[2]
}

session_requests = requests.session()

result = session_requests.get(LOGIN_URL)

tree = html.fromstring(result.text)

authenticity_token = list(set(tree.xpath("//input[@name='csrftoken']/@value")))[0]

PAYLOAD['csrftoken'] = authenticity_token

result = session_requests.post(
    LOGIN_URL,
    data=PAYLOAD,
    headers=dict(referer=LOGIN_URL)
)

ACC_MGMT_URL = 'https://www.battlenet.com.cn/account/management/'

RESULT = session_requests.get(
    ACC_MGMT_URL,
    headers=dict(referer=ACC_MGMT_URL)
)

tree = html.fromstring(RESULT.content.decode('utf8'))
for p in tree.findall(".//p"):
    if isinstance(p.text, unicode) and len(p.text) < 45:
        if re.search(u'土豪的后裔#5424', p.text.decode('utf8')):
            print "Matched"


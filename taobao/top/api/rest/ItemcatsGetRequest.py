'''
Created by auto_sdk on 2014-03-10 13:11:08
'''
from top.api.base import RestApi


class ItemcatsGetRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.cids = None
        self.fields = None
        self.parent_cid = None

    def getapiname(self):
        return 'taobao.itemcats.get'

'''
Created by auto_sdk on 2014-03-10 13:11:08
'''
from top.api.base import RestApi


class WlbInventoryDetailGetRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.inventory_type_list = None
        self.item_id = None
        self.store_code = None

    def getapiname(self):
        return 'taobao.wlb.inventory.detail.get'

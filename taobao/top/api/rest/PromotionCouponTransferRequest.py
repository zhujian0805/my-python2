'''
Created by auto_sdk on 2014-03-10 13:11:08
'''
from top.api.base import RestApi


class PromotionCouponTransferRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.coupon_number = None
        self.receiveing_buyer_name = None

    def getapiname(self):
        return 'taobao.promotion.coupon.transfer'

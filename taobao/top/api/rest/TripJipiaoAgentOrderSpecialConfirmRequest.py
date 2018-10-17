'''
Created by auto_sdk on 2014-03-10 13:11:08
'''
from top.api.base import RestApi


class TripJipiaoAgentOrderSpecialConfirmRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.can_pay = None
        self.fail_memo = None
        self.fail_type = None
        self.order_id = None
        self.pay_latest_time = None

    def getapiname(self):
        return 'taobao.trip.jipiao.agent.order.special.confirm'

'''
Created by auto_sdk on 2014-03-10 13:11:08
'''
from top.api.base import RestApi
class HotelOrderFaceCheckRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.checked = None
		self.checkin_date = None
		self.checkout_date = None
		self.oid = None

	def getapiname(self):
		return 'taobao.hotel.order.face.check'

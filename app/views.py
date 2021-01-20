from app import app 
from flask_restful import Resource, Api, reqparse


api = Api(app)

# Args parser
"""
self.request_data  = {
			"credit_card_number": '5500000000000004',
			"card_holder": "Omambia Dauglous",
			"expiration_date": "12/24",
			"security_code": "990",
			"amount": 0.0344
		}
"""

_process_payment_reqparse =  reqparse.RequestParser()
_process_payment_reqparse.add_argument(
	"credit_card_number", 
	type = str, 
	help="Please provide a valid card number",
	required =  True)

_process_payment_reqparse.add_argument(
	"card_holder", 
	type = str, 
	help="Please provide a card holder full name",
	required =  True)

_process_payment_reqparse.add_argument(
	"expiration_date", 
	type = str, 
	help="Please provide card expiration date e.g 03/24",
	required =  True)

_process_payment_reqparse.add_argument(
	"security_code", 
	type = str, 
	help="Please provide card security code e.g 001")

_process_payment_reqparse.add_argument(
	"amount", 
	help="Please provide amount",
	required =  True)

"""
Assumed Methods
"""
def premium_payment_gateway(amount):
	pass

def expensive_payment_gateway(amount):
	pass

def cheap_payment_gateway(amount):
	pass


class ProcessPayment(Resource):
	def post(self):
		args = _process_payment_reqparse.parse_args(strict=True)

		if type args.amount is decimal.Decimal:
			abort(400, massage: "Your amount must be a valid amount e.g 300.0")
		if len(arags.credit_card_number) != 16:
			abort(400, massage: "Please provide valid credit card number")
		return 
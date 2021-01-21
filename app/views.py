import decimal, json, markdown
from app import app 
from flask import abort
from app import process_payment
from flask_restful import Resource, Api, reqparse


api = Api(app)


class HomePage(Resource):
	def get(self):
		return {"message": "Hello!!"}, 200
	
	def post(self):
		return  {"message" : "Hello"}, 201


api.add_resource(HomePage, "/")
# Args parser
""" Process Payment Argument Parse
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
	type=int,
	help="Please provide amount",
	required =  True)

"""
Assumed External Payment  Service
"""
def premium_payment_gateway(amount):
	pass

def expensive_payment_gateway(amount):
	pass

def cheap_payment_gateway(amount):
	pass


class ProcessPaymentResource(Resource):
	def post(self):
		args = _process_payment_reqparse.parse_args(strict=True)

		payment = process_payment.PaymentProcess(
			args.credit_card_number, 
			args.card_holder, 
			args.expiration_date, 
			args.amount, 
			args.security_code)

		if payment.get_amount() is None:
			abort(400, {
				"massage": "Your amount must be a valid amount and can not be empty e.g 300.0",
				"data": {
					"amount": payment.get_amount()
				}})
		if len(payment.get_credit_card_number()) != 16:
			abort(400, {
				"massage": "Please provide valid credit card number",
				"data": {
					"credit_card_number": payment.get_credit_card_number()
				}})


		if payment.get_amount() < 20:
			cheap_payment_gateway(payment.get_amount())
		elif (payment.get_amount() >  20) and (payment.get_amount() <= 500):
			expensive_payment_gateway(payment.get_amount())

		elif payment.get_amount()  > 500:
			 premium_payment_gateway(payment.get_amount())

		return {
			"message": "Successfully processed your payment",
			"data": {
				"amount": payment.get_amount(),
				"card_holder": args.card_holder 
			}
		}, 200

api.add_resource(ProcessPaymentResource, "/process-payment")
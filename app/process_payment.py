# payment-process.py
import decimal
from flask import abort

class PaymentProcess(object):
	"""
	PaymentProcess ->
		 - Processes and Validates data
		 params:
		 	credit_card_number:  Credit Card valid number,
			card_holder:  Card holder name,
			expiration_date:  expiration date 
			security_code:  Security code ,
			amount: decimal amount
	"""
	
	def __init__(
		self, 
		credit_card_number, 
		card_holder, 
		expiration_date, 
		amount,
		security_code = "", 
		):

		self.credit_card_number =  credit_card_number
		self.card_holder =  card_holder
		self.expiration_date =  expiration_date
		self.security_code =  security_code
		self.amount =  amount

	def get_credit_card_number(self):
		"""Validate the credit card informations"""
		if len(self.credit_card_number) == 16:
			return self.credit_card_number
		r(400, {"message" : "please provide the amount to process"})
		return
	
	def get_card_holder(self):
		"""Valida card holder name is not empty"""
		if self.card_holder is not None:
			return True
		return False

	def get_amount(self):
		"""Validate amount is not None and is a decimal"""
		if self.amount is not None:
			return self.amount
		return abort(400, {"message" : "please provide the amount to process"})



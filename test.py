try:
	import unittest
	import decimal
	from app import app 
	from app import  process_payment
except Exception as e:
	print("Some modules are missing")



class TestProcessPayment(unittest.TestCase):
	"""
	Test for payment process"""

	def setUp(self):
		"""
		Setting up test data"""

		self.payment = process_payment.PaymentProcess("5500000000000004", "Omambia Dauglous", "12/24", 200.0, "990",)

		self.client  =  app.test_client()

	def test_process_payment_is_OK(self):
		"""Test process payment returns status code 200 -  OK"""
		response  =  self.client.post("/process-payment", 
					data = {
						"credit_card_number": "5500000000000004",
						"card_holder": "Omambia Dauglous",
						"expiration_date": "02/24",
						"security_code" : "009",
						"amount": 200})
		self.assertEqual(response.status_code, 200)


	def test_card_number_is_valid(self):
		"""Test that card number provide is correct"""
		card_number  = "5500000000000004"
		self.assertEqual(self.payment.get_credit_card_number(), card_number)

	def test_card_holder_name_is_provided(self):
		"""Test that the card holderfull name is provided"""
		self.assertTrue(self.payment.get_card_holder())

	def test_user_provides_amount_to_process(self):
		"""Test that use provides valid amount and is not empty"""
		amount  = int(200.0)
		print(self.payment.get_amount())
		# test amount is provided
		self.assertTrue(self.payment.get_amount())
		# test that user must provide amound
		self.assertEqual(int(self.payment.get_amount()), amount)




if __name__ == "__main__":
	unittest.main()
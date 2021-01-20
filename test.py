try:
	import unittest
	from app import app 
except Expression as e:
	print("Some modules are missing")


class TestProcessPayment(unittest.TestCase):
	"""
	Test for payment process"""

	def setUp(self):
		"""Setting up test data"""
		self.request_data  = {
			"credit_card_number": '5500000000000004',
			"card_holder": "Omambia Dauglous",
			"expiration_date": "12/24",
			"security_code": "990",
			"amount": 0.0344
		}
	
	def test_process_payment_status_code_200(self):
		tester   = app.test_client(self)
		response  =  tester.post("/process-payment", this.request_data)
		self.assertEqual(response.status_code, 200)
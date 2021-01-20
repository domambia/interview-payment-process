import unittest


"""
Test Process Payment
"""

class TestProcessPayment(unittest.TestCase):

	def setUp(self,):
		"""Setting Up the test case data"""
		self.request_data  = {
			"credit_card_number": '5500000000000004',
			"card_holder": "Omambia Dauglous",
			"expiration_date": "12/24",
			"security_code": "990",
			"amount": 0.0344
		}
	
	def test_request_has_all_request_data(self):
		self.assertTrue(True)
	

if __name__ == "__main__":
	unittest.main()
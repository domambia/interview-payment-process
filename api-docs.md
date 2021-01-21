# Payment Process Service 

## Usage

All response will have  the following form
```json
{
	"data":"Mixed type(s) holding the content of the response",
	"message": "Human readable description of what happened"
}
```

The following response will only show the required `data fields`

### Process Payment

**Defination**

`POST {{BASE_URL}}/process-payment`

**Request**
```json
{
	"credit_card_number": '5500000000000004',
	"card_holder": "Omambia Dauglous",
	"expiration_date": "12/24",
	"security_code": "290",
	"amount": 200.0
}
```

**Response**

- `200 OK`  on success

```json
{
	"message": "Successfully processed your payment",
	data: {
		"amount": 200.0,
		"card_holder": "Omambia Dauglous"
	} 
}
```

- `400 bad request` on invalid data

```json
{
	"message": "Some help message goes here"
}
```

- `500 server error` on server error and any other error
  
```json
{
	"message": "Server error"
}
```


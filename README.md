# Paymob Unified Checkout Integration (Intention API)

This project demonstrates how to integrate with **Paymob’s Intention API** to create a payment request and redirect the customer to the **Unified Checkout Page** using the new flow.

---

## 📌 Requirements
- Python 3.9+  
- `requests` library  
- `python-dotenv` library  

---

## ⚙️ Setup Instructions

1. **Clone the repository**  
   ```bash
   git clone https://github.com/your-username/paymob-checkout.git
   cd paymob-checkout
Create and activate virtual environment (optional but recommended)

bash
Copy
Edit
python -m venv venv
source venv/bin/activate   # for Linux/Mac
venv\Scripts\activate      # for Windows
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Create your .env file by copying .env.example

bash
Copy
Edit
cp .env.example .env
Fill in your .env with real values from Paymob Dashboard:

env
Copy
Edit
SECRET_KEY=your_secret_key_here
PUBLIC_KEY=your_public_key_here
INTEGRATION_ID=your_integration_id_here
REDIRECTION_URL=https://yourapp.com/thank-you
NOTIFICATION_URL=https://yourapp.com/paymob/webhook
▶️ Usage
Run the script to generate a checkout link:

bash
Copy
Edit
python paymob_checkout.py 150.0
150.0 is the amount in EGP.

The script will:

Create an Intention via Paymob API.

Log request & response.

Print a checkout link to complete payment.

Example Output:

arduino
Copy
Edit
=== OPEN THIS URL TO PAY ===
https://accept.paymob.com/unifiedcheckout/?publicKey=...&clientSecret=...
📩 Webhook (Optional but Recommended)
You can run a simple Flask webhook server to capture transaction updates:

bash
Copy
Edit
python webhook.py
Endpoint: POST http://localhost:5000/paymob/webhook

Logs whether payment was SUCCESS or FAILED.

Use tools like Postman/Ngrok to test webhooks.

📄 Example Request/Response
Request Payload to Intention API:

json
Copy
Edit
{
  "amount": 15000,
  "currency": "EGP",
  "merchant_order_id": "ORD-12345",
  "integration_id": 5243733,
  "payment_methods": ["card"],
  "redirection_url": "https://yourapp.com/thank-you",
  "notification_url": "https://yourapp.com/paymob/webhook",
  "billing_data": {
    "email": "customer@example.com",
    "first_name": "Test",
    "last_name": "User",
    "phone_number": "+201234567890",
    "city": "Cairo",
    "country": "EG"
  }
}
Sample Response:

json
Copy
Edit
{
  "id": 987654,
  "amount": 15000,
  "currency": "EGP",
  "client_secret": "cs_test_123456789",
  "status": "pending"
}
📌 Deliverables
paymob_checkout.py → Handles Intention creation + checkout URL

webhook.py → Optional webhook receiver

.env.example → Example secrets file

README.md → Documentation (this file)

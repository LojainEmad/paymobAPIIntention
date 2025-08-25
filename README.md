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
   ```

2. **Create and activate virtual environment (optional but recommended)**  
   ```bash
   python -m venv venv
   source venv/bin/activate   # for Linux/Mac
   venv\Scripts\activate      # for Windows
   ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Create your `.env` file** by copying `.env.example`  
   ```bash
   cp .env.example .env
   ```

5. **Fill in your `.env` with real values from Paymob Dashboard:**  
   ```env
   SECRET_KEY=your_secret_key_here
   PUBLIC_KEY=your_public_key_here
   INTEGRATION_ID=your_integration_id_here
   REDIRECTION_URL=https://yourapp.com/thank-you
   NOTIFICATION_URL=https://yourapp.com/paymob/webhook
   ```

---

## ▶️ Usage

Run the script to generate a checkout link:

```bash
python paymob_checkout.py 150.0
```

- `150.0` is the amount in **EGP**.  
- The script will:
  1. Create an **Intention** via Paymob API.
  2. Log request & response.
  3. Print a **checkout link** to complete payment.

Example Output:
```
=== OPEN THIS URL TO PAY ===
https://accept.paymob.com/unifiedcheckout/?publicKey=...&clientSecret=...
```

---

## 📩 Webhook (Optional but Recommended)

You can run a simple Flask webhook server to capture transaction updates:

```bash
python webhook.py
```

- Endpoint: `POST http://localhost:5000/paymob/webhook`  
- Logs whether payment was **SUCCESS** or **FAILED**.  
- Use tools like Postman/Ngrok to test webhooks.

---

## 📄 Example Request/Response

**Request Payload to Intention API:**
```json
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
```

**Sample Response:**
```json
{
  "id": 987654,
  "amount": 15000,
  "currency": "EGP",
  "client_secret": "cs_test_123456789",
  "status": "pending"
}
```

---

## 📌 Deliverables
- `paymob_checkout.py` → Handles Intention creation + checkout URL  
- `webhook.py` → Optional webhook receiver  
- `.env.example` → Example secrets file  
- `README.md` → Documentation (this file)  

---

## 🎥 Demo
👉 [Google Drive Demo Link](https://drive.google.com/file/d/1-DgRUJqt_leedNSArsbTDWF-V9nD78Dv/view?usp=sharing) 

---

## 🛠️ Tech Notes
- Language: **Python** (`requests`, `python-dotenv`)  
- Logs all API requests & responses for debugging.  
- Flow:
  1. Generate Intention
  2. Get `client_secret`
  3. Redirect user to Unified Checkout Page  

---

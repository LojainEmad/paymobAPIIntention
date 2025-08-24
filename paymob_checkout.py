import os, json, uuid
from dotenv import load_dotenv
import requests
from flask import Flask, render_template_string, redirect, request
load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
PUBLIC_KEY = os.getenv("PUBLIC_KEY")
INTEGRATION_ID = int(os.getenv("INTEGRATION_ID"))
REDIRECTION_URL = os.getenv("REDIRECTION_URL")
NOTIFICATION_URL = os.getenv("NOTIFICATION_URL")

API_BASE = "https://accept.paymob.com"
INTENTION_URL = f"{API_BASE}/v1/intention/"

app = Flask(__name__)

def create_intention(amount_egp: float, merchant_order_id: str):
    payload = {
        "amount": int(amount_egp * 100),
        "currency": "EGP",
        "merchant_order_id": merchant_order_id,
        "integration_id": INTEGRATION_ID,
        "payment_methods": [INTEGRATION_ID],
        "redirection_url": REDIRECTION_URL,
        "notification_url": NOTIFICATION_URL,
        "billing_data": {
            "apartment": "NA",
            "email": "customer@example.com",
            "floor": "NA",
            "first_name": "Test",
            "last_name": "User",
            "phone_number": "+201234567890",
            "street": "NA",
            "building": "NA",
            "shipping_method": "NA",
            "postal_code": "NA",
            "city": "Cairo",
            "country": "EG",
            "state": "NA"
        }
    }

    headers = {
        "Authorization": f"Bearer {SECRET_KEY}",
        "Content-Type": "application/json"
    }

    resp = requests.post(INTENTION_URL, headers=headers, json=payload, timeout=30)
    data = resp.json()
    if resp.status_code >= 300 or "client_secret" not in data:
        raise RuntimeError(f"Failed to create intention: {data}")

    return data["client_secret"]

def build_checkout_url(client_secret: str) -> str:
    return f"{API_BASE}/unifiedcheckout/?publicKey={PUBLIC_KEY}&clientSecret={client_secret}"

@app.route("/")
def product_page():
    return render_template_string("""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>E-Shop</title>
  <style>
    body {
      font-family: 'Arial', sans-serif;
      background: #ffffff;
      margin: 0;
      padding: 0;
      color: #333;
    }
    .container {
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
    }
    .card {
      background: #f0f0f0; /* light gray */
      border-radius: 20px;
      padding: 50px;
      width: 450px; /* bigger size */
      text-align: center;
      box-shadow: 0 8px 20px rgba(0,0,0,0.1);
    }
    .card img {
      width: 100%;
      border-radius: 15px;
      margin-bottom: 20px;
    }
    .card h2 {
      margin: 15px 0;
      font-size: 28px;
      color: #222;
    }
    .card p {
      font-size: 20px;
      color: #444;
    }
    button {
      background: #333;
      color: #fff;
      border: none;
      padding: 14px 25px;
      border-radius: 12px;
      cursor: pointer;
      font-size: 18px;
      margin-top: 20px;
      transition: 0.3s;
    }
    button:hover {
      background: #555;
      transform: scale(1.05);
    }
  </style>
</head>
<body>
  <div class="container">
    <div class="card">
      <img src="{{ url_for('static', filename='still-life-books-versus-technology.jpg') }}" alt="Laptop">
      <h2>Dell Laptop</h2>
      <p>Price: <strong>55000 EGP</strong></p>
      <form action="/buy" method="post">
        <button type="submit">Buy Now</button>
      </form>
    </div>
  </div>
</body>
</html>
    """)
@app.route("/buy", methods=["POST"])
def buy_now():
    order_id = f"ORD-{uuid.uuid4().hex[:8].upper()}"
    client_secret = create_intention(55000, order_id)
    checkout_url = build_checkout_url(client_secret)
    return redirect(checkout_url)

if __name__ == "__main__":
    app.run(port=5000, debug=True)

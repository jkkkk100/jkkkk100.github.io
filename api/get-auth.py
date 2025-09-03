import hmac, hashlib, time, random, os
from flask import Flask, request

app = Flask(__name__)
SECRET = os.getenv("CHATBASE_SECRET")

@app.route("/api/get-auth", methods=["GET", "POST"])
def get_auth():
    if not SECRET:
        return {"error": "CHATBASE_SECRET not set"}, 500
    user_id = f"guest_{int(time.time() * 1000)}_{random.randint(1000, 9999)}"  # 增加毫秒精度
    auth_token = hmac.new(SECRET.encode(), user_id.encode(), hashlib.sha256).hexdigest()
    return {"userId": user_id, "authToken": auth_token}

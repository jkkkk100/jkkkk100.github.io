import hmac, hashlib, time, random, os
from flask import Flask, request

app = Flask(__name__)
SECRET = os.getenv("CHATBASE_SECRET")  # 从环境变量读取密钥

@app.route("/api/get-auth", methods=["GET", "POST"])
def get_auth():
    if not SECRET:
        return {"error": "CHATBASE_SECRET environment variable is not set"}, 500
    user_id = request.json.get("userId") if request.json else f"guest_{int(time.time())}_{random.randint(1000,9999)}"
    auth_token = hmac.new(
        SECRET.encode(), user_id.encode(), hashlib.sha256
    ).hexdigest()
    return {
        "userId": user_id,
        "authToken": auth_token
    }

if __name__ == "__main__":
    app.run()

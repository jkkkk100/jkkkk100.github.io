import hmac, hashlib, time, random, os
from flask import Request

SECRET = os.getenv("CHATBASE_SECRET")  # 从环境变量读取密钥

def handler(request: Request):
    if not SECRET:
        raise ValueError("CHATBASE_SECRET environment variable is not set")
    user_id = f"guest_{int(time.time())}_{random.randint(1000,9999)}"
    auth_token = hmac.new(
        SECRET.encode(), user_id.encode(), hashlib.sha256
    ).hexdigest()
    return {
        "userId": user_id,
        "authToken": auth_token
    }

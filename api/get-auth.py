# api/get-auth.py
import hmac, hashlib, time, random, os
from flask import Request

# 从环境变量中加载密钥
SECRET = os.environ.get("CHATBASE_SECRET") 

def handler(request: Request):
    # 确保密钥已加载
    if not SECRET:
        return {"error": "Missing CHATBASE_SECRET environment variable"}, 500

    # 随机生成 userId
    user_id = f"guest_{int(time.time())}_{random.randint(1000,9999)}"

    # 生成 authToken
    auth_token = hmac.new(
        SECRET.encode(), user_id.encode(), hashlib.sha256
    ).hexdigest()

    return {
        "userId": user_id,
        "authToken": auth_token
    }

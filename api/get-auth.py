# api/get-auth.py
import hmac, hashlib, time, random
from flask import Request

SECRET = "rhkigrqj0ci7ora0a1iuoz602qjm07d7"  # 你的 Chatbase 密钥

def handler(request: Request):
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

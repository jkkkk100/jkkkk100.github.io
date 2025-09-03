import json
import hmac
import hashlib
import base64
import time
import random

def handler(request):
    bot_id = "06_63h9wgHu7IeP5wxk1m"
    secret = b"你的Secret"

    user_id = f"guest_{int(time.time()*1000)}_{random.randint(0,99999)}"
    message = (user_id + bot_id).encode("utf-8")
    signature = hmac.new(secret, message, hashlib.sha256).digest()
    auth_token = base64.urlsafe_b64encode(signature).decode("utf-8").rstrip("=")

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({"userId": user_id, "authToken": auth_token, "botId": bot_id})
    }

import time, hashlib, hmac, json
SECRET=b"key"

def issue_authorization_artifact(action, state):
    payload_obj = {
        "action": action,
        "state": state,
        "t": int(time.time())
    }
    payload = json.dumps(payload_obj, sort_keys=True)
    sig = hmac.new(SECRET, payload.encode(), hashlib.sha256).hexdigest()
    return {"payload": payload, "sig": sig}

def verify(artifact):
    expected = hmac.new(SECRET, artifact["payload"].encode(), hashlib.sha256).hexdigest()
    return expected == artifact["sig"]

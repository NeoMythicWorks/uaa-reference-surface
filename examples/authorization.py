import time, hashlib, hmac, json
SECRET=b"key"

def issue_authorization_artifact(action, state):
    payload = json.dumps({"a":action,"t":int(time.time())})
    sig = hmac.new(SECRET, payload.encode(), hashlib.sha256).hexdigest()
    return {"payload":payload,"sig":sig}

def verify(artifact):
    expected = hmac.new(SECRET, artifact["payload"].encode(), hashlib.sha256).hexdigest()
    return expected == artifact["sig"]

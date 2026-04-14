import json
def canonicalize_action(action):
    return json.dumps(action, sort_keys=True)

from canonicalize import canonicalize_action
from admissibility import evaluate_admissibility
from authorization import issue_authorization_artifact
from control_point import verify_at_control_point

def run():
    action={"type":"WRITE"}
    state={"allow_execution":True}

    ok,msg=verify_at_control_point(None)
    print("[BLOCKED]",msg)

    artifact={"payload":"bad","sig":"bad"}
    ok,msg=verify_at_control_point(artifact)
    print("[BLOCKED]",msg)

    if evaluate_admissibility(action,state):
        artifact=issue_authorization_artifact(action,state)

    ok,msg=verify_at_control_point(artifact)
    print("[EXECUTED]",msg)

run()

from authorization import verify
def verify_at_control_point(artifact):
    if not artifact:
        return False,"no authorization artifact"
    if not verify(artifact):
        return False,"invalid authorization artifact"
    return True,"action permitted"

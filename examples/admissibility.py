def evaluate_admissibility(action, state):
    return state.get("allow_execution", False)

def explain_risk(weather, risk):
    """
    LLM-style human readable explanation
    """
    return (
        f"For the {weather['location']}, the sea conditions indicate a "
        f"{risk['risk_level']} risk today. "
        f"Fishermen are advised to {risk['advice'].lower()}. "
        f"Recommended fishing zone: {risk['zone']}. "
        f"Safe till: {risk['safe_till']}."
    )

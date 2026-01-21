def check_safety(user_query):
    """
    Analyzes the user's query for high-risk keywords associated with 
    electrical hazards or hardware damage.
    
    Args:
        user_query (str): The raw text input from the user.
        
    Returns:
        tuple: (is_safe: bool, warning_message: str)
    """
    # Define high-risk keywords
    risk_keywords = [
        "power supply", "psu", "capacitor", "solder", "soldering", 
        "open case", "disassemble", "mains", "220v", "110v", "shock",
        "smoke", "spark", "burning smell"
    ]
    
    query_lower = user_query.lower()
    
    for keyword in risk_keywords:
        if keyword in query_lower:
            warning_msg = (
                f"SAFETY ALERT: High-risk keyword detected ('{keyword}').\n\n"
                "This task involves a significant risk of electrical shock or hardware damage. "
                "I cannot provide instructions for opening power supply units or soldering components.\n\n"
                "RECOMMENDATION: Unplug the device immediately and consult a certified technician."
            )
            return False, warning_msg
            
    return True, ""
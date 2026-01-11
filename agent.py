def agent_decide(state, data):
    """
    Decide whether the user can continue based on the current task state.

    Parameters:
        state (str): The current step of the task
        data (dict): User-provided application data

    Returns:
        message (str): Short feedback message (<= 120 characters)
        confidence (str): Low, Medium, or High
        can_continue (bool): Whether the user can move forward
    """

    #Collect profile
    if state == "collect_profile":
        missing_fields = [key for key in data if data[key] == "" or data[key] is None]

        if missing_fields:
            return "Profile incomplete. Please fill all fields.", "Low", False

        return "Profile captured successfully.", "Medium", True

    #Collect documents
    elif state == "collect_documents":
        cv_uploaded = data.get("cv_uploaded")
        portfolio = data.get("portfolio")

        if not cv_uploaded:
            return "A CV is required to continue.", "Low", False

        if data.get("role") == "Software Engineering" and (portfolio is None or portfolio == ""):
            return "Portfolio required for Software Engineering roles.", "Low", False

        return "Documents captured successfully.", "Medium", True

    #Validation
    elif state == "validate":
        role = data.get("role")
        portfolio = data.get("portfolio")

        if role == "Software Engineering" and (portfolio is None or portfolio == ""):
            return "Portfolio required for Software Engineering roles.", "Low", False

        return "All application requirements are satisfied.", "High", True

    #Review
    elif state == "review":
        return "Application ready for final review.", "High", True

    return "Unable to determine application state.", "Low", False

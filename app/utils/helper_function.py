def validate_email(email):
    """
    Validates the email format.
    """
    return "@" in email and "." in email

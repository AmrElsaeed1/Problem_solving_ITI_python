def is_valid_email(email):
    try:
        if not email:
            raise ValueError("Email cannot be empty.")

        local_part, domain_part = email.split('@')

        domain_part.index('.')

        if domain_part.startswith('.') or domain_part.endswith('.'):
            raise ValueError("Domain part cannot start or end with '.'.")

        invalid_chars = set(" ,;()<>[]")
        if any(char in invalid_chars for char in email):
            raise ValueError("Email contains invalid characters.")

        return "The email is valid."

    except ValueError as e:
        print(f"Invalid email: {e}")
        return False
    except Exception as e:
        print(f"Invalid email: Unexpected error{e}.")
        return False

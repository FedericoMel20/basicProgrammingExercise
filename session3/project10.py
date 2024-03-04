def extract_domain(email):
    try:
        # Split the email address by '@' symbol
        parts = email.split('@')
        if len(parts) == 2:
            # Return the second part which represents the domain name
            return parts[0]
        else:
            return None
    except Exception as e:
        print("Error:", e)
        return None

# Get user input
user_email = input("Enter your email address: ")

# Extract domain name
domain = extract_domain(user_email)

# Print domain name
if domain:
    print("Domain:", domain)
else:
    print("Invalid email address entered.")

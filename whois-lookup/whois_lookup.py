import whois

def whois_lookup(domain):
    """
    Perform a WHOIS lookup for the given domain.

    Args:
        domain (str): The domain name to look up.

    Returns:
        str: WHOIS information for the domain.
    """
    try:
        return whois.whois(domain)
    except Exception as e:
        return f"Error: {e}"

# Example usage
domain = input("Enter the domain name to look up: ")
whois_info = whois_lookup(domain)
print(whois_info)


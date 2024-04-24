import requests

def shorten_url(long_url, token):
    """
    Shorten the given URL using the Bitly API.

    Args:
        long_url (str): The URL to be shortened.
        token (str): Your Bitly access token.

    Returns:
        str: Shortened URL.
    """
    endpoint = "https://api-ssl.bitly.com/v4/shorten"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    data = {
        "long_url": long_url
    }
    response = requests.post(endpoint, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()["link"]
    else:
        print("Failed to shorten URL. Status code:", response.status_code)
        return None

# Example usage
long_url = input("Enter the URL to shorten: ")
access_token = "YOUR_BITLY_ACCESS_TOKEN"
short_url = shorten_url(long_url, access_token)
if short_url:
    print("Shortened URL:", short_url)


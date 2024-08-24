from typing import Dict
import requests

def get_json(url: str) -> Dict:
    """Get JSON from remote URL.
    """
    response = requests.get(url)
    return response.json()


url = "https://jsonplaceholder.typicode.com/users/1"
user_data = get_json(url)

print(user_data)
#for key, value in user_data.items():
#	print(key, "--", value)

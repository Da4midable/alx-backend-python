from typing import Dict
import requests

def get_json(url: str) -> Dict:
    """Get JSON from remote URL.
    """
    response = requests.get(url)
    return response.json()


"""url = "https://jsonplaceholder.typicode.com/users/1"
user_data = get_json(url)

print(user_data)
for key, value in user_data.items():
    print(key, "--", value)"""
    
def test_get_json():
    test_cases = [("http://example.com", {"payload": True}), ("http://holberton.io", {"payload": False})]
    for url, payload in test_cases:
        print(url, ":", payload['payload'])
test_get_json()

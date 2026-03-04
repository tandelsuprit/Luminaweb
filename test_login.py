import requests

# Test the /login endpoint
response = requests.post(
    "http://localhost:8000/login",
    json={"username": "test", "password": "test"}
)
print(f"Status: {response.status_code}")
print(f"Response: {response.json()}")

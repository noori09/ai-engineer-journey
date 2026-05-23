import requests

# Make a GET request to a public API
response = requests.get("https://api.github.com")

# Check what we got back
print("Status code:", response.status_code)
print("Content type:", response.headers.get("Content-Type"))
print()
print("First 500 characters of the response:")
print(response.text[:500])
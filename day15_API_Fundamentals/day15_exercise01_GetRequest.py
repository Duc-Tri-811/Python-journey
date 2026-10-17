#Day 15: Exercise 01: Get Request

import requests

url = "https://jsonplaceholder.typicode.com/todos/1"

try:
    # Send GET request with a timeout of 10 seconds to avoid infinite waiting if connection hangs
    response = requests.get(url, timeout=10)
    # Raise an exception if the HTTP status is in the 4xx or 5xx error range
    response.raise_for_status()

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")

print("Status Code:", response.status_code)
print("Response JSON:", response.json())



    
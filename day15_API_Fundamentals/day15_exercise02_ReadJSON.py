#Day 15: Exercise: Read JSON

import requests

url = "https://jsonplaceholder.typicode.com/todos/1"

try:
    # Send Get request with a timeout of 10 seconds to avoid infinite waiting if connection hangs
    response = requests.get(url, timeout=10)
    # Raise an exception of the HTTP status is in the 4xx or 5xx error range
    response.raise_for_status()
    # Convert response to a Python dictionary safely inside the try block
    data = response.json()

    user_id = data["userId"]
    title = data["title"]
    completed = data["completed"]

    print(f"--- Detail information ---")
    print(f"User Id: {user_id}")
    print(f"Title : {title}")
    print(f"Completed status:{completed}")


except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")






#Day 15: Exercise 03: Loop API Data

import requests

url = "https://jsonplaceholder.typicode.com/todos"

try:
    # Send Get request with a timeout of 10 seconds to avoid infinite waiting if connection hangs
    response = requests.get(url, timeout=10)
    # Raise an exception of the HTTP status is in the 4xx or 5xx error rang
    response.raise_for_status()
    # Convert response to a Python dictionary safely inside the try block
    data = response.json()

    #01: Count the total number of records received from API
    total_records = len(data)
    print(f"Total records received from API: {total_records}")

    print(f"---First 10 tasks list ---")

    #02: Loop through the data with safety check  
    for index, item in enumerate(data[:10], start=1):
        # Use.get() to prevent KeyError if the API record is missing "title" or "completed"
        # If the key doesn't exist, it will fallback to "N/A" or False safely
        title = item.get("title", "N/A")
        completed = item.get("completed", False)

        # Optional: Skip processing if critical data is completely missing
        if title == "N/A":
            print(f"Task {index}: Skipped due to missing title data.")
            continue

        print(f"Task {index} | Title: {title} | Completed status: {completed}")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")





# Day 15: Exercise 04: Filter API Data

import requests

url = "https://dummyjson.com/carts"

try:
    # Send Get request with a timeout of 10 seconds to avoid infinite waiting if connection hang
    response = requests.get(url, timeout=10)
    # Raise an exception of the HTTP status is in the 4xx or 5xx error rang
    response.raise_for_status()
    # Convert response to a Python dictionary safety inside the try block
    data = response.json()
    # Safety extract the carts list, fallback to an empty list if key doesn't exist
    carts_list = data.get("carts", [])
    carts_received = len(carts_list)
    print(f"Total carts received: {carts_received}")
    print(f"--- Filtered Orders (Total >= 300) ---")

    # Loop through carts with safety checks
    for cart in carts_list:
        # Use .get() to prevent KeyError if 'total', 'id', or 'userId' is missing from API
        cart_id = cart.get("id","N/A")
        user_id = cart.get("userId", "N/A")
        cart_total = cart.get("total", 0.0)
        # Filter condition based on business requirements, ensuring cart_total is numeric
        if isinstance(cart_total, (int, float)) and cart_total >= 300:
            print(
                f"Cart ID: {cart_id} | User ID: {user_id} | Total Amount: ${cart_total:.2f}"
            )

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")











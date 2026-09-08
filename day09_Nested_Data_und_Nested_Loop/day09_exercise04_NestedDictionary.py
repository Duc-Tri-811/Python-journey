#Exercise 04: Nested Dictionary

customer = {
    "name": "Anna",
    "email": "anna@example.com",
    "address": {
        "street": "Hauptstraße 10",
        "city": "Hannover",
        "country": "Germany"
    }
}


print(f"Customer : {customer['name']}")
print(f"Email : {customer['email']}")
print(f"City : {customer['address']['city']}")
print(f"Country : {customer['address']['country']}")

customer["address"]["city"] = "Sehnde"

print(f"City : {customer['address']['city']}")

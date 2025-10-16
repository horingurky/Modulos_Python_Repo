
customer = {
"id": 1,
"name": "John Doe",
"age": 30,
"is_verified": True,
"balance": 100.5,
"tags": ["premium", "active"],
"address": {
"street": "123 Main St",
"city": "Anytown",
"zip": "12345"
}
}
print(customer)

customer["address"]["street"] = "Otra Calle"
customer.update({"age": 31})

print(customer)

customer["address"].update({"street": "456 Elm St"})

print(customer)

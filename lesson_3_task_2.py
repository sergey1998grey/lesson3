from smartphone import Smartphone


catalog = [
    Smartphone("Apple", "iPhone 15", "+79151849539"),
    Smartphone("Samsung", "Galaxy S24", "+79161849539"),
    Smartphone("Xiaomi", "13", "+79151859539"),
    Smartphone("Google", "Pixel 8", "+79151949539"),
    Smartphone("OnePlus", "11", "+79151849639")
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")

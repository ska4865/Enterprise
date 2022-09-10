import requests
url = "localhost:8080/item"

payload = {
  "name": "Smart Watch",
  "price": 23.57,
  "quantity": 5
}

x = requests.post(url, data = myobj)

print(x.text)
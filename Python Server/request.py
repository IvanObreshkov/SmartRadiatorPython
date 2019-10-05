import requests

# URL
url = 'http://localhost:5000/api'

# Change the value of experience that you want to test
r = requests.post(url,json={"exp": [10, 23]})
print(r.json())
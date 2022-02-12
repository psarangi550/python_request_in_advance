import requests
from requests.exceptions import ReadTimeout
from requests.exceptions import ConnectTimeout


# try:
#     # response = requests.get("https://httpbin.org/delay/10",timeout=15)
#     response = requests.get("https://httpbin.org/delay/10",timeout=5)
# except ReadTimeout as e:
#     print(e)
# else:
#     print(response.text)
#     print(response.status_code)

# response = requests.get("https://httpbin.org/",timeout=0.05)

try:
    # response = requests.get("https://httpbin.org/delay/10",timeout=15)
    response = requests.get("https://httpbin.org/",timeout=0.05)
except ConnectTimeout as e:
    print(e)
else:
    print(response.text)
    print(response.status_code)
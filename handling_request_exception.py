import requests
#handling the HttpError response
from requests.exceptions import HTTPError
#handling Connection Error response
from requests.exceptions import ConnectionError

#:-case:1
# resp=requests.get("https://httpbin.org/status/400")
# resp=requests.get("https://httpbin.org/status/501")
# resp = requests.get("https://httpbin.org/status/405")
# try:
#     resp.raise_for_status()
# except HTTPError as e:
#     print(e)
# else:
#     print(resp.status_code)
#     print(resp.text)

#:-case:-2
#with vpn off
# resp=requests.get("http://httpbin.or")
# try:
#     resp=requests.get("http://httpbin.or")
# except ConnectionError as e:
#     print(e)
# else:
#     print("connection established")


    
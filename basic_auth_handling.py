
import requests
import requests.auth
response=requests.get("http://httpbin.org/basic-auth/rika/abi1997",auth=requests.auth.HTTPBasicAuth('rik','abi1997'))
print(response)
print(response.headers)
print(response.text)
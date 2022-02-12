import requests
import json

# resp=requests.get("http://requestbin.net/r/3fdxdjrd")

##accessing a single user #################################
##accessing a single user from the reqres.in server #################################
resp=requests.get("https://reqres.in/api/users/2")
# print(resp.text)
print(resp.json())
####putting the json data to a file #################################
with open("resp.json",'w') as f:
    json.dump(resp.json(), f,indent=4,sort_keys=True)
    
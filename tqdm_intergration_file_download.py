import requests
from tqdm import tqdm
# print(dir(tqdm))

# resp=requests.get('http://httpbin.org/image')
# print(resp.headers['Content-Type']) #fetchign the content type which is send from httpbin which is of application/json
# print(resp.headers)


resp = requests.get('http://httpbin.org/image/jpeg')
print(resp.headers['Content-Type']) #fetchign the content type which is of jpeg type hence application/jpeg
print(resp.headers['Content-Length'])
# print(help(resp.iter_content))
################################
#writing that to a file by using the tqdm and image file
################################

with open("image.jpeg","wb") as f:#opening the file in the read mode
    for i in tqdm(resp.iter_content(chunk_size=200),total=int(resp.headers["Content-Length"])/200,unit="kb"):
        f.write(i) #writing the chuck on details 
        
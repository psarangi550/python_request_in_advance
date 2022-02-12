import requests
# files={"file":open("python.png","rb")}
# files={("file1", ("python.png", open("python.png", "rb" ),"image/png")),
#        ("file2",("flask.png", open("flask.png", "rb"),"image/png"))}
################## alternate approach is #################################
files={
        "file1":("python.png", open("python.png", "rb" ),"image/png"),
        "file2":("flask.png", open("flask.png", "rb"),"image/png"),
       }
################################################################
resp=requests.post("http://httpbin.org/post",files=files)
print(resp.status_code)
print(resp.text)

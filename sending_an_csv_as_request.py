import requests 

#handling single csv file
# files={"file": open("emp.csv","r")} ##sending  only one file 
# handling multiple csv files
files={
        "file1": ("emp1.csv",open("emp1.csv","r")),
        "file2": ("emp2.csv",open("emp2.csv","r")),
    }
resp=requests.post("https://httpbin.org/post", files=files)
print(resp.status_code)
print(resp.text)

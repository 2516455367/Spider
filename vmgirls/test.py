
import requests

url='https://www.vmgirls.com/14188.html'
headers={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
}

response=requests.get(url,headers=headers)
print(response.status_code)
print(response.text)
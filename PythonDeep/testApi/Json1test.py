import requests
import json


username = 'AlexeyZ1'
password = 'e23970376f'
user_agent_val = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
url = 'https://test-stand.gb.ru/login'
session = requests.Session()
r = session.get(url, headers={
    'User-Agent': user_agent_val
})
session.headers.update({'Referer':url})
session.headers.update({'User-Agent':user_agent_val})
_xsrf = session.cookies.get('_xsrf', domain=".gb.ru")
post_request = session.post(url, {
     'backUrl': 'https://test-stand.gb.ru/login',
     'username': username,
     'password': password,
     '_xsrf':_xsrf
})
with open("teststand_success.html","w",encoding="utf-8") as f:
    f.write(post_request.text)
#после авторизации
url = 'https://test-stand.gb.ru/'
res = requests.get(url)
print('Status Code = ',res.status_code)
with open("teststand_success1.html","w",encoding="utf-8") as f:
    f.write(post_request.text)

data = json.loads(res.text)
print(data)

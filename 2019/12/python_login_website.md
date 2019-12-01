
## A simple example for login to lufy.org with python

```
import requests

def login_admin():
    username = 'yyyyyy'
    password = 'xxxxxx'
    url = 'http://192.168.0.108:8000/admin/login/?next=/admin/'

    
    s = requests.session()
    content = s.get(url)
    
    payload = {
        'username': username,
        'password': password,
        'csrfmiddlewaretoken': content.cookies.items()[0][1]
        }
    
    print(payload['csrfmiddlewaretoken'])
    out = s.post(url, data=payload, headers=dict(referer=url))
    return out
    
    
if __name__ == '__main__':
    t = login_admin()
    print(t.cookies.items())
    print(t.text)
```

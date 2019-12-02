#!/usr/bin/python3
# filename: python_drupal_auto_login.py
# Author: lufei
# Date: 20191202 09:01:46


import requests

def login_admin():
    username = '路斐'
    password = 'abc123'
    url = 'http://tfs.i-soft.com.cn/drupal/'


    s = requests.session()
    content = s.get(url)

    payload = {
        'name': username,
        'pass': password,
        'op': "登录",
        'form-buid-id': content.cookies.items()[0][1],
        'form_id': "user_login_block"
        }

    out = s.post(url, data=payload, headers=dict(referer=url))
    s.get('http://tfs.i-soft.com.cn/drupal/?q=logout')
    s.close()
    return out


if __name__ == '__main__':
    t = login_admin()
    print(t.cookies.items())
    print(t.text)


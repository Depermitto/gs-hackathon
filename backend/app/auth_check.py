import requests

def check_https(url):
    req = requests.get(url)
    return req.url.startswith('https')

def check_cookie_secure(url):
    req = requests.get(url)
    cookies = req.cookies
    for cookie in cookies:
        if cookie.secure:
            return True
    return False
    
def check_cookie_timeout(url):
    req = requests.get(url)
    cookies = req.cookies
    for cookie in cookies:
        if cookie.expires:
            return True
    return False
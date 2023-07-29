import requests
from bs4 import BeautifulSoup

def getFakeMail():
    url = 'https://email-fake.com/'
    req = requests.get(url)
    soup = BeautifulSoup(req.content, "html.parser")
    mail = soup.find_all("span", {"id": "email_ch_text"})
    print(mail)
    print(mail[0])
    return mail[0].contents

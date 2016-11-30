import requests
from bs4 import BeautifulSoup
import re

class KyukoInfo:
    def __init__(self):
        self.date = None
        self.department = None
        self.time = None
        self.teacher = None
        self.subject = None
        self.status = None
    
    def __repr__(self):
        return str(self.__dict__)
    
    def __str__(self):
        return str(self.__dict__)


def fetchKyukoInfo():
    url = 'http://hirose.sendai-nct.ac.jp/kyuko/kyuko.cgi'
    html = requests.get(url).content
    soup = BeautifulSoup(html, 'lxml')
    attrs = {'width': 650}
    kyuko = list()
    for elem in soup.findAll('table', attrs):
        detail = KyukoInfo()
        detail.date = list(re.findall('([0-9]{,2})月([0-9]{,2})日<.*>\((.*)\)</font>', str(elem.b))[0])
        detail.department, detail.time = [x.string for x in elem.select('td font b')]
        detail.teacher = elem.select('td font[color=#00008B]')[0].string.strip()
        detail.subject = elem.select('tr td tr font')[0].string
        detail.status = re.findall('./img/(.*).gif', str(elem.select('img')))[0]
        kyuko.append(detail)
    return kyuko


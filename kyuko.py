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
    
    def __getitem__(self, element):
        if element == 'date':
            return self.date
        elif element == 'department':
            return self.department
        elif element == 'time':
            return self.time
        elif element == 'teacher':
            return self.teacher
        elif element == 'subject':
            return self.subject
        elif element == 'status':
            return status
        else:
           raise IndexError() 


    def __repr__(self):
        return str(self.__dict__)
    
    def __str__(self):
        return str(self.__dict__)

    def to_dict(self):
        return self.__dict__
      


def fetchKyukoInfo():
    url = 'http://hirose.sendai-nct.ac.jp/kyuko/kyuko.cgi'
    html = requests.get(url)
    html.encoding = 'shif_jis'
    soup = BeautifulSoup(html.content, 'html5lib')
    attrs = {'width': 650}
    kyuko = list()
    num_map = {'�T': 'I', '�U': 'II', '�V': 'III'}
    for elem in soup.findAll('table', attrs):
        detail = KyukoInfo()
        detail.date = list(re.findall('([0-9]{,2})月([0-9]{,2})日<.*>\((.*)\)</font>', str(elem.b))[0])
        detail.department, detail.time = [x.string for x in elem.select('td font b')]
        detail.teacher = elem.select('td font[color=#00008B]')[0].string.strip()
        subject = elem.select('tr td tr font')[0].string
        for num in num_map:
            if num in subject:
                subject = subject.replace(num, num_map[num])
        detail.subject = subject
        detail.status = re.findall('./img/(.*).gif', str(elem.select('img')))[0]
        kyuko.append(detail)
    return kyuko

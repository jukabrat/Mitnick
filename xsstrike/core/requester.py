import random
import requests
import time
from urllib3.exceptions import ProtocolError
import warnings
import os
from concurrent.futures import ThreadPoolExecutor

from core.utils import converter, getVar
from core.log import setup_logger

logger = setup_logger(__name__)

warnings.filterwarnings('ignore')  # Disable SSL related warnings

proxybest = []
dane = input("proxy? y/n: ")
if dane == "y":
    os.chdir("../penetrateDir/")
    os.system("start /wait cmd /k python checkproxy.py")
    proxy = open("proxylist.txt")
    lines = proxy.readlines()
    os.chdir("../xsstrike/")

    print("pronalazim najbolji proxy:")
    with ThreadPoolExecutor(len(lines)):
        for line in lines:
            try:
                r = requests.get("https://dnsleaktest.com", proxies={'https' : 'http://'+line})
                print("najbolji: " + line.strip() + " : "+ str(r.status_code))
                print(r.content)
                proxybest.append(line)
                break
            except:
                pass
    proxies = {'https': 'http://'+proxybest[0]}
else:
    proxies = None

def requester(url, data, headers, GET, delay, timeout):
    if getVar('jsonData'):
        data = converter(data)
    elif getVar('path'):
        url = converter(data, url)
        data = []
        GET, POST = True, False
    time.sleep(delay)
    user_agents = ['Mozilla/5.0 (X11; Linux i686; rv:60.0) Gecko/20100101 Firefox/60.0',
                   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
                   'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36 OPR/43.0.2442.991']
    if 'User-Agent' not in headers:
        headers['User-Agent'] = random.choice(user_agents)
    elif headers['User-Agent'] == '$':
        headers['User-Agent'] = random.choice(user_agents)
    logger.debug('Requester url: {}'.format(url))
    logger.debug('Requester GET: {}'.format(GET))
    logger.debug_json('Requester data:', data)
    logger.debug_json('Requester headers:', headers)
    try:
        if GET:
            response = requests.get(url, params=data, headers=headers,
                                    timeout=20, verify=False, proxies=proxies)
        elif getVar('jsonData'):
            response = requests.post(url, json=data, headers=headers,
                                    timeout=20, verify=False, proxies=proxies)
        else:
            response = requests.post(url, data=data, headers=headers,
                                     timeout=20, verify=False, proxies=proxies)
        return response
    except ProtocolError:
        logger.warning('WAF is dropping suspicious requests.')
        logger.warning('Scanning will continue after 10 minutes.')
        time.sleep(600)
    except Exception as e:
        logger.warning('Unable to connect to the target.')
        print(e)
        return requests.Response()
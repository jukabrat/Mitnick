import requests
from fake_useragent import UserAgent
from concurrent.futures import ThreadPoolExecutor

r = requests.get("https://www.remove.bg", proxies={"https":"http://35.238.133.20:3128"})
print(r.status_code)
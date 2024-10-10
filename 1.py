# import requests
from bs4 import BeautifulSoup
import re
import json
from curl_cffi import requests

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Host': 'seatgeek.com',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'
}

url = "https://seatgeek.com/broadway-in-chicago-tickets"
response = requests.get(url, headers=headers)
print(response.status_code)
print(response.cookies['datadome'])
dd_cookie = response.cookies['datadome']

with open('1.html', 'w', encoding='utf-8') as file:
    file.write(response.text)

soup = BeautifulSoup(response.content, 'html.parser')

# Find the <script> tag containing the dd variable
script_tag = soup.find('script')

dd_script = str(script_tag)
print(dd_script)

dd_script = dd_script.replace('<script data-cfasync="false">var dd=', "")
dd_script = dd_script.replace('</script>', "")
print(dd_script)

# Replace single quotes with double quotes
json_string = dd_script.replace("'", '"')

# Parse the string into a JSON object
dd = json.loads(json_string)
# Print the JSON object
print(dd)
print(dd['hsh'])

params = {
    'initialCid': dd['cid'],
    'hash': dd['hsh'],
    'cid': dd_cookie,
    't': dd['t'],
    'referer': url,
    's': dd['s'],
    'e': dd['e'],
    'dm': 'cd'
}

captcha_url = "https://geo.captcha-delivery.com/captcha/"

url = f"{captcha_url}?initialCid={dd['cid']}&hash={dd['hsh']}&cid={dd_cookie}&t={dd['t']}&referer={url}&s={dd['s']}&e={dd['e']}&dm=cd"
url = url.replace("==", "%3D%3D")
url = url.replace("https://seatgeek.com/broadway-in-chicago-tickets", "https%3A%2F%2Fseatgeek.com%2Fbroadway-in-chicago-tickets")
print(url)

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Referer': 'https://seatgeek.com/',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Sec-Fetch-Dest': 'iframe',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'cross-site',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'
}
response = requests.get(url, headers=headers, params=params)

print(response.status_code)
with open('1.html', 'w') as file:
    file.write(response.text)

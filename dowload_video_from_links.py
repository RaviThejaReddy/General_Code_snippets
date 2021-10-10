import requests
import os
import re

url_list = ['url1','url2']

for url in url_list:
    file_name = re.sub('[^0-9a-zA-Z]+','_',url.split('/')[-1])
    r = requests.get(url_string, allow_redirects=True)
    open(file_name, 'wb').write(r.content)

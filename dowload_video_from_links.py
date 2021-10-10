import requests
import os
import re


for x in os.listdir('./'):
    if '.' not in x:
        for y in os.listdir('./'+ x):
            if '.yaml' in y:
                with open('./'+ x + '/'+ y) as yamlfile:
                    urllist = [x for x in yamlfile.readlines() if 'https://' in x]
                    for url in urllist:
                        url_string = url[15:-1]
                        file_name = re.sub('[^0-9a-zA-Z]+','_',url_string.split('/')[-1]).replace('_mp4','.mp4')
                        print(file_name)
                        r = requests.get(url_string, allow_redirects=True)
                        open(file_name, 'wb').write(r.content)
                        

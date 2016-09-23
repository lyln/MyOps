__author__ = 'ljd'

import requests
import json

headers = {'Content-Type':'application/json'}
data = {}
url="http://120.92.3.150:8080/showms/rest/user/getAllReviews"


r = requests.post(url,data=json.dumps(data),headers=headers)

print r.status_code


print type(r)

# print r.json()

for i in r.json()['data']:
    print i['url']
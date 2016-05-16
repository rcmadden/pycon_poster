# -*- coding: utf-8 -*-
'''
Request Url: http://gateway.marvel.com/v1/public/comics
source: http://uxio0.blogspot.com/2015/08/python-tutorial-basico-de-la-api-de.html
'''
from flask import Flask, render_template
from werkzeug.debug import DebuggedApplication
import hashlib
import requests
from secret import PUBLIC_KEY, PRIVATE_KEY
import datetime
import pprint
import json

app = Flask(__name__)
app.wsgi_app = DebuggedApplication(app.wsgi_app, True)

# public = PUBLIC_KEY
# private = PRIVATE_KEY
public = '74e38d12e0c5e226d3559848a5608fa1'
private = '59b8587ec1340d7d98a46eb3594a8c13f957d767'

ts = '1'
# ts = datetime.datetime.now().strftime("%Y-%m-%d%H:%M:%S")
h = hashlib.md5((ts + private + public).encode()).hexdigest()

base = 'http://gateway.marvel.com/v1/public/'
comics = requests.get(base + 'comics',
                      params={'apikey': public,
                              'ts': ts,
                              'hash': h}).json()
characters = requests.get(base + 'characters',
                          params={'apikey': public,
                                  'ts': ts,
                                  'hash': h}).json()
wolverine = requests.get(base + 'characters',
                          params={'apikey': public,
                                  'ts': ts,
                                  'hash': h,
                                  'name': 'wolverine'}).json()
# spiderman = requests.get(base + 'characters',
#                           params={'apikey': public,
#                                   'ts': ts,
#                                   'hash': h,
#                                   'name': 'spider-man'}).json()

attributionHTML = wolverine['attributionHTML']
attributionText = wolverine['attributionText']


for item in characters['data']['results']:
    if "image_not_available" not in item['thumbnail']['path']:
        image_path = item['thumbnail']['path'] + "/portrait_incredible." + item['thumbnail']['extension']
        r = characters.get(image_path)
        print(r)
        if "MAA" not in item['name']:
                with open(item['name']+'.jpg','wb') as fout:
                    fout.write(r.content)
                image = item['name'] + '.jpg'
                print(image)



# @app.route("/")
# def hello():
    # pprint.pprint(spiderman)
    # pprint.pprint(characters['data']['results'])
    # return render_template('index.html', spiderman=spiderman, characters=characters, comics=comics)

# if __name__ == "__main__":
    # app.run(debug=True)
    # hello()

#!/usr/bin/env python
# -*- coding: utf-8 -*-

''' source: https://github.com/aseemm/flask-template/blob/master/marvel.py
'''
from optparse import OptionParser, make_option
from pprint import pprint
import requests
import json
import time
import hashlib
import random
import argparse
import atexit
import sys
import datetime
from pprint import pprint
# import Image
# from cStringIO import StringIO
# from urllib2 import Request, urlopen, URLError
import urllib.request
import urllib.request as Request
import re
import random

# Marvel API keys
marvel_public_key = '138fee76826ac3baf223cb926375c3ca'
marvel_private_key = '2c750c552474676d32ed58082d8f11b27abc43e3'
offset = random.randrange(0, 1475)

def auth(marvel_private_key, marvel_public_key):
        ts = datetime.datetime.now().strftime("%Y-%m-%d%H:%M:%S")
        hash_string =  hashlib.md5(str("%s%s%s" % (ts, marvel_private_key, marvel_public_key)).encode('utf-8')).hexdigest()
        return "ts=%s&apikey=%s&hash=%s" % (ts, marvel_public_key, hash_string)

api_key = auth(marvel_private_key, marvel_public_key)
request = urllib.request('http://gateway.marvel.com:80/v1/public/characters?offset=' + str(offset) + '&limit=5&' + api_key)

try:
    data1 = json.load(urllib.request.urlopen(request))
    for item in data1['data']['results']:
        if "image_not_available" not in item['thumbnail']['path']:
            image_path = item['thumbnail']['path'] + "/portrait_incredible." + item['thumbnail']['extension']
            r = requests.get(image_path)
            i = Image.open(StringIO(r.content))
            if "MAA" not in item['name']:
                with open(item['name']+'.jpg','wb') as fout:
                    fout.write(r.content)
                image = item['name'] + '.jpg'
except URLError:
    print('No kittez. Got an error code:', e)


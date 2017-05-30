# -*- coding: utf-8 -*-
import json
import urllib
import pyperclip

url = "http://catfacts-api.appspot.com/api/facts"

while True:
    req = urllib.request.urlopen(url)
    json_object = json.load(req)
    str1 = ''.join(json_object['facts'])
    pyperclip.copy(str1)

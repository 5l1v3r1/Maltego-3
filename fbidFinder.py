#!/usr/bin/python
# Maltego tranform to get FBID

from MaltegoTransform import *
import requests
import sys
from bs4 import BeautifulSoup

m = MaltegoTransform()
m.parseArguments(sys.argv)


try:
    url = "http://www.findmyfbid.com/"
    post_data = "https://www.facebook.com/" + sys.argv[1]
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:42.0) Gecko/20100101 Firefox/42.0"
    headers = {'User-Agent': user_agent}
    req = requests.post(url, headers=headers, data = { "url": post_data})
    html_data = req.text
    soup = BeautifulSoup(html_data, 'html.parser')
    resp = str(soup.code)
    ugly1 = resp.split(">")
    ugly2 = ugly1[1].split("<")
    if resp == "<code>https://www.facebook.com</code>":
        m.addUIMessage("No ID found :(")
    else:
        m.addEntity('maltego.phrase', ugly2[0])
except Exception as e:
    m.addUIMessage(str(e))

m.returnOutput()

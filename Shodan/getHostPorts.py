#!/usr/bin/python
# Get Shodan results for our host

import sys
import shodan
from api_key import load_key
from MaltegoTransform import *

API_KEY = load_key()

api = shodan.Shodan(API_KEY)
m = MaltegoTransform()
m.parseArguments(sys.argv)

try:
    host = api.host(sys.argv[1])
    if len(host) == 0:
        m.addUIMessage('No data in Shodan')
    else:
        open_ports =  host['ports']
        for port in open_ports:
            m.addEntity('undeadsecurity.Port', str(port))
except Exception as e:
    m.addUIMessage(str(e))

m.returnOutput()

#!/usr/bin/python
# Get Shodan results for our host
# Similar to getHostPortBanners.py but with the Port:Banner in the IP details
# rather than as a separate entity

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
        data =  host['data']
        portentity = m.addEntity('maltego.IPv4Address', str(sys.argv[1]))
        for i, ports in enumerate(data):
            port = host['data'][i]['port']
            banner = host['data'][i]['data']
            port_data = str(port) + ":" + str(banner)
            port_banner_data = portentity.addAdditionalFields(str(port), "Port:Banner", True, str(port_data))

except Exception as e:
    m.addUIMessage(str(e))

m.returnOutput()

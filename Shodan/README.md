Shodan
======

Various Maltego transforms for talking to the Shodan API.
These all require the Paterva Maltego Python library and the Shodan Python library.

Maltego Python Library: https://www.paterva.com/web6/documentation/developer-local.php
Shodan Python Library: https://shodan.readthedocs.org/en/latest/


 * api_key.py - Used by the other modules to load our API key
 * getHostPorts.py - Grab the ports listed by Shodan for our host
 * getHostInfo.py - Grab useful information on our host from Shodan
 * getHostPortBanners.py - Grabs ports and banners for a host
 * getHostPortBannersv2.py - Similar to getHostPortBanners.py but it stores the port details in the IP entity 

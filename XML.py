import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
api_key = False
if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)
    print('Retrieving', url)
    uh = urllib.request.urlopen(url)

    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')
    print(data)
    tree = ET.fromstring(data)

    results = tree.findall('comments/ comment')
    for item in results:
        print('count',item.find('count').data)

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

while True:
    url = input('Enter location: ')


    print('Retrieving', url)
    uh = urllib.request.urlopen(url).read()

    data = uh.decode()
    print('Retrieved', len(data), 'characters')

    tree = ET.fromstring(data)

    count = 0 
    results = tree.findall('comments/comment')
    print('count :',len(results),)
    for item in results:
        x = int(item.find('count').text)
        count = count + x
    print(count)

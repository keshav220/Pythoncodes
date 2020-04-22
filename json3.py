import json
import urllib.request, urllib.parse, urllib.error


url = input("Enter..")
print('Retrieved :',url)

html = urllib.request.urlopen(url)
info = json.loads(html.read())
print('User count:', len(info))
sp = info['comments']
# t = tuple()
count = 0
for item in sp:
    count = count + item['count']
    # x = ('Count:', item['count'])
    # t = t + x
# l = list(t)
print(count)

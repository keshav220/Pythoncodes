import re
handle=open('regex.txt')
hand = handle.read()
count = 0
match = re.findall('[0-9]+',hand)
for i in match:
	number = int(i)
	count = count + number
print(count)

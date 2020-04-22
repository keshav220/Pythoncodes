import re
handle=open('regex.txt')

nums = list()
for line in handle:
    line = line.rstrip()
    x=re.findall('[0-9]+',line)
    if len(x) == 1:
        val = float(x[0])
        nums.append(val)
    
print(int(sum(nums)))

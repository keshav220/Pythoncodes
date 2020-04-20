fh = open('romeo.txt')
lst = list()
result = []
for line in fh:
    line = line.rstrip()
    fil = line.split()
    for k in fil:
        if k not in result:
    	    result.append(k)


result.sort()
print(result)

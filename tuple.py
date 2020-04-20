
handle = open('mbox-short.txt')
newword = []
di = dict()
listVal = list()
for line in handle:
    words = line.split()
    if len(words) < 3:
        continue
    if words[0] != 'From' :
        continue
    w = words[5].split(':')[0] 
    newword.append(w)
    

newword.sort()
for k in newword:
    di[k] = di.get(k,0) + 1
    
for k,v in di.items():
    listVal.append((k,v))
    
listVal = sorted(listVal)

for k,v in listVal:
    print(k, v)


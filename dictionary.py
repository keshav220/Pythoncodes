name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
di = dict()
newword = []
for line in handle :
    line = line.rstrip()    
    words = line.split()
    if len(words) < 3 :
        continue
    if words[0] !='From':
        continue
    newword.append(words[1])
for wds in newword :
    di[wds] = di.get(wds,0) +1
largest = -1 
theword = None
for k,v in di.items():
    
    if v > largest :
        largest = v
        theword = wds
print(theword,largest)        
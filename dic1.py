

handle = open('mbox-short.txt')
for line in handle:
    words = line.split()
    if len(words) < 3:
        continue
    if words[0] != 'From' :
        continue
    print(words[5].split(':')[0])
        
    
    
    

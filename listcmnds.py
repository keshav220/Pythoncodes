N = int(input())
l = []
for _ in range(N):
    s = input().split()
    cmd = s[0]
    val = s[1:]
    if cmd !='print':
        cmd += "("+ ",".join(val) +")"
        eval('l.'+cmd)
    else:
        print(l)    

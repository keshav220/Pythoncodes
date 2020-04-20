largest = 0
smallest = None

result = []
while True:
    num = input("Enter a number: ")
    if num == "done" : break
    try:
        fval = int(num)
        result.append(fval)
    except:
        print('Invalid input')
totalInput = len(result)
for i in range(0,totalInput):
    if smallest == None:
        smallest = result[i]
    if i <totalInput -1:
        if largest<result[i]:
            largest = result [i]
        if smallest>result[i] :
            smallest = result[i]

print("Maximum","is", largest)
print("Minimum","is", smallest)

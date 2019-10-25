counter = 0
dataStream = '00100100'
present = []
for i in range(0,len(dataStream)):
    index = i + 1
    next
    if(index == 1):
        next = int(dataStream[1])
    elif(index == 2):
        next = int(dataStream[0])
    elif(index == 6 or index ==  7 or index == 8):
        next = int(dataStream[i])
    else:
        next = int(dataStream[i]) ^ int(dataStream[7])
    present.append(next)
print(present)




counter = 0
data = ['00100100','10101100','10011100','11100101']
for i in range(0, len(data)):
    present = []
    dataStream = data[i]
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



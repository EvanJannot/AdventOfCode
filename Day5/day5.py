input = open("Day5/input.txt","r")
stacks = [[],[],[],[],[],[],[],[],[]]

countLine = 1
for line in input :
    if countLine <=8 : 
        stacks[0].append(line[1])
        stacks[1].append(line[5])
        stacks[2].append(line[9])
        stacks[3].append(line[13])
        stacks[4].append(line[17])
        stacks[5].append(line[21])
        stacks[6].append(line[25])
        stacks[7].append(line[29])
        stacks[8].append(line[33])
        countLine+=1
    else : 
        countLine = 1
        break

for stack in stacks:
    count = 0
    for element in stack :
        if element == ' ':
            count+=1
    for i in range (0, count):
        stack.remove(' ')


for line in input : 
    if countLine > 1 :
        numberToMove = int(line[5]+line[6])
        whereItIs = int(line[12]+line[13])
        whereToMove = int(line[17]+line[18])
        supplies = []
        for i in range (0, numberToMove):
            supplies.append(stacks[whereItIs-1][i])
        for element in supplies : 
            stacks[whereItIs-1].remove(element)
        supplies.reverse()
        stacks[whereToMove-1] = supplies + stacks[whereToMove-1]
        supplies.clear()
    countLine += 1

print(stacks)
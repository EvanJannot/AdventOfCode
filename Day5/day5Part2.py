input = open("Day5/input.txt","r")

# Count the number of characacters of the first line
# This is the number of columns
columns = len(input.readline())
# Reset the file pointer to the beginning of the file
input.seek(0)
stacks = [[] for i in range(columns//4)]

countLine = 1
for line in input :
    if line[0] == 'm': 
        if len(line) <= 17 :
            break
        else : 
            numberToMove = int(line[5]+line[6])
            whereItIs = int(line[12]+line[13])
            if len(line)>18: 
                whereToMove = int(line[17]+line[18])
            else : 
                whereToMove = int(line[17])
            supplies = []
            for i in range (0, numberToMove):
                supplies.append(stacks[whereItIs-1][i])
            for element in supplies : 
                stacks[whereItIs-1].remove(element)
            stacks[whereToMove-1] = supplies + stacks[whereToMove-1]
            supplies.clear()
    elif line.count('[') :  
        for i in range (0,columns) :
            if i%4 == 1 :
                stacks[((i)//4)].append(line[i]) 
        for stack in stacks:
            count = 0
            for element in stack :
                if element == ' ':
                    count+=1
            for i in range (0, count):
                stack.remove(' ')
    else : 
        pass
    countLine += 1
    


print(stacks)
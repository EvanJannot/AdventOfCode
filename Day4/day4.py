input = open("Day4/input.txt","r")

count = 0
for line in input :
    line = line.replace('-',',')
    elfPair = line.split(',')
    elfPair[3] = elfPair[3].replace('\n','')
    if (int(elfPair[0]) >= int(elfPair[2]) and int(elfPair[1]) <= int(elfPair[3])) :
        count += 1
        print(elfPair)
    elif (int(elfPair[2]) >= int(elfPair[0]) and int(elfPair[3]) <= int(elfPair[1])) :
        count += 1
        print(elfPair)

print(count)
        
        
        




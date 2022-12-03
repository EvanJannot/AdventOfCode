input = open("Day3/input.txt","r")

elfGroup = []
count = 1
priority = 0
for line in input : 
    if count % 3 == 0:
        elfGroup.append(line)
        for char in elfGroup[0]:
            if char in elfGroup[1] and char in elfGroup[2]:
                if char.isupper() :
                    priority += ord(char) - 38
                else :
                    priority += ord(char) - 96
                break
        elfGroup.clear()
        count += 1
    else : 
        elfGroup.append(line)
        count += 1

print(priority)



    
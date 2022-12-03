input = open("Day3/input.txt","r")

compartment1 = ""
compartment2 = ""
priority = 0
for line in input : 
    compartment1 = line[:len(line)//2]
    compartment2 = line[len(line)//2:]
    for char in compartment1:
        if char in compartment2:
            print(char)
            if char.isupper() :
                priority += ord(char) - 38
            else:
                priority += ord(char) - 96
            break
print(priority)


    
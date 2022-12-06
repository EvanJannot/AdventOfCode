input = open("Day6/input.txt","r")

line = input.read()
substring = ""
double = 0
for i in range(len(line)-4) :
    substring = line[i:i+4]
    for char in substring :
        if substring.count(char) >1  :
            double += 1
    if double == 0:
        print(i+4)
        exit()
    double = 0
            
        
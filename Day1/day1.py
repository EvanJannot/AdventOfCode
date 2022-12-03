input = open("Day1/input.txt","r")

mostCalories = 0
mostCaloriesElf = 0
countElf = 1
countCalories = 0
for line in input : 
    if line == "\n" : 
        countElf += 1
        countCalories = 0
        continue 
    else : 
        countCalories += int(line) 
        if mostCalories < countCalories : 
            mostCalories = countCalories
            mostCaloriesElf = countElf 

print(mostCalories)
print(mostCaloriesElf)
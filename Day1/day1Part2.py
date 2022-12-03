input = open("Day1/input.txt","r")

calories = []
countElf = 1
countCalories = 0
for line in input : 
    if line == "\n" : 
        calories.append(countCalories)
        countElf += 1
        countCalories = 0
        continue 
    else : 
        countCalories += int(line) 
calories.append(countCalories)

calories.sort()

total = calories[len(calories)-1] + calories[len(calories)-2] + calories[len(calories)-3]
print(total)
        


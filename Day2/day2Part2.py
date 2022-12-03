input = open("Day2/input.txt","r")

pointsTranslation = {
    "AX" : 3,
    "AY" : 4,
    "AZ" : 8,
    "BX" : 1,
    "BY" : 5,
    "BZ" : 9,
    "CX" : 2,
    "CY" : 6,
    "CZ" : 7,
}

totalPoints = 0
for line in input : 
    firstLetter = line[0]
    secondLetter = line[2]
    pair = firstLetter + secondLetter   
    totalPoints += pointsTranslation[pair]

print(totalPoints)
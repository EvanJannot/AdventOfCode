input = open("Day2/input.txt","r")

pointsTranslation = {
    "X": 1,
    "Y": 2,
    "Z": 3,
    "AX" : 3,
    "AY" : 6,
    "AZ" : 0,
    "BX" : 0,
    "BY" : 3,
    "BZ" : 6,
    "CX" : 6,
    "CY" : 0,
    "CZ" : 3,
}

totalPoints = 0
for line in input : 
    firstLetter = line[0]
    secondLetter = line[2]
    pair = firstLetter + secondLetter   
    totalPoints += pointsTranslation[pair]
    totalPoints += pointsTranslation[secondLetter]

print(totalPoints)
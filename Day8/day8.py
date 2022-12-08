input = open("Day8/input.txt","r")
input = input.read().splitlines()

nonVisibles = 0
visibles = len(input)

for i in range (len(input)-1):
    visibles += len(input[i])
    for j in range (len(input[i])-1):
        if i != 0 and i != len(input)-1 and j != 0 and j != len(input[i])-1:
            rowBefore = input[i][:j]
            rowAfter = input[i][j+1:]
            colonneBefore = ''
            colonneAfter = ''
            hidingTrees = 0
            for k in range(i):
                colonneBefore += input[k][j]
            for k in range(i+1,len(input)):
                colonneAfter += input[k][j]

            for tree in rowBefore:
                if tree >= input[i][j] :
                    hidingTrees += 1
                    break
            for tree in rowAfter:
                if tree >= input[i][j] :
                    hidingTrees += 1
                    break
            for tree in colonneBefore:
                if tree >= input[i][j] :
                    hidingTrees += 1
                    break
            for tree in colonneAfter:
                if tree >= input[i][j] :
                    hidingTrees += 1
                    break
            if hidingTrees == 4 : 
                nonVisibles += 1

            
print(visibles- nonVisibles)
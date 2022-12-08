input = open("Day8/input.txt","r")
input = input.read().splitlines()

visibles = len(input)
bestScenic = 0

for i in range (len(input)-1):
    visibles += len(input[i])
    for j in range (len(input[i])-1):
        if i != 0 and i != len(input)-1 and j != 0 and j != len(input[i])-1:
            rowBefore = input[i][:j]
            rowBefore = rowBefore[::-1]
            rowAfter = input[i][j+1:]
            colonneBefore = ''
            colonneAfter = ''
            scenicU = 0
            scenicD = 0
            scenicL = 0
            scenicR = 0
            scenic = 0
            for k in range(i):
                colonneBefore += input[k][j]
            for k in range(i+1,len(input)):
                colonneAfter += input[k][j]
            colonneBefore = colonneBefore[::-1]
            for tree in rowBefore:
                if tree < input[i][j] :
                    scenicU += 1
                else:
                    scenicU += 1
                    break
            for tree in rowAfter:
                if tree < input[i][j] :
                    scenicD += 1
                else:
                    scenicD += 1
                    break
            for tree in colonneBefore:
                if tree < input[i][j] :
                    scenicL += 1
                else:
                    scenicL += 1
                    break
            for tree in colonneAfter:
                if tree < input[i][j] :
                    scenicR += 1
                else:
                    scenicR += 1
                    break
            scenic = scenicU * scenicD * scenicL * scenicR
            if scenic > bestScenic:
                bestScenic = scenic
            
print(bestScenic)
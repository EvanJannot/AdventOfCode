input = open("Day8/input.txt","r").read().splitlines()

gridSize = len(input)-1
bestScenic = 0

def column(matrix, i):
    return [row[i] for row in matrix]

for i in range (gridSize):
    for j in range (gridSize):
        if i != 0 and i != gridSize and j != 0 and j != len(input[i])-1:
            rowBefore = input[i][:j][::-1]
            rowAfter = input[i][j+1:]
            columnBefore = column(input,j)[0:i][::-1]
            columnAfter = column(input,j)[i+1:gridSize+1]
            scenic = [0,0,0,0,0]
            for tree in rowBefore:
                if tree < input[i][j] :
                    scenic[0] += 1
                else:
                    scenic[0] += 1
                    break
            for tree in rowAfter:
                if tree < input[i][j] :
                    scenic[1] += 1
                else:
                    scenic[1] += 1
                    break
            for tree in columnBefore:
                if tree < input[i][j] :
                    scenic[2] += 1
                else:
                    scenic[2] += 1
                    break
            for tree in columnAfter:
                if tree < input[i][j] :
                    scenic[3] += 1
                else:
                    scenic[3] += 1
                    break
            scenic[4] = scenic[0] * scenic[1] * scenic[2] * scenic[3]
            if scenic[4] > bestScenic:
                bestScenic = scenic[4]
            
print(bestScenic)
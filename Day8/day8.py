input = open("Day8/input.txt","r").read().splitlines()

gridSize = len(input)-1
visibles = len(input)*4 - 4

def column(matrix, i):
    return [row[i] for row in matrix]

for i in range (gridSize):
    for j in range (gridSize):
        if i != 0 and i != gridSize and j != 0 and j != len(input[i])-1:
            rowBefore = input[i][:j]
            rowAfter = input[i][j+1:]
            columnBefore = column(input,j)[0:i]
            columnAfter = column(input,j)[i+1:gridSize+1]
            visibleUp = all( tree < input[i][j] for tree in columnBefore)
            visibleDown = all( tree < input[i][j] for tree in columnAfter)
            visibleLeft = all( tree < input[i][j] for tree in rowBefore)
            visibleRight = all( tree < input[i][j] for tree in rowAfter)
            if visibleUp or visibleDown or visibleLeft or visibleRight :
                visibles += 1
            
print(visibles)
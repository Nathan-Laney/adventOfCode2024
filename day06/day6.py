import time
# Turn input into 2d array
# Array holds either: 
# '#' for obstacle, '.' for unvisited, 
# 'X' for visited, and '^' '<' '>' 'V' for up left right and down respectively

map = []
obstacles = ""
def createMap(fileName):
    tempMap = []
    with open(fileName, 'r') as file:
        for line in file:
            tempMap.append(list(line.strip()))
    return tempMap

def findGuard(map): 
    for i in range(len(map)):
        # print(i)
        # print(map)
        for j in range(len(map[i])):
            if map[i][j] == '^':
                # print('Iterating.')
                return((i, j))

def moveGuard(mapArray, obstacles, guardCoords):
    pass
    row, column = guardCoords[0], guardCoords[1]
    # check their orientation
    # check the block one in front of that orientation
    # if it's an obstacle, rotate the guard 90degrees. 
    # if it's the end of the map, call it done
    # if it's not, put the guard there. 
    # if mapArray[row][column] in ('<', '>', '^', 'V'):
        # print("Guard!")
        # Handle Left
    if mapArray[row][column] == '<':
        if column == 0:
            return "Exit", obstacles, guardCoords
        if mapArray[row][column-1] == '#':
            obstacle = " " + str(row) + ':' + str(column-1) + 'l,'
            if obstacle in obstacles:
                return "Looped", obstacles, guardCoords
            obstacles += obstacle
            mapArray[row][column] = '^'
            return mapArray, obstacles, guardCoords
        mapArray[row][column-1] = '<'
        mapArray[row][column] = 'X'
        guardCoords = (guardCoords[0], guardCoords[1]-1)
        
        return mapArray, obstacles, guardCoords
    
    # Handle Up
    if mapArray[row][column] == '^':
        if row == 0:
            return "Exit", obstacles, guardCoords
        if mapArray[row-1][column] == '#':
            obstacle = " " + str(row-1) + ':' + str(column) + 'l,'
            if obstacle in obstacles:
                return "Looped", obstacles, guardCoords
            obstacles += obstacle
            mapArray[row][column] = '>'
            return mapArray, obstacles, guardCoords
        mapArray[row-1][column] = '^'
        mapArray[row][column] = 'X'
        guardCoords = (guardCoords[0]-1, guardCoords[1])
        return mapArray, obstacles, guardCoords
    
    # Handle down
    if mapArray[row][column] == 'V':
        if row+1 >= len(mapArray):
            return "Exit", obstacles, guardCoords
        if mapArray[row+1][column] == '#':
            obstacle = " " + str(row+1) + ':' + str(column) + 'l,'
            if obstacle in obstacles:
                return "Looped", obstacles, guardCoords
            obstacles += obstacle
            mapArray[row][column] = '<'
            return mapArray, obstacles, guardCoords
        mapArray[row+1][column] = 'V'
        mapArray[row][column] = 'X'
        guardCoords = (guardCoords[0]+1, guardCoords[1])
        return mapArray, obstacles, guardCoords

    # Handle right
    if mapArray[row][column] == '>':
        if column+1 >= len(mapArray[row]):
            return "Exit", obstacles, guardCoords
        if mapArray[row][column+1] == '#':
            obstacle = " " + str(row) + ':' + str(column+1) + 'l,'
            # print(obstacles)
            if obstacle in obstacles:
                return "Looped", obstacles, guardCoords
            obstacles += obstacle
            mapArray[row][column] = 'V'
            return mapArray, obstacles, guardCoords
        mapArray[row][column+1] = '>'
        mapArray[row][column] = 'X'
        guardCoords = (guardCoords[0], guardCoords[1]+1)
        return mapArray, obstacles, guardCoords

def runPart1():

    map = createMap('intput.txt')
    obstacles = ""
    guardCoords = findGuard(map)
    nextMap = map
    # print(map)
    # print(moveGuard(map))

    while nextMap not in  ("Exit", "Looped"):
        map = nextMap
        # print(moveGuard(map,obstacles))
        nextMap, obstacles, guardCoords = moveGuard(map, obstacles, guardCoords)
        # print("------------")
        # print(obstacles)
    if nextMap == "Exit":
        # Start at 1 to account for the guard leaving their edge square
        totalCoverage = 1

        for item in map:        
            print(item)
            for char in item:
                if char == 'X':
                    totalCoverage += 1

        print(totalCoverage)
    if nextMap == "Looped":
        print("Loop created.")


def runPart2():
    map = createMap('input.txt')
    loops = 0
    iteration = 0
    for rowIndex in range(len(map)):
        for columnIndex in range(len(map[rowIndex])):
            iteration += 1
            # For every row, for every item in it, reset the map but
            # set that item as an obstacle. 
            # If we end the bruteforce with a loop, 
            # increment the loop counter. 
            map = createMap('input.txt')
            obstacles = ""
            if map[rowIndex][columnIndex] != '^':
                map[rowIndex][columnIndex] = '#'
                guardCoords = findGuard(map)
                obstacles = ""
                nextMap = map
                # print(map)
                # print(moveGuard(map))

                while nextMap not in  ("Exit", "Looped"):
                    map = nextMap
                    # print(moveGuard(map,obstacles))
                    nextMap, obstacles, guardCoords = moveGuard(map, obstacles, guardCoords)
                    # print("------------")
                    # print(obstacles)
                if nextMap == "Exit":
                    # print("Not a loop...")
                    # Start at 1 to account for the guard leaving their edge square
                    totalCoverage = 1

                    for item in map:        
                        # print(item)
                        for char in item:
                            if char == 'X':
                                totalCoverage += 1

                    # print(totalCoverage)
                if nextMap == "Looped":
                    # print("Loop on iteration " + str(iteration))
                    loops += 1
                    for item in map:
                        print(item)
                    print(obstacles)
                    print(guardCoords)
    print("iterations: " + str(iteration))
    print("Loops: " + str(loops))



# runPart1()
runPart2()
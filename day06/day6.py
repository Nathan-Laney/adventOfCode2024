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

def moveGuard(mapArray, obstacles):
    # print(mapArray)
    for row in range(len(mapArray)):
        for column in range(len(mapArray[row])):
            # print(mapArray[row][column])
            # if this is the guard,
            # check their orientation
            # check the block one in front of that orientation
            # if it's an obstacle, rotate the guard 90degrees. 
            # if it's the end of the map, call it done
            # if it's not, put the guard there. 
            if mapArray[row][column] in ('<', '>', '^', 'V'):
                # print("Guard!")
                # Handle Left
                if mapArray[row][column] == '<':
                    if column == 0:
                        return "Exit", obstacles
                    if mapArray[row][column-1] == '#':
                        obstacle = str(row) + ':' + str(column) + 'l,'
                        if obstacle in obstacles:
                            return "Looped", obstacles
                        obstacles += obstacle
                        mapArray[row][column] = '^'
                        return mapArray, obstacles
                    mapArray[row][column-1] = '<'
                    mapArray[row][column] = 'X'
                    return mapArray, obstacles
                
                # Handle Up
                if mapArray[row][column] == '^':
                    if row == 0:
                        return "Exit", obstacles
                    if mapArray[row-1][column] == '#':
                        obstacle = str(row) + ':' + str(column) + 'u,'
                        if obstacle in obstacles:
                            return "Looped", obstacles
                        obstacles += obstacle
                        mapArray[row][column] = '>'
                        return mapArray, obstacles
                    mapArray[row-1][column] = '^'
                    mapArray[row][column] = 'X'
                    return mapArray, obstacles
                
                # Handle down
                if mapArray[row][column] == 'V':
                    if row+1 >= len(mapArray):
                        return "Exit", obstacles
                    if mapArray[row+1][column] == '#':
                        obstacle = str(row) + ':' + str(column) + 'd,'
                        if obstacle in obstacles:
                            return "Looped", obstacles
                        obstacles += obstacle
                        mapArray[row][column] = '<'
                        return mapArray, obstacles
                    mapArray[row+1][column] = 'V'
                    mapArray[row][column] = 'X'
                    return mapArray, obstacles

                # Handle right
                if mapArray[row][column] == '>':
                    if column+1 >= len(mapArray[row]):
                        return "Exit", obstacles
                    if mapArray[row][column+1] == '#':
                        obstacle = str(row) + ':' + str(column) + 'r,'
                        # print(obstacles)
                        if obstacle in obstacles:
                            return "Looped", obstacles
                        obstacles += obstacle
                        mapArray[row][column] = 'V'
                        return mapArray, obstacles
                    mapArray[row][column+1] = '>'
                    mapArray[row][column] = 'X'
                    return mapArray, obstacles

def runPart1():

    map = createMap('example.txt')
    obstacles = ""
    nextMap = map
    # print(map)
    # print(moveGuard(map))

    while nextMap not in  ("Exit", "Looped"):
        map = nextMap
        # print(moveGuard(map,obstacles))
        nextMap, obstacles = moveGuard(map, obstacles)
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
    map = createMap('day6.txt')
    loops = 0
    for rowIndex in range(len(map)):
        for columnIndex in range(len(map[rowIndex])):

            # For every row, for every item in it, reset the map but
            # set that item as an obstacle. 
            # If we end the bruteforce with a loop, 
            # increment the loop counter. 
            map = createMap('day6.txt')
            if map[rowIndex][columnIndex] != '^':
                map[rowIndex][columnIndex] = '#'

                obstacles = ""
                nextMap = map
                # print(map)
                # print(moveGuard(map))

                while nextMap not in  ("Exit", "Looped"):
                    map = nextMap
                    # print(moveGuard(map,obstacles))
                    nextMap, obstacles = moveGuard(map, obstacles)
                    # print("------------")
                    # print(obstacles)
                if nextMap == "Exit":
                    print("Not a loop...")
                    # Start at 1 to account for the guard leaving their edge square
                    totalCoverage = 1

                    for item in map:        
                        # print(item)
                        for char in item:
                            if char == 'X':
                                totalCoverage += 1

                    # print(totalCoverage)
                if nextMap == "Looped":
                    print("Loop.")
                    loops += 1
    print("Loops: " + str(loops))




runPart2()
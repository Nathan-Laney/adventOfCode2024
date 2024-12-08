import itertools
# map coords of all nodes
# note size of map
# find all possible antinodes
# find the difference X and Y of each node with all others in the list of nodes of that frequency
    # find every permutation of pairs
    # add the coords of the next 2 points 
    # coords will be (minus difference of X1 and X2, minus of Y1 and Y2)
    # then same with plus
# note coords and frequency of every possible antinode 
# filter out those that share coordinates, or have coordinates off the map (at very end)
def partOne():
    coordinateMap = []
    nodeCoordinates = []
    nodeTypes  = set()

    with open('input.txt', 'r') as file:
        for line in file:
            coordinateMap.append(list(line.strip()))

    mapLength = len(coordinateMap)
    mapWidth = len(coordinateMap[0])


    # Get a list of all non-blank spots, and what is there
    for row in range(len(coordinateMap)):
        for coordinate in range(len(coordinateMap[row])):
            if coordinateMap[row][coordinate] != '.': # ignore blank spots
                nodeTypes.add(coordinateMap[row][coordinate])
                nodeCoordinates.append((row, coordinate, coordinateMap[row][coordinate]))

    # Find a list of all possible antinodes. 
    possibleAntinodes = []
    # For every type of node that we found,
    for nodeType in nodeTypes:
        # Find the number of nodes of that type
        x = [t for t in nodeCoordinates if t[2] == nodeType]
        possibleNodes = list(itertools.combinations(x, r=2))

        for possibleNode in possibleNodes:

            possibleAntinodes.append(
                # X1 value minus difference of X2 and X1
                (possibleNode[0][0] - (possibleNode[1][0] - possibleNode[0][0]), 
                # Y1 value minus difference of Y2 and Y1
                possibleNode[0][1] - ( possibleNode[1][1] - possibleNode[0][1] ), 
                nodeType))
            
            possibleAntinodes.append(
                # X2 value plus difference of X2 and X1
                (possibleNode[1][0] + (possibleNode[1][0] - possibleNode[0][0]), 
                # Y2 value plus difference of Y2 and Y1
                possibleNode[1][1] + ( possibleNode[1][1] - possibleNode[0][1] ), 
                nodeType))

    # Put coords in a set to ignore duplicates
    antinodes = set()
    for possibleAntinode in possibleAntinodes:
        if (possibleAntinode[0] >= 0 and possibleAntinode[0] < mapWidth) and (possibleAntinode[1] >= 0 and possibleAntinode[1] < mapLength):
            antinodes.add((possibleAntinode[0], possibleAntinode[1]))

    print(len(antinodes))

# Part 2
def partTwo():
    coordinateMap = []
    nodeCoordinates = []
    nodeTypes  = set()

    with open('input.txt', 'r') as file:
        for line in file:
            coordinateMap.append(list(line.strip()))

    mapLength = len(coordinateMap)
    mapWidth = len(coordinateMap[0])


    # Get a list of all non-blank spots, and what is there
    for row in range(len(coordinateMap)):
        # print(row)
        for coordinate in range(len(coordinateMap[row])):
            if coordinateMap[row][coordinate] != '.': # ignore blank spots
                nodeTypes.add(coordinateMap[row][coordinate])
                nodeCoordinates.append((row, coordinate, coordinateMap[row][coordinate]))
            # print(coordinate)

    # Find a list of all possible antinodes. 

    possibleAntinodes = []
    # For every type of node that we found,
    for nodeType in nodeTypes:
        # print("Nodetype: " + nodeType)
        # Find the number of nodes of that type
        x = [t for t in nodeCoordinates if t[2] == nodeType]
        possibleNodes = list(itertools.combinations(x, r=2))
        # print(possibleNodes)

        for possibleNode in possibleNodes:
            # append the nodes themselves - they'll always be within puzzle bounds.
            possibleAntinodes.append((possibleNode[0][0], possibleNode[0][1], nodeType))
            possibleAntinodes.append((possibleNode[1][0], possibleNode[1][1], nodeType))

            # keep finding antinodes until we leave the puzzle bounds
            x2x1diff = possibleNode[1][0] - possibleNode[0][0]
            y2y1diff = possibleNode[1][1] - possibleNode[0][1]

            # Going backwards... 
            currentX1 = possibleNode[0][0]
            currentY1 = possibleNode[0][1]
            tempAntinode1 = (currentX1, currentY1, nodeType)
            while (tempAntinode1[0] >= 0 and tempAntinode1[0] < mapWidth) and (tempAntinode1[1] >= 0 and tempAntinode1[1] < mapLength) :
                possibleAntinodes.append((tempAntinode1[0], tempAntinode1[1], nodeType))
                tempAntinode1 = ((currentX1 - x2x1diff), (currentY1 - y2y1diff), nodeType)
                currentX1 = tempAntinode1[0]
                currentY1 = tempAntinode1[1]
            
            # Going forwards... 
            currentX2 = possibleNode[1][0]
            currentY2 = possibleNode[1][1]
            tempAntinode2 = (currentX2, currentY2, nodeType)
            while (tempAntinode2[0] >= 0 and tempAntinode2[0] < mapWidth) and (tempAntinode2[1] >= 0 and tempAntinode2[1] < mapLength) :
                possibleAntinodes.append((tempAntinode2[0], tempAntinode2[1], nodeType))
                tempAntinode2 = ((currentX1 + x2x1diff), (currentY1 + y2y1diff), nodeType)
                currentX1 = tempAntinode2[0]
                currentY1 = tempAntinode2[1]

    # Put the coordinates in a set to remove duplicates (ignores the type now)
    antinodes = set()
    for possibleAntinode in possibleAntinodes:
        if (possibleAntinode[0] >= 0 and possibleAntinode[0] < mapWidth) and (possibleAntinode[1] >= 0 and possibleAntinode[1] < mapLength):
            antinodes.add((possibleAntinode[0], possibleAntinode[1]))

    print(len(antinodes))

partTwo()
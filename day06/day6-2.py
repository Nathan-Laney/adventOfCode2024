
class Guard():
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.facing = 'N'
        self.obstacles = []
        self.knownObstacles = []

    def createObstacle(self, obxpos, obypos):
        self.obstacles.append((obxpos, obypos))

    # Appends an obstacle to the guard's known obstacles. 
    def createKnownObstacle(self, obxpos, obypos, obface):
        # Mark the face we've seen, and the X and Y positions of the obstacle.
        self.knownObstacles.append((obxpos, obypos, obface))
    
    # Return True if the guard has seen this obstacle before. 
    # Else return false. 
    def checkKnownObstacle(self, obxpos, obypos, obface):
        if tuple(obxpos, obypos, obface) in self.knownObstacles:
            return True
        return False
    
    # Updates the guard's coordinates based on their facing. 
    # Returns the new coordinates. 
    def updateGuardCoordinates(self):
        if self.facing == 'N':
            self.xpos = self.xpos - 1
        elif self.facing == 'S':
            self.xpos = self.xpos + 1
        elif self.facing == 'W':
            self.ypos = self.ypos - 1
        elif self.facing == 'E':
            self.ypos = self.ypos + 1
        return (self.ypos, self.ypos)
    
    # Updates the guard's facing to the next cardinal. 
    # Returns new facing. 
    def rotateGuard(self):
        if self.facing == 'N':
            self.facing = 'E'
        elif self.facing == 'S':
            self.facing = 'W'
        elif self.facing == 'W':
            self.facing = 'N'
        elif self.facing == 'E':
            self.facing = 'S'
        return self.facing

    # Returns coordinates of where the guard's next move would take them
    # should they move forward.
    def whereWouldGuardMove(self):
        if self.facing == 'N':
            return (self.xpos - 1, self.ypos )
        elif self.facing == 'S':
            return (self.xpos + 1, self.ypos )
        elif self.facing == 'W':
            return (self.xpos, self.ypos - 1)
        elif self.facing == 'E':
            return (self.xpos, self.ypos + 1)

    def moveGuard(self):
        nextCoordinates = self.whereWouldGuardMove()
        # If this is a known obstacle, we're looped.
        if (nextCoordinates[0], nextCoordinates[1], self.facing) in self.knownObstacles:
            return "Loop detected."
        # If this is an unknown obstacle, mark it known.
        if nextCoordinates in self.obstacles:
            self.createKnownObstacle(nextCoordinates[0], nextCoordinates[1], self.facing)
            self.rotateGuard()
        # If there's no obstacle, move.
        else:
            self.updateGuardCoordinates()
        return (self.xpos, self.ypos)


def simulateMap(simulationMap):
    # print(simulationMap)
    for x in range(len(simulationMap)):
        for y in range(len(simulationMap[x])):
            if simulationMap[x][y] == '^':
                # Create guard.
                guard = Guard(x, y)
    
    for x in range(len(simulationMap)):
        for y in range(len(simulationMap[x])):
            if simulationMap[x][y] == '#':
                # Create obstacles.
                guard.createObstacle(x, y)
    

    # Run until the guard is off the simulationMap or a loop is detected. Mark which one happens. 
    loops = 0
    solves = 0
    while True: 
        # print("+1")
        # print ("Coords: (" + str(guard.xpos) + ', ' + str(guard.ypos) + ") Facing " + guard.facing)
        result = guard.moveGuard()
        if (result == 'Loop detected.'):
            # print('loop')
            loops += 1
            break
        elif (guard.xpos not in range(len(simulationMap)) or guard.ypos not in range(len(simulationMap[0]))):
            # print(range(len(simulationMap)))
            # print(guard.xpos)
            solves += 1
            break
    return(loops, solves)


def runPart2():
    map = []
    loops = 0
    solves = 0
    increment = 0
    filename = ('input.txt')
    with open(filename, 'r') as file:
        for line in file:
            map.append(list(line.strip()))

    for x in range(len(map)):
        for y in range(len(map[0])):
            if map[x][y] != '^':
                increment += 1
                if increment % 100 == 0:
                    print("Increment " + str(increment))
                map = []
                with open(filename, 'r') as file:
                    for line in file:
                        map.append(list(line.strip()))
                map[x][y] = '#'
                loopCounter, solveCounter = simulateMap(map)
                loops += loopCounter
                solves += solveCounter
    print("Loops: " + str(loops))
    print("Solves: " + str(solves))
    
runPart2()


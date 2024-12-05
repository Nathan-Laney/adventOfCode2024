# create 2d array containing contents of puzzle
# & insert a line of ' ' chars at the right side
# and the bottom to break up any matches that roll
# off the side of the puzzle and wrap around to find
# a match on the other side
# (... it took an embarrassingly long time to
#      diagnose this was happening)
puzzle = []
with open('day4.txt', 'r') as file:
    for line in file:
        puzzle.append(list(line.strip() + " "))
    # print(len(puzzle[-1]))
    puzzle.append(list(len(puzzle[-1]) * " "))
# print(puzzle)

# loop through each character of the array. 
# if it's an X, check all surrounding directions for 'MAS'. 
# if they match, increment count by 1. 
matches = 0
for line in range(len(puzzle)):
    for char in range(len(puzzle[line])):
        if puzzle[line][char].upper() == 'X':
            # print("Potential XMAS")
            # for all cardinal and ordinal: N, S, E, W, NE, NW, SE, SW
            # checking if index is out of range of list
            # ignore index errors and pass
            directions = {
                "n" : '', 
                "s" : '',
                "e" : '',
                "w" : '',
                "ne" : '',
                "nw" : '',
                "se" : '',
                "sw" : ''
            }
            for x in range(1, 4):
                # time for nasty. avert ye eyes. could have been avoided by not being so lazy
                try:
                    directions["n"] += puzzle[line-x][char]
                except IndexError:
                    pass
                try:
                    directions["s"] += puzzle[line+x][char]
                except IndexError:
                    pass
                try:
                    directions["e"] += puzzle[line][char+x]
                except IndexError:
                    pass
                try:
                    directions["w"] += puzzle[line][char-x]
                except IndexError:
                    pass
                try:
                    directions["nw"] += puzzle[line-x][char-x]
                except IndexError:
                    pass
                try:
                    directions["ne"] += puzzle[line-x][char+x]
                except IndexError:
                    pass
                try:                    
                    directions["sw"] += puzzle[line+x][char-x]
                except IndexError:
                    pass
                try:
                    directions["se"] += puzzle[line+x][char+x]
                except IndexError:
                    pass
            # print(directions)
            for direction in directions:
                if directions[direction] == "MAS":
                    matches = matches + 1
                    # print(str(matches) + " found in " + direction + " starting from origin point of " + str(line) + " " + str(char))
print(matches)

# part 2
matches = 0
for line in range(len(puzzle)):
    for char in range(len(puzzle[line])):
        if puzzle[line][char].upper() == 'A':
            # print("Potential XMAS")
            # check each diagonal
            # ignore index errors and pass
            directions = {
                "nw" : '',
                "se" : '',
            }
            for x in range(-1, 2):
                try:
                    directions["se"] += puzzle[line+x][char+x]
                except IndexError:
                    pass
                try:
                    directions["nw"] += puzzle[line-x][char+x]
                except IndexError:
                    pass
            if ((directions["se"] == "MAS") or (directions["se"] == "SAM")) and ((directions["nw"] == "MAS") or (directions["nw"] == "SAM")):
                matches = matches + 1

print(matches)
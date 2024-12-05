# store our rules as an array of tuples
rules = []

# define a rule (add it to a data structure)
def defineRule(input):
    rules.append(tuple(input.strip().split('|')))

# check if string complies with rules
def checkCompliance(input):
    compliant = True
    orderedList = input
    for rule in rules:
        if (rule[0] in input) and (rule[1] in input):
            # if noncompliant,
            if orderedList.index(str(rule[0])) > orderedList.index(str(rule[1])):
                # swap indeces of the noncompliant numbers and check again. 
                compliant = False
    return compliant

def fixCompliance(orderedList):
    # If it's compliant, return the number.
    # If it's not compliant, swap the places of the two noncompliant numbers
    # and check again. 

    # if compliant, break the loop
    if checkCompliance(orderedList):
        return(orderedList)
    
    # otherwise fix it
    for rule in rules:
        # If the relevant numbers are present:
        if (rule[0] in orderedList) and (rule[1] in orderedList):
            
            # If number 1 appears after number 2:
            if orderedList.index(str(rule[0])) > orderedList.index(str(rule[1])):
                # ton of print statements from bugfixing 
                # print("Hit")
                # print(orderedList[orderedList.index(str(rule[0]))])
                # print(orderedList[orderedList.index(str(rule[1]))])
                indexOfRule0 = orderedList.index(str(rule[0]))
                indexOfRule1 = orderedList.index(str(rule[1]))
                # print(str(indexOfRule0) + ":" + str(indexOfRule1))
                orderedList[indexOfRule0], orderedList[indexOfRule1] = orderedList[indexOfRule1], orderedList[indexOfRule0]
                # print("Broke rule " + str(rule))
                return fixCompliance(orderedList)

def runDay1():
    # take in file and do the thing
    middleValue = 0
    with open('day5.txt', 'r') as file:
        for line in file:
            if "|" in line:
                defineRule(line)
            elif not line.strip():
                pass
            else:
                orderedList = line.strip().split(',')
                if(checkCompliance(line)) == True:
                    # The following pulls the middle index, and pulls 
                    # the value at that index, and converts to int.
                    tempList = (line.strip().split(','))
                    middleValue += int(tempList[len(tempList)//2])
    print(middleValue)

def runDay2():
    # take in file and do the thing
    middleValue = 0
    nonCompliantMiddleValue = 0
    with open('day5.txt', 'r') as file:
        for line in file:
            if "|" in line:
                defineRule(line)
            elif not line.strip():
                pass
            else:
                orderedList = line.strip().split(',')
                if(checkCompliance(orderedList)) == True:
                    # The following pulls the middle index, and pulls 
                    # the value at that index, and converts to int.
                    tempList = (line.strip().split(','))
                    middleValue += int(tempList[len(tempList)//2])
                else:
                    # print("Attempting to fix " + str(orderedList))
                    fixedList = (fixCompliance(orderedList))
                    # print("Fixed list: " + str(fixedList))
                    nonCompliantMiddleValue += int(fixedList[len(fixedList)//2])
                    # print("Adding " + str(int(fixedList[len(fixedList)//2])))
    print(nonCompliantMiddleValue)

runDay1()
runDay2()

# store our rules as an array of tuples
rules = []

# define a rule (add it to a data structure)
def defineRule(input):
    rules.append(tuple(input.strip().split('|')))
# check if string complies with rules
def checkCompliance(input):
    compliant = True
    orderedList = input.strip().split(',')
    for rule in rules:
        if (rule[0] in input) and (rule[1] in input):
            if orderedList.index(str(rule[0])) > orderedList.index(str(rule[1])):
                compliant = False
    return compliant

# take in file and do the thing
middleValue = 0
with open('day5.txt', 'r') as file:
    for line in file:
        if "|" in line:
            defineRule(line)
        elif not line.strip():
            pass
        else:
            if(checkCompliance(line)) == True:
                # The following pulls the middle index, and pulls 
                # the value at that index, and converts to int.
                tempList = (line.strip().split(','))
                middleValue += int(tempList[len(tempList)//2])
print(middleValue)
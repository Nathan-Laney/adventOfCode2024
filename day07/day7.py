import itertools

def slicezip(a, b):
    result = [0]*(len(a)+len(b))
    result[::2] = a
    result[1::2] = b
    return result

def eval_left_to_right(expression):
  pieces = []

  i = 0
  for c in expression:
    if c.isdigit():
      try:
        pieces[i] += c
      except IndexError:
        pieces.append(c)
    elif c in {'+', '*', '↔'}:
      i += 1
      pieces.append(c)
  
  last_piece = pieces.pop(0)
  result = 0
  for piece in pieces:
    # print(piece)
    if '↔' in piece:
       result = int(str(last_piece) + str(piece[1:]))
    else:
        result = eval(f'{last_piece}{piece}')
    last_piece = str(result)
  return result

# ... what's the best data structure for this? 
# Doing a tuple, with (int(goal), int(currentTotal), [ints to math])? idk

chain = []

with open('input.txt', 'r') as file:
    for line in file:
        temp = line.strip().split(': ')
        # The following line converts the file line into
        # a tuple, with (int(goal), int(currentTotal), [int(numberToUse), ...])
        # and appends to the chain
        chain.append((int(temp[0]), list(map(int, temp[1].split(' ')))))

def partOne():
    x = ['+','*']
    sumOfTrue = 0
    for item in range(len(chain)):
        numArray = chain[item][1]
        chainLength = len(numArray)
        isPossible = False
        mostRecentTrueTotal = 0
        for permutation in itertools.product(x, repeat=chainLength-1):
            # print(permutation)
            permArray = list(itertools.chain.from_iterable(permutation))
            permArray.append("")
            
            
            # print(permArray)
            # print(numArray)
            # print(slicezip(numArray, permArray))
            stringEval = ''.join(str(x) for x in slicezip(numArray, permArray))
            total = (eval_left_to_right(stringEval))
            # print("Total: " + str(total) + " and evaluation: " + stringEval)
            if total == chain[item][0]:
                # print("Seen as equal.")
                isPossible = True
                mostRecentTrueTotal = total
                break
        
        if isPossible:
            sumOfTrue += mostRecentTrueTotal
            isPossible = False
        

    print(sumOfTrue)

def partTwo():
    x = ['+','*', '↔']
    sumOfTrue = 0
    for item in range(len(chain)):
        print("Analyzing " + str(item))
        numArray = chain[item][1]
        chainLength = len(numArray)
        isPossible = False
        mostRecentTrueTotal = 0
        for permutation in itertools.product(x, repeat=chainLength-1):
            # print(permutation)
            permArray = list(itertools.chain.from_iterable(permutation))
            permArray.append("")
            
            
            # print(permArray)
            # print(numArray)
            # print(slicezip(numArray, permArray))
            stringEval = ''.join(str(x) for x in slicezip(numArray, permArray))
            total = 0
            try:
               total = int(stringEval)
            except:
                total = (eval_left_to_right(stringEval))
            # print("Goal: " + str(chain[item][0]) + " result: " + str(total) + " and evaluation: " + stringEval)
            if total == chain[item][0]:
                # print("Seen as equal.")
                isPossible = True
                mostRecentTrueTotal = total
                break
        
        if isPossible:
            sumOfTrue += mostRecentTrueTotal
            isPossible = False
        

    print(sumOfTrue)


# partOne()
partTwo()
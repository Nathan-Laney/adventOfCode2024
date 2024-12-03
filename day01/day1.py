list1 = []
list2 = []

with open('example1.txt', 'r') as file:
    for line in file:
        split = line.strip().split('   ')
        list1.append(split[0])
        list2.append(split[1])


list1_sorted = sorted(list1, key=int)
list2_sorted = sorted(list2, key=int)
total_difference = 0
for i in range(len(list1_sorted)):
    total_difference += abs(int(list1_sorted[i]) - int(list2_sorted[i]))

print(total_difference)


# Part 2

similarityScore = 0
for i in range(len(list1_sorted)):
    for j in range(len(list2_sorted)):
        timesSeen = 0
        if int(list1_sorted[i]) == int(list2_sorted[j]):
            timesSeen = timesSeen + 1
        similarityScore += timesSeen * int(list1_sorted[i])

print(similarityScore)

import re
pattern = "mul\\((\\d+),(\\d+)\\)"
sum = 0
with open('input.txt', 'r') as file:
    match = re.findall(pattern, file.read())
    if match:
        for mulOp in match:
            # print(mulOp)
            sum += int(mulOp[0]) * int(mulOp[1])
print(sum)

# part 2
pattern = "don't\\(\\).*?do\\(\\)" #everything between don't and do
sum = 0
with open('input.txt', 'r') as file:
    text = "do()" + file.read() + "don't()"
    match = re.findall(pattern, text)
    if match:
        for mulOp in match:
            # print(mulOp)
            text = text.replace(mulOp, "") # delete everything between 'don't' and 'do' 
    # print(text)

    # then just part 1 again
    pattern = "mul\\((\\d+),(\\d+)\\)"
    match = re.findall(pattern, text)
    if match:
        for mulOp in match:
            # print(mulOp)
            sum += int(mulOp[0]) * int(mulOp[1])

print(sum)

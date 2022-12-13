lines = []

with open('input.txt', 'r') as file:
    lines = file.readlines()

numbers = []
current_numbers = []
for i in range(len(lines)):
    if lines[i] == '\n':
        numbers.append(current_numbers)
        current_numbers = []
        continue
    current_numbers.append(int(lines[i]))

numbers.append(current_numbers)

sums = []
for block in numbers:
    sums.append(sum(block))

print(max(sums))
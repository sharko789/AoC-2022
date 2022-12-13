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

count_three = 0
print(max(sums))
count_three += max(sums)
sums.remove(max(sums))
print(max(sums))
count_three += max(sums)
sums.remove(max(sums))
print(max(sums))
count_three += max(sums)

print(count_three)
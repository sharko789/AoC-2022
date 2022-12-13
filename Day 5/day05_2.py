lines = []

with open('input.txt', 'r') as file:
    lines = file.readlines()

for i in range(len(lines)):
    lines[i] = lines[i][:-1]

stacks_input = []
for line in lines:
    if line == '':
        stacks_input.pop()
        break

    stacks_input.append(line.split(' '))

stacks_input.reverse()

# print(stacks_input)

stacks = []
for stack_count in range(len(stacks_input[0])):
    stacks.append([])

for row in stacks_input:
    i = 0
    index = 0
    while i < len(row):
        crate = row[i].strip('[]')
        if crate == '':
            i += 4
        else:
            stacks[index].append(crate)
            i += 1
        index += 1


line = ' '
while line != '':
    line = lines.pop(0)


for i in range(len(lines)):
    lines[i] = lines[i].replace('move ', '')
    lines[i] = lines[i].replace('from ', '')
    lines[i] = lines[i].replace('to ', '')
    lines[i] = lines[i].split()
    
# print(lines)
print(stacks)

for line in lines:
    amount = int(line[0])
    from_id = int(line[1]) - 1
    to_id = int(line[2]) - 1

    on_crane = []
    for i in range(amount):
        on_crane.append(stacks[from_id].pop())

    on_crane.reverse()
    for crate in on_crane:
        stacks[to_id].append(crate)


print(stacks)

for stack in stacks:
    print(stack.pop())
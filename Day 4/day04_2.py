lines = []

with open('input.txt', 'r') as file:
    lines = file.readlines()

for i in range(len(lines)):
    lines[i] = lines[i][:-1]


pairs = []
for pair in lines:
    intervalls = pair.split(',')
    bounds = []
    for intervall in intervalls:
        bounds.append((intervall.split('-')))
    pairs.append(bounds)

sum = 0
for pair in pairs:    
    if int(pair[0][1]) < int(pair[1][0]):
        continue
    elif int(pair[0][0]) > int(pair[1][1]):
        continue
    else:
        sum += 1


print(sum)
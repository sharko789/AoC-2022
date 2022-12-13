line = ''

with open('input.txt', 'r') as file:
    line = file.readline()

line.strip()

threshold = []
for i in range(len(line)):
    character = line[i]
    threshold.append(character)

    if len(threshold) == 5:
        threshold.pop(0)
        if len(set(threshold)) == 4:
            print(threshold)
            print(i + 1)
            break
lines = []

with open('input.txt', 'r') as file:
    lines = file.readlines()

for i in range(len(lines)):
    lines[i] = lines[i][:-1]


common_items = []
for line in lines:
    half1 = line[0:len(line)//2]
    half2 = line[len(line)//2:]

    # print(half1)
    # print(half2)

    for letter in set(half1) & set(half2):
        common_items.append(letter)

priorities = []
for item in common_items:
    ascii_item = ord(item)
    # print(ascii_item)
    if ascii_item >= 97: #is a or bigger
        priorities.append(ascii_item - 96)
    else:
        priorities.append(ascii_item - 38)

# print(common_items)
# print(priorities)
print(sum(priorities))
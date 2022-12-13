lines = ['hello\n', 'hi\n', 'hunt\n', 'bananna\n', 'bee\n', 'bomb\n']

with open('input.txt', 'r') as file:
    lines = file.readlines()

for i in range(len(lines)):
    lines[i] = lines[i][:-1]


common_items = []
for i in range(len(lines) // 3):
    first_elf = lines[i*3]
    second_elf = lines[i*3 + 1]
    third_elf = lines[i*3 + 2]

    for letter in set(first_elf) & set(second_elf) & set(third_elf):
        common_items.append(letter)

priorities = []
for item in common_items:
    ascii_item = ord(item)
    if ascii_item >= 97: #is a or bigger
        priorities.append(ascii_item - 96)
    else:
        priorities.append(ascii_item - 38)

# print(common_items)
# print(priorities)
print(sum(priorities))
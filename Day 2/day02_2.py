lines = []
possible_games = {
    'A X': 3, 'A Y': 4, 'A Z': 8,
    'B X': 1, 'B Y': 5, 'B Z': 9,
    'C X': 2, 'C Y': 6, 'C Z': 7
}

with open('input.txt', 'r') as file:
    lines = file.readlines()

# cuts away \n
for i in range(len(lines)):
    lines[i] = lines[i][:-1]

values = []
for line in lines:
    values.append(possible_games[line])

print(sum(values))
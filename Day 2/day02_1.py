lines = []
possible_games = {
    'A X': 4, 'A Y': 8, 'A Z': 3,
    'B X': 1, 'B Y': 5, 'B Z': 9,
    'C X': 7, 'C Y': 2, 'C Z': 6
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
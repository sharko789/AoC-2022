lines = []

with open('demo.txt', 'r') as file:
    for line in file.readlines():
        lines.append(line.strip())


tree_grid = []

for line in lines:
    row = []
    for character in line:
        row.append(int(character))
    tree_grid.append(row)
    



height, width = len(tree_grid), len(tree_grid[0])
visible_trees = []
tree_scenic_score = tree_grid

for x in range(width):
    for y in range(height):
        if x + 1 == width or x - 1 < 0 or x + 1 == height or x - 1 < 0:
            tree_scenic_score[y][x] = 0
        else:
            top_max = tree_grid[y - 1][x]
            top_trees = 0
            bottom_max = tree_grid[y + 1][x]
            bottom_trees = 0

            
            right_max = tree_grid[y][x + 1]
            right_trees = 0
            left_max = tree_grid[y][x - 1]
            left_trees = 0




for x in range(width):
    visible_trees.append((x, 0))
    top_max = tree_grid[0][x]

    visible_trees.append((x, height - 1))
    bottom_max = tree_grid[height - 1][x]

    for y in range(height):
        if tree_grid[y][x] > top_max:
            visible_trees.append((x, y))
            top_max = tree_grid[y][x]

        if tree_grid[height-1 - y][x] > bottom_max:
            visible_trees.append((x, height-1 - y))
            bottom_max = tree_grid[height-1 - y][x]

for y in range(height):
    visible_trees.append((0, y))
    left_max = tree_grid[y][0]

    visible_trees.append((width - 1, y))
    right_max = tree_grid[y][width - 1]

    for x in range(width):
        if tree_grid[y][x] > left_max:
            visible_trees.append((x, y))
            left_max = tree_grid[y][x]

        if tree_grid[y][width-1 - x] > right_max:
            visible_trees.append((width-1 - x, y))
            right_max = tree_grid[y][width-1 - x]

for row in tree_grid: print(row)
# print(visible_trees)
# print('\n')
# print(set(visible_trees))
print(len(set(visible_trees)))

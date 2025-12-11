grid = []

filename = "input.txt"
with open(filename, 'r') as file:
    for line in file:
        line = line.strip()
        grid.append(line)
        
grid = [list(row) for row in grid]

# for row in grid:
#     print(' '.join(row))
# print("")

count = 0
for row in range(len(grid)-1):
    for col in range(len(grid[row])):
        c = grid[row][col]
        if c == '|' or c == 'S':
            if grid[row+1][col] == '^':
                count += 1
                grid[row+1][col+1] = '|'
                grid[row+1][col-1] = '|'
            else:
                grid[row+1][col] = '|'
                
# for row in grid:
#     print(' '.join(row))
print(count)
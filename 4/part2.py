filename = "input.txt"

grid = [[]]

with open(filename, 'r') as file:
    for line in file:
        grid.append(list(line.strip()))



def checkgrid(grid, x, y):
    if x >= 0 and x < len(grid) and y >= 0 and y < len(grid[x]):
        return grid[x][y]
    return '.'

prev_sum = -1
sum = 0

while(sum > prev_sum):
    prev_sum = sum
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            count = 0
            if grid[i][j] == '.':
                continue
            
            if checkgrid(grid, i+1, j) != '.':
                count += 1
            
            if checkgrid(grid, i, j+1) != '.':
                count += 1
                
            if checkgrid(grid, i-1, j) != '.':
                count += 1
            
            if checkgrid(grid, i, j-1) != '.':
                count += 1
                
            if checkgrid(grid, i+1, j+1) != '.':
                count += 1
            
            if checkgrid(grid, i-1, j-1) != '.':
                count += 1
                
            if checkgrid(grid, i+1, j-1) != '.':
                count += 1
            
            if checkgrid(grid, i-1, j+1) != '.':
                count += 1
            
            
            if count < 4:
                sum += 1
                grid[i][j] = '.'
            
for line in grid:
    print(''.join(line))
print(sum)
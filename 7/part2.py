grid = []

filename = "test.txt"
with open(filename, 'r') as file:
    for line in file:
        line = line.strip()
        grid.append(line)
        
grid = [list(row) for row in grid]

# for row in grid:
#     print(' '.join(row))
# print("")


def getstart():
    for row in range(len(grid)-1):
        for col in range(len(grid[row])):
            if grid[row][col] == 's':
                return (row,col)
root = getstart()

def calc_pahts(cur, grid):
    # make the tree recusively
    y = cur[0]
    x = cur[1]
    
    try:
        grid[x][y]
    except:
        return 1 # out of bounds
    
    if grid[x][y-1] == '.' or grid[x][y-1] == '|':
        grid[x][y-1] = '|'
        return calc_pahts((x,y-1), grid)
    else: # == '^'
        grid[x+1][y-1] = '|'
        grid[x-1][y-1] = '|'
        
        return calc_pahts((x+1,y-1), grid) + calc_pahts((x-1,y-1), grid)


sum = calc_pahts(root, grid)
print(sum)
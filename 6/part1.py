grid = []

filename = "input.txt"
with open(filename, 'r') as file:
    for line in file:
        nums = line.strip().split(" ")
        
        if nums[0] == "*" or nums[0] == '+':
            nums = [n for n in nums if n != '']
            grid.append(nums)
        else:
            nums = [int(n) for n in nums if n != '']
            grid.append(nums)

#print(grid)

sum = 0


for col in range(len(grid[0])):
    symbol = grid[len(grid)-1][col]
    cur_sum = grid[0][col]
    
    for row in range(1, len(grid)-1):
        if symbol == '*':
            cur_sum *= grid[row][col]
        elif symbol == '+':
            cur_sum += grid[row][col]
    sum += cur_sum
        
print(sum)
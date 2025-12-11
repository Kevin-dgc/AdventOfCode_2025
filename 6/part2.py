grid = []
symbol_list = []
lens_list = []

filename = "input.txt"
with open(filename, 'r') as file:
    lines = file.readlines()
    last = lines[-1]
    
    count = 0
    symbol_list.append(last[0])

    for c in last:
        if c != ' ' and count != 0:
            symbol_list.append(c)
            lens_list.append(count-1)
            count = 1
        else:
            count += 1
    lens_list.append(count)
    
    for not_used, line in enumerate(lines[:-1]):
        line = line.rstrip('\n')
        row = []
        
        #print(line)
        
        num = ""
        row_index = 0
        row = []
        str_len = lens_list[row_index]
        for c in line:
            if str_len == 0:
                row_index += 1
                str_len = lens_list[row_index]
                row.append(num)
                num = ""
                continue

            num += c
            str_len -= 1
        row.append(num)
        grid.append(row)
        
#print(grid)
#print(lens_list)
#print(symbol_list)

sum = 0
col_index = 0

for col in range(len(grid[0])):
    symbol = symbol_list[col_index]
    col_index += 1

    new_nums = []
    
    for i in range(len(grid[0][col])): # len of each string
        num = 0
        for row in range(len(grid)):
            str_num = grid[row][col]
            
            if str_num[i] == ' ':
                continue
            else:
                num *= 10
                num += int(str_num[i])
        new_nums.append(num)

    # calc new_nums
    #print(new_nums, symbol)
    cur_sum = new_nums[0]
    for n in range(1, len(new_nums)):
        if symbol == '*':
            cur_sum *= new_nums[n]
        elif symbol == '+':
            cur_sum += new_nums[n]
    #print(cur_sum)
    sum += cur_sum

print(sum)
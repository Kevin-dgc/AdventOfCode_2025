range_list = []

filename = "input.txt"

with open(filename, 'r') as file:
    for line in file:
        if not line.strip():
            break
        
        pairs = line.strip().split("-")
        range_list.append([int(pairs[0]), int(pairs[1])])
      
range_list.sort(key=lambda pair: pair[0])
#print(range_list)
for i, pair in enumerate(range_list):
    if pair[0] == pair[1] == -1:
        continue
    
    for index in range(i+1, len(range_list)):
        after = range_list[index]
        if after[0] == after[1] == -1:
            continue
        
        if pair[1] >= after[0]:
            pair[1] = max(pair[1], after[1])
            after[0] = -1 # zero out after
            after[1] = -1      
range_list = [pair for pair in range_list if pair[0] != -1]

        
#print(range_list)
count = 0

for pair in range_list:
    count += pair[1] - pair[0] + 1
    # each range + one for couting
    
print(count)
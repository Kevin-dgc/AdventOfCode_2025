range_list = []
ingredient_id = []

filename = "input.txt"
second_half = False

with open(filename, 'r') as file:
    for line in file:
        if not line.strip():
            second_half = True
            continue
            
        if second_half: # second half
            ingredient_id.append(int(line.strip()))
        else: # first half
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

for id in ingredient_id:
    left = 0
    right = len(range_list) -1
    
    while left <= right: # bin search the ranges with id
        mid = (left+right) //2
        pair = range_list[mid]
        
        if id >= pair[0] and id <= pair[1]:
            count += 1
            break
        elif id < pair[0]:
            right = mid - 1
        else:
            left = mid + 1
            
print(count)
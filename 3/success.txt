filename = 'input.txt'
banks = list()

with open(filename, 'r') as file:
    for line in file:
        banks.append(line.strip())
    
sum = 0    

for bank in banks:
    stack = []
    removes_left = len(bank) - 12
    
    for n in bank:
        while stack and removes_left > 0 and stack[-1] < n:
            stack.pop()
            removes_left -= 1
        stack.append(n)
        
    while removes_left > 0:
        stack.pop()
        removes_left -= 1
        
    sum += int(''.join(stack))
    
print(sum)
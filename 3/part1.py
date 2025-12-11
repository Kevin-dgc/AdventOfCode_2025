filename = 'input.txt'
banks = list()

with open(filename, 'r') as file:
    for line in file:
        banks.append(line.strip())
    
sum = 0    
for bank in banks:
    volt = [None, None]
    for i, c in enumerate(bank):
        if volt[0] is None or (c > volt[0] and i+1 < len(bank)):
            volt[0] = c
            volt[1] = None
            
        elif volt[1] is None or c > volt[1]:
            volt[1] = c
                   
    sum += int(volt[0]+volt[1])
    #print(int(volt[0]+volt[1]))
    
print(sum)
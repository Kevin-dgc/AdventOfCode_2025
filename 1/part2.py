filename = "input.txt"
input = list()

with open(filename, 'r') as file:
    for line in file:
        input.append(line.strip())

sum = 0
dial = 50

for turn in input:
    n = int(turn[1:])
    c = turn[0]
    
    if c == 'L':
        n *= -1
        if dial == 0:
            sum -= 1
    
    dial += n
    sum += abs(dial//100)

    if dial < 0 and dial%100 == 0:
        sum += 1
        
    if dial == 0:
        sum += 1
    
    dial %= 100

print(sum)

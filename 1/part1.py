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
    
    if c == 'R': # +
        dial += n
        dial %= 100
        #print(f'1 {dial}')

    else: # -
        #print(f'2 {dial}')
        dial -= n
        #print(f'3 {dial}')

        if dial < 0:
            dial %= 100
        #print(f'4 {dial}')

    if dial == 0:
        sum += 1
    #print(f'5 {dial}')
    #print("===========")

print(sum)

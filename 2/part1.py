filename = 'input.txt'
ids = list(tuple())

with open (filename, 'r') as file:
    content = file.read()
    
    pairs = content.split(',')
    
    ids = [tuple(pair.split('-')) for pair in pairs]
            
#print(ids)
   
sum = 0
   
for pair in ids:
    start = int(pair[0])
    end = int(pair[1])
    
    for n in range(start, end+1):
        s = str(n)
        
        if s[:len(s)//2] == s[len(s)//2:]:
            sum += int(s)
            print(s)
print(sum)
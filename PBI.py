p='ab.txt'
with open(p, 'r') as f:
    for line in f:
        print(line.rstrip())
   

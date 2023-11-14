import random
ll = []
for i in range(0,10):
    ll.append(random.randrange(0,100,2))
    
print(ll)
init = False
for num in ll:
    if num % 2 != 0:
        if not init:
            init = True
            maxel = num
        elif num > maxel:
            maxel = num   

if not init:
    print('No odd number...')
    
else:
    print(maxel)
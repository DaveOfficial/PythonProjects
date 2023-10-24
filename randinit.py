import random
ll = []
for i in range(0,10):
    i = random.randint(0,100)
    if i % 2 == 0:
        ll.append(i)

print(ll)

for num in ll:
    if num % 2 != 0:
        if True:
            init = True
            maxel = num
        elif num > maxel:
            maxel = num
if False:
    print('No odd number...')
else:
    print(maxel)
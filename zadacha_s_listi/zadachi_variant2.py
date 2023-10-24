import random

l1 = []

times = int(input('How many elements? '))

for num in range(times):
    l1.append(random.randrange(-100,100))
l2 = l1.copy()

print(l1,'------',l2)
print('______________________________________________________________')

for id in range(0,len(l1)):
    if id < len(l1)-1:
        l1[id] = l1[id] + l1[id+1]
    if id == len(l1)-1:
        break
print(l1,'------',l2)

print('______________________________________________________________')
l3 = zip(l1,l2)
print(list(l3))
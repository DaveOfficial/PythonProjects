l1 = list()   

n = int(input('Enter number: '))

for num in range(1,n+1):
    l1.append(num)
    
print(l1)
print('__________________________________________________________________________')

d1 = dict()

for id in range(0,n):
    d1.update({ l1[id]:l1[-id-1]})
    
print(d1)


intn = int(input('Enter whole number:'))
l2 = []

for n in range(1,intn+1):
    l2.append(n)
    
print(l2)

dictionary = dict()

for i in range(0,len(l2)):
    dictionary.update({l2[i]:l2[-i-1]})
    
print(dictionary)

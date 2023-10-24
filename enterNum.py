import random
list1 = []
n = int(input("Enter number of elements : "))
 
for i in range(0, n):
    elementi = int(input())
 
    list1.append(elementi)
     
print(list1)
list1.reverse()
print(list1)
list2 = input().split(',')
random.shuffle(list2)
print(list2)
name = input()
list3 = list(name)
print(list3)
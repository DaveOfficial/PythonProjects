list1 = [1,45,67,42,12]
length = len(list1)

for i in range(0,length):
    if i == 1:
        list1.insert(4,list1[0])
    list1.pop(0)
    print(list1)
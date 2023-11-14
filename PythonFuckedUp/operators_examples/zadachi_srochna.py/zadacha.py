nums = int(input('Enter how many numbers you want?'))
l1 = list()
for n in range (0,nums):
    l1.append(int(input()))

list_sum = sum(l1)
print(list_sum)
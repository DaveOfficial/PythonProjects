user_input = list(input('Type down\n'))
my_dict = dict()
for i in user_input:
    my_dict.update({i : user_input.count(i)})
    
print(my_dict)
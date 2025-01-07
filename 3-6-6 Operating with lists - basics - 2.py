my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
changed_list = []

for i in range(len(my_list)):
    flag = False
    if my_list[i] in my_list[i+1:]:
        flag= True
    if not flag:
        changed_list.append(my_list[i])

my_list = changed_list[:]
#
print("The list with unique elements only:")
print(my_list)

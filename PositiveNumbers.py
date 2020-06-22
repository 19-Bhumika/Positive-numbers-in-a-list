list1=[12,-7,5,64,-14]
print(list1)
for num in list1:
    if(num>=0):
        print(num , end=" ")
print("\n")
list2=[12,14,-95,3]
print(list2)
new_list=list(filter(lambda i: i>=0 ,list2))
print(new_list)


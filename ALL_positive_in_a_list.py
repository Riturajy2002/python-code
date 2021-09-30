nums=[12,-7,5,64,-14]
print("Original number in the list",nums)
new_nums=filter(lambda x:x>0,nums)
print("positive numbers in the list are=",list(new_nums))
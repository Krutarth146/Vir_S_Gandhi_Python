list1 = []
print(type(list1))  # <class 'list'>

list3 = [10,10,90.90,True,[(10,20)], {10,20,10}, {"Name" : "Vir", "Address" : "Shahpur"}]

print(list3)   # [10, 10, 90.9, True, [(10, 20)], {10, 20}, {'Name': 'Vir', 'Address': 'Shahpur'}]

# List Characteristics: Ordered (Indexed)

# Indexing
print(list3[6])   # {'Name': 'Vir', 'Address': 'Shahpur'}
print(list3[-1])   # {'Name': 'Vir', 'Address': 'Shahpur'}
print(list3[1])   # 10
print(list3[2])   # 90.9

l3 = [10,20,[(10,20,30,(14,90,23,45,[40,20,10,{"Name" : "Vir", "address" : {'pincode' : [10,20,67,456]}}],78,45))]]

print(l3[-1])  # [(10, 20, 30, (14, 90, 23, 45, [40, 20, 10, {'Name': 'Vir', 'address': {'pincode': [10, 20, 67, 456]}}], 78, 45))]
print(l3[-1][0])  # (10, 20, 30, (14, 90, 23, 45, [40, 20, 10, {'Name': 'Vir', 'address': {'pincode': [10, 20, 67, 456]}}], 78, 45))
print(l3[-1][0][-1])  # (14, 90, 23, 45, [40, 20, 10, {'Name': 'Vir', 'address': {'pincode': [10, 20, 67, 456]}}], 78, 45)
print(l3[-1][0][-1][-3])  # [40, 20, 10, {'Name': 'Vir', 'address': {'pincode': [10, 20, 67, 456]}}]
print(l3[-1][0][-1][-3][-1])  # {'Name': 'Vir', 'address': {'pincode': [10, 20, 67, 456]}}
print(l3[-1][0][-1][-3][-1]['address'])  # {'pincode': [10, 20, 67, 456]}
print(l3[-1][0][-1][-3][-1]['address']['pincode'][-1])  # 456


# Slicing

l4 = [10, 90, 78, 67, 56 , 34, 24, 12 , 90, 89, 78, 57, 32, 21]

# print(l3[start : end (n-1) : step (n-1)])


print(l4[2:3])  # [78]
print(type(l4[2:3]))  # [78]   # <class 'list'>
print(l4[-3:5:1])  # []
print(l4[-2:-5:-2])  # [32,78]
print(l4[-4::])  # [78, 57, 32, 21]
print(l4[-4:-1:])  # [78, 57, 32]
print(l4[-4::-1])  # [78, 89, 90, 12, 24, 34, 56, 67, 78, 90, 10]
print(l4[-4:0:-1])  # [78, 89, 90, 12, 24, 34, 56, 67, 78, 90]
print(l4[:-4:])  # [10, 90, 78, 67, 56, 34, 24, 12, 90, 89]
print(l4[5:-5:3])  # [34, 90]
print(l4[6:-7:-1])  # []

# for i in range(-3,5,1):
#     print(i)

print(id(l4))  # 3004634956416
print(len(l4))  # 14  # starts from 1, Index starts from 0
print(min(l4))  # 10
print(max(l4))  # 90
print(all(l4))  # True   like and
print(any(l4))  # True   like or
print(sum(l4))  # 738   
print(l4.__sizeof__())  # 152


for k in l4:
    print(k,end=' ')   # 10 90 78 67 56 34 24 12 90 89 78 57 32 21

# for p in range(len(l4)):
#     print(l4[p])   # # 10 90 78 67 56 34 24 12 90 89 78 57 32 21


print(l4)
l4.append(90000)
l4.append("VIr Gandhi")
print(l4)   # [10, 90, 78, 67, 56, 34, 24, 12, 90, 89, 78, 57, 32, 21, 90000, 'VIr Gandhi']


# l4.extend(100)   # int object is not iterable.

l5 = [10,20,30]

l4.append(l5)
print(l4)   # [10, 90, 78, 67, 56, 34, 24, 12, 90, 89, 78, 57, 32, 21, 90000, 'VIr Gandhi', [10, 20, 30]]

# l4.extend(l5) 
# print(l4)    # [10, 90, 78, 67, 56, 34, 24, 12, 90, 89, 78, 57, 32, 21, 90000, 'VIr Gandhi', 10, 20, 30]

l4.extend("str")
print(l4)   # [10, 90, 78, 67, 56, 34, 24, 12, 90, 89, 78, 57, 32, 21, 90000, 'VIr Gandhi', [10, 20, 30], 's', 't', 'r']


l4.insert(2,"Patel")
print(l4)   # [10, 90, 'Patel', 78, 67, 56, 34, 24, 12, 90, 89, 78, 57, 32, 21, 90000, 'VIr Gandhi', [10, 20, 30], 's', 't', 'r']

del l4[5:]

print(l4)   # [10, 90, 'Patel', 78, 67]

l4.insert(-1,"Manish")
print(l4)   # [10, 90, 'Patel', 78, 'Manish', 67]

l4[2] = "dhyan"
print(l4)   # [10, 90, 'dhyan', 78, 'Manish', 67]

# l4[10] = 'Gandhi'
# print(l4)  # Gives Error
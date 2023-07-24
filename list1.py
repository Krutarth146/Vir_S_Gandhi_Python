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


list1 = [10,20,1,1,1,1,3,2,10,20]
# 10 ---> [0,8]
# 20 ---> [1,9]
# 1  ---> [2,3,4,5]


unique = []

for i in list1:
    if i not in unique:
        unique.append(i)

temp = []
for ele in unique:   # i = 10
    # temp = []
    temp.clear()
    for ind in range(len(list1)):
        if ele == list1[ind]:
            temp.append(ind)

    print(ele, '---->', temp)



# ans = [ (90,2), (44,6), (10,20), (32,26)]



list2 = [(10,20), (90,2), (32,26), (44,6)]


def fun3(subtup):
    return subtup[-1]

list2.sort(key=fun3)
print(list2)


l4 = [[10,32], [3,], [555,32], [22,900], [10,20]]

n = 2

ans = []
temp = []

for sublist in l4:
    temp = []
    for ele in sublist:
        if len(str(ele)) == 2:
            temp.append(True)

        else:
            temp.append(False)
    
    if all(temp):
        print(sublist)
# print(ans)



print([i for i in list1 if all(len(str(j)) == k for j in i)])
# list1 = [10,20,44,333,20,88]

# # Allow's Duplicates, Mutable (Changeble), Ordered (Indexed)

# list1.append(500)
# # list1.extend(400)  # 'int' object is not iterable
# list1.extend([10,20,10,10])
# list1.extend([[200,2001], [10]])

# print(list1)  # [10, 20, 44, 333, 20, 88, 500, 10, 20, 10, 10, [200, 2001],[10]]

# list1.insert(-1,800)
# print(list1)   # [10, 20, 44, 333, 20, 88, 500, 10, 20, 10, 10, [200, 2001], 800, [10]]

# list1[-1] = 900

# print(list1)  # [10, 20, 44, 333, 20, 88, 500, 10, 20, 10, 10, [200, 2001], 800, 900]

# # list1[30] = 700

# # print(list1)  # list assignment index out of range

# rem_value = list1.pop()

# print(rem_value)  # 900
# print(list1) # [10, 20, 44, 333, 20, 88, 500, 10, 20, 10, 10, [200, 2001], 800]


# list1.pop(1)
# print(list1)  # [10, 44, 333, 20, 88, 500, 10, 20, 10, 10, [200, 2001], 800]

# list1.remove(500)
# print(list1)   # [10, 44, 333, 20, 88, 10, 20, 10, 10, [200, 2001], 800]


# # del list1
# # print(list1)   # [10, 44, 333, 20]


# print(list1.index(10))  # 0
# print(list1.index(20,4))  # 6

# print(list1.count(230))  # 0
# del list1[4:]
# list1.sort()

# print(list1)  # [10, 20, 44, 333]

# list1.sort(reverse=True)
# print(list1)   # [333, 44, 20, 10]

# # list1.reverse()
# # print(list1)   # [333, 44, 20, 10]


# l2 = [(10,90), (55,32), (21,88), (3,2)]

# l2.sort()  # Sort By 1st Element

# print(l2)   # [(3, 2), (10, 90), (21, 88), (55, 32)]


# # def second_ele(subtup):
# #     return subtup[-1]

# # l2.sort(key=second_ele)   # Sort by Last ELement
# l2.sort(key=lambda subtup : subtup[-1])  # Anounomous Function
# print(l2)   # [(3, 2), (55, 32), (21, 88), (10, 90)]

# l3 = l2.copy()   # Shallow Copy  # ELement Copy
# l4 = list(l2)

# l4.append(400)

# l5 = l2   # Deep Copy  # REf SAme


# l5.append(400)
# print(l2)   # [(3, 2), (55, 32), (21, 88), (10, 90), 400]

# List Matrices


list1 = [[10,90,80], 
         [40,55,33], 
         [22,77,88]]


print(list1)
print(len(list1))   # 3

for sublist in list1:
    print(sublist)  # [10, 90, 80]


# [10, 90, 80]
# [40, 55, 33]
# [22, 77, 88]

c = 0
for sublist in list1:
    for ele in sublist:
        print(ele,end=' ')  # 10 90 80 40 55 33 22 77 88
        c+=1

print(c)  # 9


for r in range(len(list1)):
    for c in range(len(list1[r])):
        print(list1[c][r],end=' ')  # Transpose

    print()

# 10 90 80
# 40 55 33
# 22 77 88

# Spiral Hw
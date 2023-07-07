# while(num > 0)

# for(   ; num > 0 ;   )

for j in range(10):   # start - 0, End - 10 (n-1) = 9
    print(j,end=' ')   # 0 1 2 3 4 5 6 7 8 9

print()

for k in range(2,8):
    print(k,end=' ')  # 2 3 4 5 6 7 

print()

for riya in range(8,1):
    print(riya)   # No o/p

for m in range(-3,5,3):   # start , end(n-1), step (n-1)
    print(m,end=' ')  # -3 0 3

print()

for w in range(-4,-9,2):
    print(w)

print()

for j in range(10,-2,-2):
    print(j,end=' ')  # 10 8 6 4 2 0

print()

for k in range(5,-5,2):
    print(k,end=' ')
print()  # blank


list1 = [10,90,80,78,676]

for i in list1:
    print(i)

for j in range(len(list1)):
    print(list1[j])

for k in range(len(list1)-1,-1,-1):
    print(list1[k],end=' ')

print()

for i in reversed(list1):
    print(i)
print()


# list1.reverse()
# for i in list1:
#     print(i)
# print()


# list1 = [10,90,80,78,676]
# for i in list1[::1]:
#     print(i)

# for i in list1[::-1]:
#     print(i)
# print()
# for i in list1[:0:-1]:
#     print(i)

counter = 0

for k in range(1):   # k = 1
    for s in range(1,2):   # s = 0
        for l in range(1,3): # l = 0  
            if s % l == 0:  
                continue
        else:
            print("sub for loop3 Else Executed")
        if k == s:
            break
        print(s)
    print(k)


print(counter)  # 18
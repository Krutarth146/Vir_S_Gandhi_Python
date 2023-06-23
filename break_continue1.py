k = 10

while k<=15:
    if k == 13:
        k+=1
        continue
    print(k,end=' ')  # 10 11 12 14 15 
    k+=1

print()
print()
f = 13

while f<=18:
    if f==15:
        break
    print(f,end=' ')   # 13 14
    f+=1

# ----------------------

j = 65

while j<=69:
    k = 66
    while k<=69:
        if j==k:
            break
        print(k,end=' ')
        k+=1
    print(j,end=' ')
    j+=1
# 66 67 68 69 65 66 66 67 66 67 68 66 67 68 69

print()
print()
print()
j = 25
k = 25

while j<=30:
    while k<=30:
        if j==k:
            k+=1
            continue
        print(k)
        k+=1
    print(j)
    j+=1


for i in range(2,8):
    for j in range(i):
        if i==j:
            break
        print(j)
    else:
        print("Internal Else Executed")
    if i % j == 0:
        break
    print(i)
else:
    print("External Else Executed")



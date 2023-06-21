l1 = [10, 90, 89, 78, 68]

# user_need = int(input("Enter a Number: "))


# for j in l1:
#     if j == user_need:
#         print("Element is Found")
#         break
# else:   # if loop is Naturally Executed then It will Run after the Loop
#     print("Not Found")
    

# if user_need in l1:
#     print("Element is Found")
# else:  
#     print("Not Found")

# Membership O/p --->  in, not in 


# Identity O/p

x = 90
y = 90

if x == y:
    print("x == y")

print(id(x))  # 2909881633808
print(id(y))  # 2909881633808
 
if x is y:
    print("x is y")

y += 10
print(id(x))  # 2909881633808
print(id(y))  # 2909881639632

l1 = [10,20,30]
l2 = [10,20,30]

if l1 == l2:
    print("l1 == l2")

if l1 is l2:
    print("l1 is l2")


l1 = l2   # Deep Copy   # Digilocker

if l1 is l2:
    print("l1 is l2------------")

l3 = l2.copy()   # Xerox  # Shallow Copy

if l3 is l2:   # 
    print("l3 is l2")


# ----------------------------------------------------

# Print Reverse Number
num = 907 # ----> 709


# while num != 0:
while num > 0:
    rem = num % 10
    print(rem,end='')
    num = num // 10


# Sum of odd Digits
print()
num = 907 # ----> 709
sum = 0

# while num != 0:
while num > 0:
    rem = num % 10
    if rem % 2 != 0:
        sum = sum + rem
    num = num // 10

print(sum)   # 16


# Palindrome Number
print()
num = 101 # ----> 709
rev = 0


xerox = num
# while num != 0:
while num > 0:
    rem = num % 10
    rev = rev * 10 + rem
    num = num // 10

print(rev)   # 101

if rev == xerox:   # 101 == 0
    print("Palindrome Number")



# Armstrong Number  1 to 10000
print()
num = 153  # ----> 3*3*3 + 5*5*5 + 1*1*1 ===>>  153 
rev = 0


xerox = num
# while num != 0:
while num > 0:
    rem = num % 10
    rev = rev
    num = num // 10

print(rev)   # 101

if rev == xerox:   # 101 == 0
    print("Armstrong Number")



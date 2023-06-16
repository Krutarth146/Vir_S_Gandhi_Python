# Typecasting ---> one datatype to Another Datatype

# 1. Implicit Tc
# 2. Explicit Tc

x = 90   # int 
y = 67.89  # float
print(x+y)  # 157.89   # Implicit

w = True   # Bool  ---> 1
q = 67     # int
print(w+q)   # 68   # Implicit

x = 32
y = 90 + 5j
print(x+y)   # (122+5j)

h = 'A'
# print(int(h))   # Gives Error
print(ord(h))   # 65
print(chr(100))   # d

k = '90'
print(int(k))  # 90
print(type(k))  # <class 'str'>

l = '32.90'
# print(int(l))  # Error

print(int(float(l)))  # 32    # Explicit

k = '34' 
g = 90

print(int(k)+g)   # Explicit Typecasting

print(round(32.90))  # 33
print(round(32.33))  # 32
print(round(32.332121,2))  # 32.33
print(round(32.33,1))  # 32.3
print(round(32.33,0))  # 32.0
print(round(32.33,-1))  # 30
print(round(32.33,-2))  # 0.0
print(round(52.33,-2))  # 100.0
print(round(52.33,-3))  # 0.0

import math

print(math.floor(34.99999))   # 34
print(math.ceil(34.001))   # 35
print(math.ceil(34.000))   # 34

print(-22 // 4)   # -6

print(25 / 2)  # 12.5   Float
print(25 // 2)  # 12   # floor Division

print(25 ** 2)   # 25 * 25   ----> 625
print(25 ** 4)   # 25 * 25   ----> 390625


# Operators

# 1. Arithmetic O/p   + - * / // % **

print(25 / 2)  # 12.5   Float
print(25 // 2)  # 12   # floor Division
print(25 % 2)  # 1
print(25 ** 2)  # 625
print(2**3**2)  # 512   # Right to Left



# 2. Assignment O/p  =  += -= *= /= //= %= **= <<= >>= ^= |= &=   (Low Priority)

x = 25

x += 20   # x = x + 20
x += 300
x //= 2
x *= 3
x %= 4

print(x)   # 0




# Bitwise O/p  &  |  ^  ~  <<  >>


print(bin(671))  # 1010011111

# 1010101111101

print(0b1010101111101)  # 32
print(0o100000)  # 32768
print(0xF)  # 15    


name = "Vir Gandhi"
print("%s" %name)   # Vir Gandhi
print("I have %d ruppes only." %600)   # I have 600 ruppes only.
print("I have %4.0f ruppes only." %600.9089)   # I have 600 ruppes only.
# print("I have %x ruppes only." % var name)   # Exponencial
print("I have %c ruppes only." %'A')   # I have A ruppes only.
print("I have %c ruppes only." %97)   # I have a ruppes only.



# AND Table (A*B)

# I/p  I/p  o/p
# 0    0    0
# 0    1     0
# 1    0     0
# 1    1     1

# OR Table (A+B)

# I/p  I/p  o/p
# 0    0     0
# 0    1     1
# 1    0     1
# 1    1     1


# XOR Table same = 0, else 1

# I/p  I/p  o/p
# 0    0     0
# 0    1     1
# 1    0     1
# 1    1     0



print(32 & 90)   # 0
print(32 | 90)   # 122
print(32 ^ 90)   # 122

print(255 << 2)   # 1020
print(bin(255))   # 1111111100.000

print(0b1111111100)  # 1020

print(45666 >> 3)   # 5708

print(~90)  # -91 
print(~(-90))  # 89 
print(~(~90))  # 90


# Comparison Operators   < > <= >= != ==

print(32 <= 32)   # True
print(32 != 32)   # False

if 78 > 90:
    print(False)
else:
    print(True)   

# True


# Logical Operators  and or not

print(90 and 78)   # 78
print(90 or 78)   # 90
print(not 90)   # False
print(not -78.90)   # False
print(not 0)   # True

num = 90

if num % 5 == 0:
    pass
# print numbers b/w 1 to 100 which  divisible by 5 or 7
# print 25 to 1 in reverse order which is divisible by 3
# print odd numbers without using if condition (b/w 1 to 100)
# print(Table) Ex. 2 * 1 = 2 .....

x = 1
while x <= 10:
    print(x)
    x+=1


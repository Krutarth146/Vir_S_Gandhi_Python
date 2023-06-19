# Fibonacci Series

# 0 1 1 2 3 5 8 .....

n1 = 0
n2 = 1

print(n1,n2,end=" ")

i=1
while i<=3:
    n3 = n1 + n2
    print(n3,end=' ')

    n1 = n2
    n2 = n3
    i+=1


# x = 12   # start Point

# while x < 24:   # Condition  END Point
#     print(x,end=' ')  # 12 13 14 15 16 17 18 19 20 21 22 23  # statements
#     x+=1   # Flow

print()
import random
x = random.randint(1,10)
print(x)
if x == int(input()):
    print("Correct Guess")
else:
    print("wrong")

# Random Module
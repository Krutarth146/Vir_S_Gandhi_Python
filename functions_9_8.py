# Type - 2 Without Return type and With arguments

def vir(num1 = 90, num2 = 4, name = "Vir1", price=4):
    print(num1*num2,name * price)

# vir(10,20,"Vir Gandhi ")  # 200 Vir Gandhi Vir Gandhi 
vir()   # 360 Vir1Vir1Vir1Vir1


def Ajay(num):
    # list1 = []
    # for i in range(num):  # 0
    #     list1.append(i)  # 0
    # return list1

    for i in range(num):
        yield i

# print(Ajay(5))  # <generator object Ajay at 0x000001AC25D89A10>

for i in Ajay(5):
    print(i)


x = Ajay(5)
print(x.__next__())   # 0
print(x.__next__())   # 1
print(x.__next__())   # 2
print(x.__next__())   # 3
print(x.__next__())   # 4

# --------------------------------------------------

# Lambda (Anounoumous Function - One Liner) 


def square(num):
    return num ** 2

print(square(5))   # 25


x = lambda num : num ** 2
print(type(x))  # <class 'function'>

print(x(34))   # 1156


y = lambda x,y,z = 60 : x+y+z
# print(y(10,20,30))  # 60
print(y(10,20))  # 90


# Quadratic Function  ---> a*x**2 + b*x + c

def quadratic_fun(a1,b1,c1):
    return lambda x : a1*x**2 + b1*x + c1


# kru = quadratic_fun(10,20,25)
# print(kru(5))  # 375

print(quadratic_fun(10,20,25)(5))   # 375


# Nested Lambda

x = lambda n1 ,n2 = 78: lambda x1, y1 : x1 + y1 + n1 + n2

# ans = x(10,20)

# print(ans(4,23))   # 57

print(x(10)(5,4))    # 97
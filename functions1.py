# Inbuilt Functions, User Defined Functions


# Function ---> 1. Func. Defination  2. Func. Calling


# Func. Types
# 1. Without Return Type and Without Arguments
# 2. Without Return Type and With Arguments
# 3. With Return Type and Without Arguments
# 4. With Return Type and With Arguments



# 1. Without Return Type and Without Arguments

def Nihar():   # Func. Defination
    print("Vir S Gandhi is Present Today.")


Nihar()   # Vir S Gandhi is Present Today.   # FUnc. Calling


# 2. Without Return Type and With Arguments

def Addition(a,x,p):
    print(a+x+int(p))


Addition(90, 78.89, '32')  # 200.89



def Multiplication(num1, num2=1,num3 = 1):  # Default Func.
    print(num1 * num2 * num3)

Multiplication(10,90,80)  # 72000
Multiplication(10,90)  # 900
Multiplication(10,90,80)  # 72000
Multiplication(10)  # 10


# 3. With Return Type and Without Arguments

def Vir():
    l1= [10,20,30,40,50]
    tup1= (10,20,30,556,323)
    return l1,tup1

print(Vir())   # ([10, 20, 30, 40, 50], (10, 20, 30, 556, 323))

x= Vir()
print(x)   # ([10, 20, 30, 40, 50], (10, 20, 30, 556, 323))

print(x[1][::-1])   # (323, 556, 30, 20, 10)
print(x[-1][::-1])   # (323, 556, 30, 20, 10)



# 4. With Return Type and With Arguments

def division(num1, num2):
    return num1 // num2

print(division(900,56))  # 16


# FIbonnacci

# 0 1 1 2 3 .....


def fibonnacci(step):


    n1,n2 = 0,1

    print(n1,n2,sep=' ',end=' ')

    for i in range(step-2):
        n3 = n1 + n2
        print(n3,end=' ')
        n1 = n2
        n2 = n3


fibonnacci(5)   # 0 1 1 2 3

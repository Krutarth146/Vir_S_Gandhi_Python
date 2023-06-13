# Single Line Comment

'''
Multi
Line
Comment
'''

# Python is Interpreted, Dynamic, High Level Lang. (Human Readable)

# Compiler ---> Whole code at a time
# Interpreter ---> Line By line Interpretation

print("hello")
print("hello")
print("hello")
print("hello")
print("Vir")


# Dynamic (Run Time Memory Allocation)

# int a;
# float b;
# int _1;

vir = 90
print(vir)  # 90
print(type(vir))  # <class 'int'>

# Print statement

print("Hello Vir",end=' ***** ')
print("Good Afternoon!")  # Hello Vir ***** Good Afternoon!

x = 90
y = 78.89
s = 45

print(x,y,s,sep='\t',end='              ')   # 90      78.89   45

print("Hello")   # 90      78.89   45              Hello

print("""
    Sarghasan Br.
    Gnr - 380001
    212121212
""")

name = "Vir"
ruppes = 500

print(name,'has',ruppes, 'Rs.' + ' only.')  # Vir has 500 only.
print(f"{name} has {ruppes + 5000} Rs. only.")  # fstring (Adv. Formatted String)
# Vir has 5500 Rs. only.


# scanf("%d",&num1);
n = 90  # int


num1 = int(input("Enter No1: "))  # str to int
num2 = int(input("Enter No2: "))  # str to int

print(num1 + num2)  # str + str (Concat)  # 30


# fstring ---> Calc + - * / // % **
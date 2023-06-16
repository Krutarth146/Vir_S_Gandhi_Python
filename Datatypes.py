# Datatypes

x = 9000000000000000000000222222222222222

print(x)  # 90
print(type(x))   # <class 'int'>
print(x.__sizeof__())  # 44

_1 = 9000000000000000000000222222222222222.0
print(type(_1))   # <class 'float'>
print(_1.__sizeof__())  # 24


x = 'w'
print(type(x))  # <class 'str'>

f = "jkl"
print(type(f))  # <class 'str'>

w = 'True'
print(type(w))  # <class 'str'>

g = False
print(type(g))  # <class 'bool'>

l = None
print(type(l))   # <class 'NoneType'>

f = 8 + 7j   # 8 is Real Part, 7j is Imaginary Part
print(type(f))   # <class 'complex'>
 
# Collections

l1 = [10,10,20,45.90, "sre1", True, [(5,10,10), {10,20,30,}, {'Name' : "Vir", 'Surname' : 'Gandhi'}]]
print(type(l1))   # <class 'list'>
print(len(l1))   # 7  ----> Length starts from 1, Index starts from 0

print(l1.__sizeof__)   # <built-in method __sizeof__ of list object at 0x0000022C992A2680>
print(l1.__sizeof__())   # 96

print(id(l1))   # 2016448947840

tup2 = tuple()
tup3 = list()

tup1 = ()
tup1 = (10,10,20,45.90, "sre1", True, [(5,10,10), {10,20,30,}, {'Name' : "Vir"}])
print(tup1)   # (10, 10, 20, 45.9, 'sre1', True, [(5, 10, 10), {10, 20, 30}, {'Name': 'Vir'}])

print(type(tup1))  # <class 'tuple'>

set1 = {}
print(type(set1))   # <class 'dict'>

set2 = {10,}
print(type(set2))  # <class 'set'>

dict5 = {'Name' : "Mohan", 'roll' : [10,20,30,40,50]}
print(dict5)   # {'Name': 'Mohan', 'roll': [10, 20, 30, 40, 50]}
print(type(dict5))   # <class 'dict'>

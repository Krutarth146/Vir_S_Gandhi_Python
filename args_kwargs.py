def mul(num1=10, num2 = 90, num3=0):
    return num1 + num2 + num3


print(mul(10,90))   # 100
print(mul(4,3,8))   # 15
print(mul())   # 100


def vir(num1, num2, *kru,ayush=90):
    print(type(kru))  # <class 'tuple'>
    # print(kru)  # (10, 20, 30, 40, 'Str1', [10, 20, 30], (10, 20), {10, 20}, {'Name': [10, 20, 30]})

    for k in kru:
        print(k,end=' ')
    print()
    print(kru[-1]["Name"][-2])  # 20


vir(10,20,30,40,"Str1", [10,20,30], (10,20), {10,20}, {"Name" : [10,20,30]})


# -------------------------------------------


# kwargs -----> Dict()  ----> key (Unique), value (Allow's Duplicates)

def royal(*args,**gandhi):
    print(gandhi)   # {'name': 'Aman', 'roll': 900, 'salary': 90}
    print(type(gandhi))

    for key,val in gandhi.items():
        print(key,"- - - - ",val,end='\n')

    print(args)

    gandhi["Surname"] = "Gandhi"

    print(gandhi)


dict1 = {"name" : "Aman", "roll" : 900, "salary" : 90}
royal(90,80,79,67,dict1)



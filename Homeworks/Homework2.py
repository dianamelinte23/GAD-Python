# 1. Sa se scrie o functie care primeste un numar nedefinit de parametri
# Sa calculeze suma parametrilor care reprezinta numere intregi sau reale

def my_function(*args, **kwargs):
    result = 0
    for i in args:
        if isinstance(i, (int, float)):
            result += i
    for i in kwargs.values():
        if isinstance(i, (int, float)):
            if i != 2:
                result += i
    return print(result)

my_function(1,5,-3, 'abc', [12, 56, 'cad'])
my_function()
my_function(2, 4, 'abc', param_1 = 2)

# 2. Sa se scrie o fct recursiva care primeste ca parametru un nr intreg si returneaza:
# suma tuturor nr de la [0,n]
def first_func(n):
    if n < 1:
        return 0
    else:
        return n + first_func(n-1)

print(f"Suma tuturor numerelor de la [0,n]: {first_func(6)}")

# suma numerelor pare de la [0,n]
def second_func(n):
    if n < 1:
        return 0
    if n % 2 == 0:
        return n + second_func(n-2)
    else:
        return second_func(n-1)
print(f"Suma tuturor nr pare de la [0,n]: {second_func(6)}")

# suma numerelor impare de la [0,n]
def third_func(n):
    if n<2:
        return 1
    if n%2 > 0:
        return n + third_func(n-2)
    else:
        return third_func(n-1)

print(f"Suma tuturor nr impare de la [0,n]: {third_func(6)}")

# 3. Sa se scrie o fucntie care citeste de la tastatura
# si returneaza valoarea daca aceasta este un nr intreg

def verify():
    n = input("Introdu o valoarea: ")
    try:
        print (f"{int(n)} este un numar intreg")
    except ValueError as err:
        print (f"{n} nu este un numar intreg => {err}")
    else:
         print("No errors found!")
verify()


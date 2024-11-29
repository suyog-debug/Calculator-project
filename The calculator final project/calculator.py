def add(a,b):
    return a+b
def substract(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def divide(a,b):
    return a/b
operator={
    "+":add,
    "-":substract,
    "*":multiplication,
    "/":divide,
}
for i in operator:
    print(i)
def calculation():
    recalculation=True
    a=float(input("enter the first number; "))
    while recalculation:
        b=float(input("enter the second number; "))
        sign=input("enter the sign; ")
        answer=operator[sign](a,b)
        print(f'{a}{sign}{b}={answer}')
        further_calculation=input("type y if you wanna do further calculation with {a} or no for end the calculation")
        if further_calculation=="y":
            a=answer
        else:
            recalculation=False
            print('/n'*22)
calculation()


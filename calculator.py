def add(num1,num2):
    result =  num1+num2
    print(num1 , "+", num2 , "=" , result)

def sub(num1,num2):
    result =  num1-num2
    print(num1 , "-", num2 , "=" , result)

def mul(num1,num2):
    result =  num1*num2
    print(num1 , "*", num2 , "=" , result)


def div(num1,num2):
    result =  num1/num2
    print(num1 , "/", num2 , "=" , result)

choice = input("enter a choice + - * / : ")
first_number =  int(input("enter first number  : "))
second_number= int(input("enter second number  : " ))

if choice == "+":
    add(first_number,second_number)

if choice == "-":
    sub(first_number,second_number)

if choice == "*":
    mul(first_number,second_number)

if choice == "/":
    div(first_number,second_number)
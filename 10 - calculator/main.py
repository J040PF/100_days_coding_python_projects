from data import logo

print(logo)

def sum(num1, num_2):
    return(num1+num_2)

def sub(num1, num_2):
    return(num1-num_2)

def div(num1, num_2):
    return(num1/num_2)

def multiply(num1, num_2):
    return(num1*num_2)

num_1 = float(input("Type the first number"))
operator = input("Type the the operation do you want to do ( - , +, * , /) ")
num_2 = float(input("Type the second number"))
operations = {"-":sub(num_1, num_2), 
              "+":sum(num_1, num_2), 
              "/":div(num_1, num_2), 
              "*":multiply(num_1, num_2)
              }

print(f" your result is { operations[operator] } ")
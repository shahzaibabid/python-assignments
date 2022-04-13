
def add(num1,num2):
    return num1+num2

def sub(num1,num2):
     return num1-num2
        
def mul(num1,num2):
    return num1*num2
    
def div(num1,num2):
    return num1/num2
    
print("write add for addition")
print("write sub for Subtraction")
print("write mul for Multiply")
print("write div for Division")

while True:
   
    select = input("Enter operator(add/subtract/multiply/divide): ")


    if select in ('add', 'subtract', 'multiply', 'divide'):
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        if select == 'add':
            print(num1, "+", num2, "=", add(num1, num2))

        elif select == 'subtract':
            print(num1, "-", num2, "=", sub(num1, num2))

        elif select == 'multiply':
            print(num1, "*", num2, "=", mul(num1, num2))

        elif select == 'divide':
            print(num1, "/", num2, "=", div(num1, num2))
        
      
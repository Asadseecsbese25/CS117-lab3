def addition(a,b):
  return a+b
def subtraction(a,b):
  return a-b
def division(a,b):
  if b==0 :
    return"error,b can't be zero"
  return a/b
def multiplication(a,b):
  return a*b
def floordivision(a,b):
  if b==0:
    return"error,b can't be zero"
  return a//b
def modulus(a,b):
  if b==0 :
    return"error,b can't be zero"
  return a%b
def exponent(a,b):
  return a**b
def evenodd(number):
  if number%2==0:
    return "Number is even"
  else:
    return"Number is odd"
def percentage(obtained,total):
  if total==0:
    return"error,total marks can't be zero"
  return f"percentage = {(obtained/total)*100}%"


while True:
      print("Type  a  operation :\naddition,\nsubtraction,\ndivision,\nmultiplication,\nfloordivision,\nmodulus,\nexponent,\nevenodd,\npercentage")
      operation=input("enter the operation : ")
      if operation in["addition","subtraction","division","multiplication","floordivision","modulus","exponent"]:
        a =float(input("enter first no :"))
        b =float(input("enter second no :"))
        if operation == "addition":
          print("RESULT =",addition(a,b))
        elif operation == "subtraction":
          print("RESULT =",subtraction(a,b))
        elif operation == "division":
          print("RESULT =",division(a,b))
        elif operation == "multiplication" :
          print("RESULT =",multiplication(a,b))
        elif operation == "floordivision": 
          print("RESULT =",floordivision(a,b))
        elif operation == "modulus":
          print("RESULT =",modulus(a,b))
        elif operation == "exponent":
          print("RESULT =",exponent(a,b))
      elif operation == "evenodd":
        number=int(input("enter the number : "))
        print(evenodd(number))
      elif operation == "percentage":
        obtained=float(input("enter obtained marks : "))
        total=float(input("enter total marks : "))
        print(percentage(obtained,total))
      else:
        print("invalid operation")
      again =input("Do you want another calculation: (yes/no)\n")
      if again != "yes":
        print("Good Bye !")
        break

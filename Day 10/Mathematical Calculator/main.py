from art import logo

# add
def add(a,b):
  return a+b

# subtract
def subtract(a,b):
  return a-b

# multiply
def multiply(a,b):
  return a*b


def divide(a,b):
  return a/b

operation={"+":add,
           "-":subtract, 
           "*":multiply , 
           "/":divide  }

def calculator():
  print(logo)
  num1=int(input("Enter first number:  "))
  for symbols in operation:
    print(symbols)
  for_continue=True
  
  while for_continue:
    operation_symbol=input("Enter operation you want to do:  ")
    if operation_symbol in operation:
      num2=int(input("Enter Second number:  "))
      function=operation[operation_symbol]
      result=function(num1,num2)
      print(f"{num1}  {operation_symbol} {num2} =  {result}")
      x=input("Write 'y' for continue \n 'n' for stoping \n 'm' for opertion symbols \n 'cal' for new calculator   ")
      if x =="n":
        x= False
      elif x=="cal":
        num1=0
        num2=0
        result=0
        calculator()
      elif x=="m":
        for symbols in operation:
          print(symbols)
      num1= result
        
    else:
      print("Enter a wrong symbol plz correct it.")
      

calculator()
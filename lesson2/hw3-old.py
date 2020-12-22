myinput = 0
total = 0
operands = []
operators = []

# function to check user input
def user_input():
   while True:
      try: 
         inp = input(">>> ")
         if (inp == "exit"):
            return -1
         elif (inp == "+"):
            return '+'
         elif (inp == "-"):
            return '-'
         elif (inp == "*"):
            return '*'
         elif (inp == "/"):
            return '/'
         elif (inp == "="):
            return '='
         else:
            inp = float(inp)
            return inp
      except ValueError:
         print ("Invalid Character. Please type numbers or operations: [+ - * /].\nType \"exit\" to leave application.")
         continue

# function to calculate 
def calc(a,b,operator):
   if operator == "+":
      return f"{a} + {b} = {a+b}"
   elif operator == "-":
      return f"{a} - {b} = {a+b}"
   elif operator == "*":
      return f"{a} * {b} = {a+b}"
   elif operator == "/":
      if b != 0:
         return f"{a} / {b} = {a/b}"
      else:
         return 0

# main program
while myinput != -1:
   myinput = user_input()

   # if numbers
   if(isinstance(myinput, (float, int)) and myinput != -1):
      if len(operands) == 2:
         print("input operators: [ + - * / ]")
         continue
      else:
         operands.append(myinput)
   
   elif (myinput == "=") and (len(operands) == 2) and (len(operators) == 1):
      if len(operators) == 1 and len(operands) == 2:
         total = calc(operands[0],operands[1],operators[0])
         print(f"result: {total}")
         operands = []
         operators = []
         continue

   elif (myinput == "+") and (len(operators) == 0):
      operators.append("+")
      continue
   
   elif (myinput == "-") and (len(operators) == 0):
      operators.append("-")
      continue
   
   elif (myinput == "*") and (len(operators) == 0):
      operators.append("*")
      continue
   
   elif (myinput == "/") and (len(operators) == 0):
      operators.append("/")
      continue

mainArray = ['+']
userInput = 0
# function of user input cycle
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

# function to do a math operation on two operands
def calc(a,b,operator):
   debugPrintValues = False
   if operator == "+":
      if debugPrintValues: print (f"{a} + {b} = {a+b}")
      return a+b
   elif operator == "-":
      if debugPrintValues: print (f"{a} - {b} = {a-b}")
      return a-b
   elif operator == "*":
      if debugPrintValues: print (f"{a} * {b} = {a*b}")
      return a*b
   elif operator == "/":
      if b != 0:
         if debugPrintValues: print (f"{a} / {b} = {a/b}")
         return a/b
      else:
         print ("division by zero!")
         exit(1)
         return 0

# function to check if input is a number
def isNumber(input):
   if isinstance(input, (float, int)): 
      return True
   else:
      return False

# calculate array
def final_calculation(input):
   debugPrintValues = True
   res=0.0
   # remove first element '+' from the list.
   # This is used to check input in the main cycle.
   input = input[1:]
   print(f"Calculating: {input}")
   # assign first value of an array to result.
   res = input[0]
   
   for i in range(0, len(input)-2, 2):
      if debugPrintValues: print(f"i: {i}\t{res}{input[i+1]}{input[i+2]}={calc(res,input[i+2],input[i+1])}")
      res = calc(res,input[i+2],input[i+1])
   
   print (f"RESULT: {res}")

# main program cycle
# mainarray = ['+', 1.0, '+', 5.0, '/', 2.0, '*', 6.0, '-', 4.0, '/', 8.0, '+', 10.0, '*', 5.0] # 58.75
# final_calculation(mainarray)
while userInput != -1:
   userInput = user_input()

   # check if input is a number.
   # isNumber(mainArray[-1] is used to check for previous array element.
   # Array is initialized with '+' char, so on first input 
   # not isNumber(mainArray[-1] will always be False.

   if isNumber(userInput) and not isNumber(mainArray[-1]):
      mainArray.append(userInput)
      print (mainArray)
      continue
   
   elif (userInput == "="):
      # add: remove 1st element
      final_calculation(mainArray)
      break

   elif (userInput == "+") and isNumber(mainArray[-1]):
      mainArray.append("+")
      print (mainArray)
      continue
   
   elif (userInput == "-") and isNumber(mainArray[-1]):
      mainArray.append("-")
      print (mainArray)
      continue
   
   elif (userInput == "*") and isNumber(mainArray[-1]):
      mainArray.append("*")
      print (mainArray)
      continue
   
   elif (userInput == "/") and isNumber(mainArray[-1]):
      mainArray.append("/")
      print (mainArray)
      continue


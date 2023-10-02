#python program  for simple calculator
# fuction to add two numbers
def add(num1 + num2):
    return num1 + num2

# function to subtract two numbers
def substract(num1,num2):
    return num1-num2

# function to multiply two numbers
def multiply(num1 * num2):
    return num1 * num2

# function to divide two numbers
def divide(num1 / num2):
    return num1 / num2

print("please select operation -\n" \
               "1.   add\n"   \
                "2.   subtract\n"   \
                "3.   multiply\n"   \
                "4.    divide\n"   \
                
  #take input from the user 
  # 
  select = int(input("select operation from 1,2,3,4;"))              
  number_1 = int(input("enter first number:"))
  number_2 = int(input("enter second number:"))

  # if select == 1:
     print(number_1, "+", number_2,"=", 
                          add(number_1, number2))

    # select == 2:
       print(number_1, "-", number_2, "=";                      
                      subtract(number_1, number2))

   #  elif select == 3:                 
             print(number_1, "*", number_2,  "=",
                                multiply(number_1, number2))

       elif select == 4:
                  print(number_1, "/", number_2, "=")  
                        add(number_1, number2))  

         #  else:                                 
            #   print("invalid input")

      #  please select operation -       
      #  1. add 
      #  2.substract
       # 3.multiply
       # 4.divide

      #  select operations form 1, 2, 3, 4:4
      #  Enter first number:45
       # Enter second number:9
      #  45/9=5.0
Print("Python Calculator")
Print("Made By Code With Maaz")
Print("Made By Code With Maaz")
Print("Made By Code With Maaz")
Print("Made By Code With Maaz")


num1 = input('Enter first number: ')
num2 = input('Enter second number: ')   

#the sum of the two numbers variable
sum = float(num1) + float(num2)
sum2 = float(num1) - float(num2)
sum3 = float(num1) * float(num2)
sum4 = float(num1) / float(num2)

#what operator to use
choice = input('Enter an operator, + = addition, - = subtraction, * = multiplication and / = division: ')
#different sums based on the operators
if choice == '+': 
  print('The sum of {0} and {1} is {2}'.format  (num1, num2, sum))

elif choice == '-':
    print('The sum of {0} and {1} is {2}'.format(num1, num2, sum2))

elif choice == '*':
    print('The sum of {0} and {1} is {2}'.format(num1, num2, sum3))a

elif choice == '/':
    print('The sum of {0} and {1} is {2}'.format(num1, num2, sum4))

else:
      print("Invalid input!")

   #Made by code with maaz

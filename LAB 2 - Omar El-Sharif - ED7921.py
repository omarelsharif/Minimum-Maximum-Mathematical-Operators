

# Lab 02 



number = input ("Enter an integer between 1000 and 9999 ")

number = int(number)

1234

digit1= number % 10
number = number // 10
digit2 = number % 10
number = number // 10
digit3 = number % 10
digit4 = number // 10



print ("The 4 digits are", digit4, " ", digit3, " ", digit2, " ", digit1)

minimum = min(digit1,digit2,digit3,digit4)
maximum = max(digit1,digit2,digit3,digit4)



total = digit1+digit2+digit3+digit4
print ("The sum of the 4 digits is ", total)




print ("The minimum of the 4 digits is ", minimum)
print ("The maximum of the 4 digits is ", maximum)









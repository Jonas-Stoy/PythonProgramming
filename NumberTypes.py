"""
Programmer: Jonas Stoy
Program: Number type
Created on: 9-26-2022
Last updated on: 9-26-2022
Version: 3.7.9

"""
print("Welcome to Mathematical Operations")
print("1 Odd numbers \n"
      "2 Even numbers \n"
      "3 Prime Numbers \n"
      "4 Perfect Numbers \n"
      "5 Palindrome")
choice = int(input ("Choose the operation by selecting a number:\t"))
if choice == 1:
    print("Printing odd numbers from the first 100 natural numbers")
    for i in range (0, 101):
          if (i&2 != 0):
                print(i,end= " ")

elif choice == 2:
    print("Printing even numbers from the first 100 natural numbers\n")
    for i in range (0,101):
      if (i%2 != 0):
            print(i,end=" ")

elif choice == 3:
     print("Prime numbers from first 100 numbers")
     counter = 0 #intializing counter variable to 0
     n = 100
     for n in range (1, 101): #Checking number of divisors for a number
        for i in range(2, int(n/2+1)): #interating for numbers between 2 and n/2+1
           if (n/i == 0): #Check for reminder is 0
                 counter = counter+1 #Increase the counter if you find a divisor
                 if counter == 0: #decision to see if counter is 0 i.e. no divisors
                   print(n,end=" ") #printig the number is prime
                 counter = 0

elif choice == 4:
    print("Perfect numbers from first 100 natural numbers")
    sum = 0
    check = 0
    n = 100
    for n in range (1, 101):
        for i in range(1, int(n/2+1)):
            check = n % i
            if (check == 0):
                sum = sum + i
        if sum == n:
            print(n,end=" ")
            sum = 0

elif choice == 5:
    number=int(input("Please enter your number"))
    reverse = 0
    originalNumber = number
    while number > 0:
        remainder = number%10
        reverse = reverse*10+remainder
        number = number/10
    if originalNumber==reverse:
        print(originalNumber, "is a palindrome number")
    else:
        print(originalNumber, "is not a original number")

# Programmer : Jonas
#Program : Oddnumbers
#First changed : 9-21-2022 08:04:00
# Last changed : 9-21-2022 08:04:00
# Version : 3.7.9

# print("Printing odd numbers from the first hundred natural number")
#
# for i in range (0,101):
#    if (1%2 != 0):
#        print(i,end= " ")
#
# print("Alternate Approach")
# for k in range(1, 51):
#      print(((2*k)-1), end='')

print("Printing odd numbers from first 100 natural numbers using while loop")
i=1
while i <= 100:
    if i%2!=0:
        print(i, end='')
    i=i+1




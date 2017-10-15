from task_2 import divisors()

R = int(input ("Could I ask you for a number? "))
k = len (task_2.divisors(R))
if k < 3:
    print ("Congratulations! It is a prime number!")
else:
    print ('Sorry, it is not a prime number')

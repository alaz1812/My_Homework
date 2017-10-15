print ("Hello, I have fixed my bugs! Check me!")
a = int (input("Add the first number: "))
b = int (input("Add the second number: "))
c = raw_input("Add an operator: ")

if  c == "+":
    y = a + b
elif c == '-':
    y = a - b
elif c == "*":
    y = a * b
elif c == "/":
        if (b != 0):
            y = a / b
        else:
            y = "Sorry, I have no idea how to split in zero"
else:
    y = 'Unknown operation'
print (y)
print ("Thanks for using me! ")
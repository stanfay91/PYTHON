doAgain = 'yes'
while doAgain == 'yes' or doAgain == 'Yes':
FarTemp = int(input("What is the temperture in Fahrenheit: "))
CelTemp = (FarTemp - 32) / 1.8
print("Your temp in Fahrenheit: ", FarTemp, " Your temp in Celsius: ", CelTemp)
doAgain = input("Do you want to do it again: ")
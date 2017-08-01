def largestNumber(a):
a.sort(reverse=True)
return a[0]
def smallestNumber(a):
a.sort()
 return a[0]
moreNumbers = 'yes'
totalNumbers=0
numberList=[]
while (moreNumbers == 'yes' or moreNumbers == 'Yes' and totalNumbers >= 2):
totalNumbers += 1
numbers = int(input("Please enter a number: "))
numberList.append(numbers)
if totalNumbers < 2:
print("Another number is required.")
else:
moreNumbers = input("Do you want to add more numbers: (yes/no)")
print("Your largest number is:", largestNumber(numberList))
print("Your smallest number is:", smallestNumber(numberList))
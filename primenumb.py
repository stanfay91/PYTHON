def prime(a):
if a== 1:
return True
elif a > 1:
n = a // 2
for i in range(1, n + 1):
if a % i == 0:
return False
return True
else:
return False
for number in range(2,100):
if prime(number):
print (number)
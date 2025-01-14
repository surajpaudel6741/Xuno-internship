import math
    
a =int( input("Enter a number"))
b = 0
count = 0
if a==1 or a == 0:
    b = 1
else:
    for i in range(2, int (math.sqrt(a))):
        count = count + 1
        if a % i ==0:
            b = 1
if b == 0:
    print(a, "is the prime number")
else:
    print(a, "is not a prime number")
print (count)

# a =int( input("Enter a number"))
# b = 0
# count = 0
# if a==1 or a == 0:
#     b = 1
# else:
#     for i in range(2, int (a/2)):
#         count = count + 1
#         if a % i ==0:
#             b = 1
# if b == 0:
#     print(a, "is the prime number")
# else:
#     print(a, "is not a prime number")
# print (count)

# a =int( input("Enter a number"))
# b = 0
# count = 0
# if a==1 or a == 0:
#     b = 1
# else:
#     for i in range(2, a):
#         count = count + 1
#         if a % i ==0:
#             b = 1
# if b == 0:
#     print(a, "is the prime number")
# else:
#     print(a, "is not a prime number")
# print (count)
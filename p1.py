
# Assingment 1.1: WAP to print your name three times
for i in range(0,3,1):
    print("siddhant")

'''
Assingment 2.1: WAP to add three numbers and print the result.
Assingment 2.2: WAP to concatinate three strings and print the result.
'''
def addNumbers(a, b, c):
    a = int(a)
    b = int(b)
    c = int(c)
    return (a + b + c)

print(addNumbers(1,-2,3))

def concatString(str1, str2, str3):
    s1 = str(str1)
    s2 = str(str2)
    s3 = str(str3)
    return str(s1+s2+s3)

print(concatString("hello", " hoo haa ", "!!!!"))

'''
Assingment 4.1: WAP to print the table of 7, 9.
Assingment 4.2: WAP to print the table of n and n is given by user.
Assingment 4.3: WAP to add all the numbers from 1 to n and n is given by user.
'''
for i in range(1,11,1):
    print(7*i)
    print("\b")
for i in range(1,11,1):
    print(9*i)
    print("\b")

num = int(input("enter a number: "))
sum = 0
for i in range(1,11,1):
    print(num*i)
    print("\b")
    
for j in range(1,num,1):
    sum+=j
print("the final sum is: ",sum)

'''
Assingment 5.1: WAP to find max amoung three numbers and input from user. [Try max() function]
Assingment 5.2: WAP to add all numbers divisible by 7 and 9 from 1 to n and n is given by the user.
Assingment 5.3: WAP to add all prime numbers from 1 to n and n is given by the user.
'''

def maxNumber(a,b,c):
    a = int(a)
    b = int(b)
    c = int(c)
    return max(a,b,c)
print(maxNumber(1,2,3))

sum2 = 0
for i in range(1,num,1):
    if(i % 7 and i % 9):
        sum2+=i
    else:
        continue

def isPrime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

print(isPrime(31))

def printPrimes(num):
    for i in range(2,num):
        if(isPrime(i)):
            print(i)

printPrimes(10)

'''
Assingment 6.1: WAP using function that add all odd numbers from 1 to n, n is given by the user.
Assingment 6.2: WAP using function that add all prime numbers from 1 to n, n given by the user.
'''

sumOfPrimes = 0, sumOfOdd = 0
def addOddNumbers(a):
    for i in range(0,a):
        if(i % 2 != 0):
            sumOfOdd+=i

    print("sum of the odd numbers upto", a, " is:", sumOfOdd)

def addPrimeNumbers(a):
    for i in range(2,a):
        if(isPrime(i)):
            sumOfPrimes+=i
    print("sum of the prime numbers upto ", a, " is ->", sumOfPrimes)


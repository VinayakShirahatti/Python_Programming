# n = int(input("Enter a number "))
# if n % 2 == 0:
#     print(f"{n} is an even number")
# else:
#     print(f"{n} is an odd number")


# def custom(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False


# n = int(input("Enter a number "))
# flag = custom(n)

# if flag:
#     print(f"{n} is an even number")
# else:
#     print(f"{n} is an odd number")


# # OPTIMISED CODE!!!!!
# def custom(n):
#     return n % 2 == 0


# n = int(input("Enter a number "))
# flag = custom(n)

# if flag:
#     print(f"{n} is an even number")
# else:
#     print(f"{n} is an odd number")


# program to print all the even numbersof a user defined range


def even_odd(n):
    return n % 2 == 0


start = int(input("Enter the Start Value "))
end = int(input("Enter the end value "))

if start > end:
    print("Invalid Input")

else:
    for i in range(start, end + 1):
        flag = even_odd(i)

        if flag:
            print(i, end=" ")


def even_odd(n):
    return n % 2 == 0


start = int(input("Enter the Start Value "))
end = int(input("Enter the end value "))

if start > end:
    print("Invalid Input")

else:
    print("Even Num")
    for i in range(start, end + 1):
        flag = even_odd(i)
        if flag:
            print(i, end=" ")
    print("\nOdd Num")
    for i in range(start, end + 1):
        flag = even_odd(i)
        if not flag:
            print(i, end=" ")

# TC - O(2N)  == O(N)
# SC - O(1)

# WAP TO PRINT FIRST N EVEN NUMBERS


# def even_odd(n):
# return n % 2 == 0


# n = int(input("Enter a number "))

# count = 0
# number = 0
# while count < n:
#     flag = even_odd(number)
#     if flag:
#         count += 1
#         print(number, end=" ")
#     number += 1


# def even_odd(n):
#     return n % 2 == 0


# n = int(input("Enter a number "))
# i = 1
# while n > 0:
#     flag = even_odd(i)
#     if flag:
#         print(i, end=" ")
#         n -= 1
#     i += 1


# WAP TO PRINT FIRST N ODD NUMBERS


# def even_odd(n):
#     return n % 2 == 0


# n = int(input("Enter a number "))
# i = 1
# while n > 0:
#     flag = even_odd(i)
#     if not flag:
#         print(i, end=" ")
#         n -= 1
#     i += 1


# WAP TO CHECK WHETHER YEAR IS LEAP YEAR OR NOT

# year = int(input("Enter a number "))
# if (year % 100 != 0 and year % 4 == 0) or (year % 400 == 0):
#     print("Leap year")
# else:
#     print("Not Leap year")


# WAP TO CHECK WHETHER YEAR IS LEAP YEAR using customized functions


# def leap(year):
#     return (year % 100 != 0 and year % 4 == 0) or (year % 400 == 0)


# year = int(input("Enter a year "))
# flag = leap(year)
# if flag:
#     print("Leap year")
# else:
#     print("Not Leap year")


# WAP TO CHECK WHETHER YEAR IS LEAP YEAR using USER DEFINED RANGE


def leap(year):
    return (year % 100 != 0 and year % 4 == 0) or (year % 400 == 0)


start = int(input("Enter the start year "))
end = int(input("Enter the end year "))

if start > end:
    print("Invalid Input")
else:
    print("Leap--Year")
    for i in range(start, end + 1):
        flag = leap(i)
        if flag:
            print(i, end=" ")
    print("\nNon--Leap--Year")
    for i in range(start, end + 1):
        flag = leap(i)
        if not flag:
            print(i, end=" ")


# WAP TO COUNT THE NUMBER OF DIGITS IN A GIVEN INTEGER +VE OR -VE

n = int(input("Enter the num "))
if n < 0:
    # n = abs(n)
    n = n * (-1)
count = 0
while n > 0:
    n = n // 10
    count += 1
print(count)


# WAP TO COUNT A NO OF DIGITS OF A NUM USING CUSTOMISED FUNCTION


def count_digits(n):
    if n < 0:
        # n = abs(n)
        n = n * (-1)
    count = 0
    while n > 0:
        n = n // 10
        count += 1
    return count


n = int(input("Enter the num "))
print(count_digits(n))


# NOTE TO REMOVE A DIGIT FROM A GIVEN INTEGER : n // 10

# ARMSTRONG NUMBERS


def count_digits(n):
    count = 0
    while n > 0:
        n = n // 10
        count += 1
    return count


n = int(input("Enter the num "))
temp = n
ans = 0
if n < 0:
    # n = abs(n)
    n = n * (-1)
power = count_digits(n)
while n > 0:
    base = n % 10  # Extract digit
    ans = ans + (base**power)
    n //= 10
# if temp < 0:
#     ans = ans * -1
if temp == ans or temp == -ans:
    print(f"{temp} is an Amstrong Number")
else:
    print(f"{temp} is not a Amstrong number")


# CONVERT TO FUNCN


def count_digits(n):
    count = 0
    while n > 0:
        n = n // 10
        count += 1
    return count


def is_armstrong(n):
    temp = n
    ans = 0
    if n < 0:
        # n = abs(n)
        n = n * (-1)
    power = count_digits(n)
    while n > 0:
        base = n % 10  # Extract digit
        ans = ans + (base**power)
        n //= 10
    return temp == ans or temp == -ans


n = int(input("Enter the num "))
flag = is_armstrong(n)
if flag:
    print(f"{n} is an Amstrong Number")
else:
    print(f"{n} is not a Amstrong number")


# WAP TO PRINT ALL THE AMSTRONG NUMBER OF USER DEFINED RANGE


def count_digits(n):
    count = 0
    while n > 0:
        n = n // 10
        count += 1
    return count


def is_armstrong(n):
    temp = n
    ans = 0
    if n < 0:
        # n = abs(n)
        n = n * (-1)
    power = count_digits(n)
    while n > 0:
        base = n % 10  # Extract digit
        ans = ans + (base**power)
        n //= 10
    return temp == ans or temp == -ans


start = int(input("Enter the start range "))
end = int(input("Enter the end range "))
if start > end:
    print("Invalid Input")
else:
    print("Amstrong number")
    for i in range(start, end + 1):
        flag = is_armstrong(i)
        if flag:
            print(i, end=" ")


# WAP TO PRINT ALL THE AMSTRONG AND NON AMSTRONG NUMBER SEPERATELY OF A USER DEFINED RANGE


def count_digits(n):
    count = 0
    while n > 0:
        n = n // 10
        count += 1
    return count


def is_armstrong(n):
    temp = n
    ans = 0
    if n < 0:
        # n = abs(n)
        n = n * (-1)
    power = count_digits(n)
    while n > 0:
        base = n % 10  # Extract digit
        ans = ans + (base**power)
        n //= 10
    return temp == ans or temp == -ans


start = int(input("Enter the start range "))
end = int(input("Enter the end range "))
if start > end:
    print("Invalid Input")
else:
    print("Amstrong number")
    for i in range(start, end + 1):
        flag = is_armstrong(i)
        if flag:
            print(i, end=" ")
    print("\nNon Amstrong Number")
    for i in range(start, end + 1):
        flag = is_armstrong(i)
        if not flag:
            print(i, end=" ")

# WAP TO PRINT FIRST N AMSTRONG NUMBERS


def count_digits(n):
    count = 0
    while n > 0:
        n = n // 10
        count += 1
    return count


def is_armstrong(n):
    temp = n
    ans = 0
    if n < 0:
        # n = abs(n)
        n = n * (-1)
    power = count_digits(n)
    while n > 0:
        base = n % 10  # Extract digit
        ans = ans + (base**power)
        n //= 10
    return temp == ans or temp == -ans


n = int(input("Enter a number "))

print("Amstrong number")
i = 1
while n > 0:
    flag = is_armstrong(i)
    if flag:
        print(i, end=" ")
        n -= 1
    i += 1

# from collections import defaultdict

# nums=[1,1,2,3,3,4]
# count = defaultdict(int)
# for n in nums:
#     count[n] += 1
# print(count)

"""
REVERSE A NUMBER
"""
def reverse_num(n):
    temp = n
    if n < 0:
        n = n * (-1)
    rev = 0
    while n > 0:
        ld = n % 10
        rev = (rev * 10) + ld
        n //= 10
    return rev if temp > 0 else -rev


n = int(input("Enter the number "))
print(reverse_num(n))


"""
WAP TO REVERSE ALL THE NUMBERS IN A USER DEFINED RANGE
SR = 11, ER = 14
REVERSAL OF 11 IS 11
REVERSAL OF 12 IS 21
REVERSAL OF 13 IS 31
REVERSAL OF 14 IS 41
"""


def reverse_num(n):
    temp = n
    if n < 0:
        n = n * (-1)
    rev = 0
    while n > 0:
        ld = n % 10
        rev = (rev * 10) + ld
        n //= 10
    return rev if temp > 0 else -rev


start = int(input("Enter the Start Range "))
end = int(input("Enter the End Range "))

if start > end:
    print("Invalid Range")
else:
    for i in range(start, end + 1):
        ans = reverse_num(i)
        print(f"Reverse of {i} is {ans}")


""" 
WAP TO PRNT ALL THE INTEGER PALINDROMIC NUMBER OR NOT
"""


n = int(input("Enter the number "))
temp = n
if n < 0:
    n = n * (-1)
rev = 0
while n > 0:
    ld = n % 10
    rev = (rev * 10) + ld
    n //= 10
if rev == temp or temp == -rev:
    print("Number is Palindrome")
else:
    print("Number is not a palindrome")


""" 
WAP TO PRNT ALL THE INTEGER PALINDROMIC NUMBER OR NOT USING A CUSTOMISED FUNCTION
"""
def integer_palindrome(n):
    temp = n
    if n < 0:
        n = n * (-1)
    rev = 0
    while n > 0:
        ld = n % 10
        rev = (rev * 10) + ld
        n //= 10
    return True if temp == rev else temp == -rev


n = int(input("Enter the number "))
print(integer_palindrome(n))


""" 
WAP TO PRNT ALL THE INTEGER PALINDROMIC NUMBER IN A USER DEFINED RANGE
"""


# def integer_palindrome(n):
#     temp = n
#     if n < 0:
#         n = n * (-1)
#     rev = 0
#     while n > 0:
#         ld = n % 10
#         rev = (rev * 10) + ld
#         n //= 10
#     return True if temp == rev else temp == -rev


# start = int(input("Enter the start range "))
# end = int(input("Enter the end range "))
# print("Palindromic Integer Numbers")
# for i in range(start, end + 1):
#     flag = integer_palindrome(i)
#     if flag:
#         print(i, end=" ")


""" 
WAP TO PRNT ALL THE INTEGER PALINDROMIC AND NON PALINDROMIC NUMBER IN A USER DEFINED RANGE SEPERATELY
"""
def integer_palindrome(n):
    temp = n
    if n < 0:
        n = n * (-1)
    rev = 0
    while n > 0:
        ld = n % 10
        rev = (rev * 10) + ld
        n //= 10
    return True if temp == rev else temp == -rev


start = int(input("Enter the start range "))
end = int(input("Enter the end range "))
print("Palindromic Integer Numbers")
for i in range(start, end + 1):
    flag = integer_palindrome(i)
    if flag:
        print(i, end=" ")
print("\nNon Palindromic Integer Number")
for i in range(start, end + 1):
    flag = integer_palindrome(i)
    if not flag:
        print(i, end=" ")


""" 
WAP TO PRINT FIRST "n" PALINDROMIC NUMBERS
"""


def integer_palindrome(n):
    temp = n
    if n < 0:
        n = n * (-1)
    rev = 0
    while n > 0:
        ld = n % 10
        rev = (rev * 10) + ld
        n //= 10
    return True if temp == rev else temp == -rev


n = int(input("Enter the count of number "))
i = 1
while n > 0:
    flag = integer_palindrome(i)
    if flag:
        print(i, end=" ")
        n -= 1
    i += 1


"""  
WAP TO PRINT ALL THE FACTORS OF A GIVEN N NUMBER

"""
n = int(input("Enter a number "))
for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=" ")


def is_factor(n):
    for i in range(1, n + 1):
        if n % i == 0:
            print(i, end=" ")


n = int(input("Enter a number "))
is_factor(n)


def is_factor(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count


n = int(input("Enter a number "))
print(is_factor(n))


"""  
No of cycles taken to get all the factors of a given num
"""


def is_factor(n):
    count_factor = 0
    count = 0
    for i in range(1, n + 1):
        count_factor += 1
        if n % i == 0:
            count += 1
    return count_factor


n = int(input("Enter a number "))
print(is_factor(n))


"""  
OPTIMISED LOGIC (TIME COMPLEXITY = O(SQRT N))
"""

"""  
ALL THE FACTORS OF A GIVEN NUMBER CAN BE LISTED WITHIN THE SQUARE ROOT OF A GIVEN NUMBER  

NOTE- if 'i' is a factor of 'n' (i.e, n % i == 0) then 100% 'n // i' is also a factor of 'n'
All the factorsof a given number can be listed either witthin the direct square root of the number or nearest lowest squareroot of thr number.
"""
n = int(input("Enter the number "))
i = 1
while i * i <= n:
    if n % i == 0:
        print(i, end=" ")
        if n // i != i:
            print(n // i, end=" ")
    i += 1


def factors(n):
    i = 1
    while i * i <= n:
        if n % i == 0:
            print(i, end=" ")
            if n // i != i:
                print(n // i, end=" ")
        i += 1


n = int(input("Enter the number "))
factors(n)


def dispfact(n):
    countfact = 0
    countcycles = 0
    i = 1
    while i * i <= n:
        countcycles += 1
        if n % i == 0:
            countfact += 1
            print(i, end=" ")
            if (n // i) != i:
                countfact += 1
                print(n // i, end=" ")
        i += 1
    return countfact, countcycles


n = int(input("Enter number "))
resfact, rescycle = dispfact(n)
print(f"\nTotal factors {resfact}")
print(f"Total count cycles {rescycle}")

""" 
prime numbers
"""


def prime_no(n):
    countfact = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            countfact += 1
            if (n // i) != i:
                countfact += 1
        i += 1
    return countfact == 2


print(prime_no(23))


"""  
GCD OR HCF OF 2 no_
"""


def gcd(n1, n2):
    lower = n1
    if n2 < n1:
        lower = n2
    hcf = 1
    for i in range(2, lower + 1):
        if n1 % i == 0 and n2 % i == 0:
            hcf = i
    return hcf


n1 = int(input("Enter the first number "))
n2 = int(input("Enter the second number "))
print(gcd(10, 8))


"""  
WAP TO CHECK WHETHER THE GIVEN 2 NUMBERS ARE CO-PRIMES OR NOT!!
CO-PRIME - IF THE HCF OF THE GIVEN 2 NUMBERS IS 1 THEN IT IS SAID TO BE CO PRIMES
"""


def gcd(n1, n2):
    lower = n1
    if n2 < n1:
        lower = n2
    hcf = 1
    for i in range(2, lower + 1):
        if n1 % i == 0 and n2 % i == 0:
            hcf = i
    return True if hcf == 1 else False


n1 = int(input("Enter the first number "))
n2 = int(input("Enter the second number "))
print(gcd(10, 8))

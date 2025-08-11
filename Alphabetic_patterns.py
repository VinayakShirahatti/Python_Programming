#Alphabetic_Patterns

#ASCII VALUES :
# "A" TO "Z" : 65-90
# "a" to "z": 97-122
# "0"-"9" : 48-57
# " "[space] : 32

# Ordinal():
#    Syntax: ord(singlr_char)

#character():
    #  Syntax: chr(positive whole number)

# print(ord("B"))
# print(chr(99))
# print(ord(""))   #Error
# print(ord("abc")) #Error only one character needs to br given 
# print(chr(-19))   #Error negative cannot be given 


#Logic 
#Uppercase => (64+Val)
#Lowercase => (96+Val)

# n=int(input("Enter the number:"))
# for i  in range(1,(n+1)):
#     for j in range(1,(n+1)):
#         print(chr(64+j),end=" ")
#     print()

# Enter the number:4
# A B C D
# A B C D
# A B C D
# A B C D

# n=int(input("Enter the number:"))
# for i in range (1,(n+1)):
#     for j in range(1,(i+1)):
#         print(chr(96+j),end=" ")
#     print()

# Enter the number:4
# a
# a b
# a b c
# a b c d

"""
n=int(input("Enter the number:"))
for i in range(1,(n+1)):
    for j in range(1,(n+1)):
        if i%2==0:
            print(chr(96+j),end=" ")
        else:
            print(chr(64+j),end=" ")
    print()

"""


# Enter the number:4
# A B C D
# a b c d
# A B C D
# a b c d


"""
n=int(input("Enter the number:"))
for i in range (n,0,-1):
    for j in range(1,i+1):
        print(chr(96+j),end=" ")
    print()
"""

# Enter the number:4
# a b c d
# a b c
# a b
# a

"""
n=int(input("Enter the number:"))
for i in range(1,(n+1)):
    for j in range(i,n+i):
        print(chr(64+j),end=" ")
    print()
"""

# Enter the number:4
# A B C D
# B C D E
# C D E F
# D E F G

"""
n=int(input("Enter the number:"))
for i in range(1,(n+1)):
    for j in range(1,(n+1)):
        if i%2==0:
            if j%2==0:
                print(chr(96+j),end=" ")
            else:
                print(chr(64+j),end=" ")
        else:
            if j%2!=0:
                print(chr(96+j),end=" ")
            else:
                print(chr(64+j),end=" ")
    print()
"""

# Enter the number:4
# a B c D
# A b C d
# a B c D
# A b C d

"""
n=int(input("Enter the number:"))
count=1
for i in range(1,(n+1)):
    for j in range(1,(i+1)):
        if count%2==0:
            print(chr(96+count),end=" ")
            count+=1
        else:
            print(chr(64+count),end=" ")
            count+=1
    print()
"""

# Enter the number:4
# A
# b C
# d E f
# G h I j

"""
count=4
n=int(input("Enter the number:"))
for i in range(1,(n+1)):
    for j in range(1,(i+1)):
        print(chr(64+count),end=" ")
    count-=1
    print()
"""

# Enter the number:4
# D
# C C
# B B B
# A A A A

#Combinational_Patter
# n=int(input("Enter the number:"))
# noc=1
# for i in range(1,(n*2)):
#     for j in range(1,(noc+1)):
#         print("*",end=" ")
#     print()
#     if i<n:
#         noc+=1
#     else:
#         noc-=1

#cominational_pattern_with_spaces
# n=int(input("Enter the number:"))
# noc=1
# for i in range(1,(n*2)):
#     for k in range(n,noc,-1):
#         print(" ",end="")
#     for j in range(1,(noc+1)):
#         print("*",end="")
#     print()
#     if i<n:
#         noc+=1
#     else:
#         noc-=1

#Combinational_patter_Equal
# n=int(input("Enter the number:"))
# noc=1
# for i in range(1,(n*2)):
#     for k in range(n,noc,-1):
#         print(" ",end="")
#     for j in range(1,(noc+1)):
#         #Provide space in either "end" or "*" 
#         print("*",end=" ")
#     print()
#     if i<n:
#         noc+=1
#     else:
#         noc-=1

#Combinational_pattern
# n=int(input("Enter the number:"))
# noc=n
# for i in range(1,(n*2)):
#     for j in range(1,(noc+1)):
#         print("*",end=" ")
#     print()
#     if i<n:
#         noc-=1
#     else:
#         noc+=1

# n=int(input("Enter the number:"))
# noc=n
# for i in range(1,(n*2)):
#     for k in range(n,noc,-1):
#         print(" ",end="")
#     for j in range(1,(noc+1)):
#         print("*",end="")
#     print()
#     if i<n:
#         noc-=1
#     else:
#         noc+=1

# n=int(input("Enter the number:"))
# noc=n
# for i in range(1,(n*2)):
#     for k in range(n,noc,-1):
#         print(" ",end="")
#     for j in range(1,(noc+1)):
#         print("*",end=" ")
#     print()
#     if i<n:
#         noc-=1
#     else:
#         noc+=1


#Butterfly_Pattern
# n=int(input("Enter the number:"))
# noc=1
# nor=(n*2)-1
# for i in range (1,(n*2)):
#     for j in range(1,(n*2)):
#         if j<=noc or j>=nor:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
#     if i<n:
#         noc+=1
#         nor-=1
#     else:
#         noc-=1
#         nor+=1

#Hollow pattern
n=int(input("Enter the Number:"))
for i in range(1,(n+1)):
    for j in range(1,(n+1)):
        if (i==1 or i==n) or (j==1 or j==n):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
        
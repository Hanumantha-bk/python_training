#Recursion: Write Once ,Execute Multiple Times....
 
# def power(a,n):
#     if(n==0):
#         return 1
#     if(n%2==0):
#         return power(a*a,n/2)
#     return a*power(a*a,(n-1)/2)
# a=3
# n=2
# print(power(a,n))

# 2)
#def power(a,n):
#     if(n==0):
#         return 1
#     elif(n%2==0):
#         return power(a*a,n/2)
#     else:
#         return a*power(a*a,(n-1)/2)
# a=3
# n=2
# print(power(a,n))

# def power(a,n):
#     if(n==0):
#         return 1
#     if(n%2==0):
#         return power(a*a,n/2)
#     return a*power(a*a,(n-1)/2)
# a=3
# n=2
# print(power(a,n))    

# def pow(n,m):
#     if(n==0):
#         return 1
#     return n*pow(n,m-1)
# n=2
# m=3
# print(pow(n,m))


# def sum(n):
#     if n==0:
#         return -1  # Or We Can Use return 0
#     else:
#         return n%10+sum(n//10)
# num=123
# print(sum(num))

# REturn Last Digit Of Two Digit No
# def last_dgt(n):
#     if n==0:
#         return -1
#     else:
#         return abs(n)%10
# num=123
# print(last_dgt(num))


#REturn Second Last Digit Of Two Digit No
# def sec_dgt(n):
#     if n==0:
#         return -1
#     else:
#         return (n//10)%10
# num=1236
# print(sec_dgt(num))

# def pow(a,b):
#     if b==0:
#         return 1
#     else:
#         return a*pow(a,b-1)
# a=3
# b=2
# print(pow(a,b))
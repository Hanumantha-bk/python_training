def fact(n):
    if n==0:
        return 1
    elif n<0:
        print("Pos No") 
    elif n==1:
        return n
    else:
        return n*fact(n-1)
num=int(input("enter a num"))
print(fact(num))

# if num<0:
#     print("Write Positive Number")
# elif num==0:
#     print("Fact of 0! is 1")
# else:
#     print(fact(num))
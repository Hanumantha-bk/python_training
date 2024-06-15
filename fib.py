def fib(n):
    if n<=1:
        return n
    else:
        return(fib(n-1)+fib(n-2))
nt=int(input("Enter a  NUm :"))
for i in range(nt):
    print(fib(i))
# if nt<=0:
#     print("Enter a Positive no")
# else:
#     print("Fibo Sequ are:")
# for i in range(nt):
    # print(fib(i))
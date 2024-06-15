def prime(num):
    if num <= 1:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True
def n_p(num):
    next_num = num + 1
    while True:
        if prime(next_num):
            return next_num
        next_num += 1
n=int(input("enter a Prime No"))
if prime(n):
    print("Next Prime No:", n_p(n))
else:
    print("Not Prime No")

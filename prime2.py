# n to n/2
#It prints THe NexT Prime NuMber......
def isprime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
        return True
num=int(input())
k=num+1

while True:
    if isprime(k):
        print(k)
        break
    k=k+1
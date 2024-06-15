
n = 167
def sod(n):
    c = 0
    while n > 0:
        c += 1
        n //= 10
    return c

def rev(n):
    ans = 0
    while n > 0:
        dig = n % 10   
        sq = dig ** 2  
        sod_sq = sod(sq)
        ans = ans * (10 ** sod_sq) + sq 
        n = n // 10  
    return ans

def rev2(n):
    ans2 = 0
    while n > 0:
        dig = n % 10
        ans2 = ans2 * 10 + dig
        n //= 10
    return ans2
ans = rev(n)
res = rev2(ans)
print(res)  




def rev(n):
    ans = 0
    factor = 1
    while n > 0:
        dig = n % 10       
        sq = dig ** 2      
        ans += sq * factor 
        factor *= 10 ** (len(str(sq))) 
        n //= 10          
    return ans

def rev2(n):
    ans2 = 0
    while n > 0:
        dig = n % 10
        ans2 = ans2 * 10 + dig
        n //= 10
    return ans2


n = 167
ans = rev(n)
output = rev2(ans)
print(output)  

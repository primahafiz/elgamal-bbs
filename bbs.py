from seed import Seed
import time

class BBS:

    def modpow(self,x,n,mod):
        ret = 1
        while n > 0:
            if n&1:
                ret = ret * x % mod
            x = x * x % mod
            n >>= 1
        return ret

    def gcd(self,x,y):
        if y == 0:
            return x
        return self.gcd(y,x%y)

    def totient(self,x,y):
        ret = (x-1)*(y-1)
        ret //= self.gcd(x-1,y-1)
        return ret

    def random(self,p,q,k,x,ln):
        n = p*q
        t = self.totient(p,q)
        ans = 0
        for _ in range(ln):
            exp = self.modpow(2,k,t)
            num = self.modpow(x,exp,n)

            ans <<= 1
            ans |= (num&1)

            k = x
            x = num

        return ans




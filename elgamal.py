from bbs import BBS
from seed import Seed

class ElGamal:
    MESSAGE_LEN = 8
    def __init__(self,x,p) -> None:
        # p must be at max 31 bit
        self.x = x
        self.bbs = BBS()
        self.seed = Seed()
        self.p = p
        self.g = self.bbs.random(*self.seed.generateSeed(),ElGamal.MESSAGE_LEN) % p
        self.y = self.bbs.modpow(self.g,self.x,self.p)
    
    def modpow(self,x,n,mod):
        ret = 1
        while n > 0:
            if n&1:
                ret = ret * x % mod
            x = x * x % mod
            n >>= 1
        return ret

    def invMod(self,x,mod):
        return self.modpow(x,mod-2,mod)

    def encrypt(self,m):
        k = self.bbs.random(*self.seed.generateSeed(),ElGamal.MESSAGE_LEN) % self.p
        a = self.bbs.modpow(self.g,k,self.p)
        b = (self.bbs.modpow(self.y,k,self.p) * m) % self.p

        return a,b
    
    def decrypt(self,a,b):
        return b*self.invMod(self.modpow(a,self.x,self.p),self.p) % self.p

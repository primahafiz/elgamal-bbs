import time
import hashlib

class Seed:
    MAX_PRIME = 100000
    def __init__(self):
        self.sieve = []
        self.flag = [True for _ in range(Seed.MAX_PRIME)]
        for i in range(2,Seed.MAX_PRIME):
            if not self.flag[i]:
                continue
            self.sieve.append(i)
            for j in range(i*i,Seed.MAX_PRIME,i):
                self.flag[j] = False

    def generateDigest(self) :
        t = time.time()
        k = t * 1000000
        k = int(k)

        k = str(k)
        k = k.encode('utf-8')
        digest = hashlib.sha256(k).hexdigest()

        return int(digest,16)
    
    def generateSeed(self):
        digest = self.generateDigest()
        
        p = self.sieve[(digest & 0xFF)]
        digest >>= 16
        q = self.sieve[(digest & 0xFF)]
        digest >>= 16
        k = self.sieve[(digest & 0xFF)]
        digest >>= 16
        x = self.sieve[(digest & 0xFF)]
        digest >>= 16

        return p,q,k,x
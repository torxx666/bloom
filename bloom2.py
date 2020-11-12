from hashlib import blake2b
import struct
import sys


'''
    in this version we use a subset of the hash function
'''



class Bloom2():
    
    hashed = ''

    def __init__(self):
        self.bloom_hash = set()
        pass


    def get_n_hash(self,chain):
        self.h2 = blake2b(digest_size=2)
        self.h4 = blake2b(digest_size=4)
        self.h8 = blake2b(digest_size=8)

        encoded_str = chain.encode()
        self.h2.update(encoded_str)
        c2 = self.h2.hexdigest()

        self.h4.update(encoded_str)
        c4 = self.h4.hexdigest()
        self.h8.update(encoded_str)
        c8 = self.h8.hexdigest()
        return c2,c4,c8


    def and_value(self,value,shift):
        value =  int(value, 16)
        max_size = value.bit_length()
        base= 0
        for i in range(max_size):
            t = value & 0xffff
            base= base  | t
            value = value >> max_size
        resp = base << shift
        return resp

    def get_hash(self,chain):
        c2,c4,c8 = self.get_n_hash(chain)
        chain_hash = self.and_value(c2,2) ^ self.and_value(c4,8) ^ self.and_value(c8,32)
        return chain_hash

    def Add(self,chain):
        if self.Contains(chain):
            return False
        else:
            self.bloom_hash.add(self.hashed)
            return True 

    def Contains(self,chain):
        self.hashed = self.get_hash(chain)
        return self.hashed in self.bloom_hash  

    def Len(self):
        return len(self.bloom_hash)


import bitarray
from bitarray.util import ba2int
import hashlib 
import pickle
import struct
import sys


class Bloom():
    bloom_hash = set()
    hashed = ''
    BA_SIZE = 64
    EXPORT_FILE = 'saved_hash.dta'

    def __init__(self):
        print(sys.maxsize)
        try:
            with open (self.EXPORT_FILE, 'rb') as fp:
                itemlist = pickle.load(fp)
                # if itemlist:
                #     self.bloom_hash = itemlist
        except:
            pass


    def get_hash(self,chain):
        result = hashlib.md5(chain.encode('utf-8')) 
        ba = bitarray.bitarray()
        ba.frombytes(result.hexdigest().encode())
        
        i = ba2int(ba[:self.BA_SIZE])
        # print(i)
        return i

    def Add(self,chain):
        
        if self.Contains(chain):
            # print('---------------deja %s ' % chain)
            return False
        else:
            self.bloom_hash.add(self.hashed)
            # self.bloom_hash[self.hashed] = True
            return True 
        # print(self.bloom_hash)

    def Contains(self,chain):
        self.hashed = self.get_hash(chain)
        # print(' chain %s ------ HASH %s' % (chain,self.hashed))
        # return self.bloom_hash[self.hashed]  #
        return self.hashed in self.bloom_hash
    def Len(self):
        return len(self.bloom_hash)

    def Save(self):
        with open(self.EXPORT_FILE, 'wb') as fp:
                pickle.dump(self.bloom_hash, fp)

# b = Bloom()
# b.Add('coucou')
# b.Add('couco1u')
# b.Add('coucou3')
# b.Add('coucou')
# b.Add('coucoudd')

# b.Save()
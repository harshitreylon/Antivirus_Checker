import re, mmap, json


def ver_chk(name):
        for val in items:
                if name.lower() == val['name'].lower():
                        return val['version']

def ver_out(item, v):
        if (ver_chk(item) != None):
                print("The latest version is: ", ver_chk(item))
                old_ver = ver_chk(item)
                if old_ver == v:
                        print("You are on the latest version!\n\n")
                else:
                        print("An update is available. Kindly update!\n\n")
        else:
                print("The latest version is: NA\n\n")

def reset(name):
        pf = open(name, 'r')
        data = mmap.mmap(pf.fileno(), 0, access = mmap.ACCESS_READ)
        return data


jsondata = """[
 {
  "name":"Bitdefender Total Security",
  "version":"23.0.24.120"
 },
 {
  "name":"Kaspersky Total Security",
  "version":"21.1.15.500"
 },
 {
  "name":"Kaspersky Internet Security",
  "version":"21.2.16.590"
 },
 {
  "name":"Quick Heal AntiVirus Pro",
  "version":"19.00"
 },
 {
  "name":"AVG AntiVirus Free",
  "version":"21.3.6164.0"
 },
 {
  "name":"AVG Internet Security",
  "version":"21.3.6164.0"
 },
 {
  "name":"Bitdefender Internet Security",
  "version":"25.0.10.52"
 },
 {
  "name":"ESET Smart Security Premium",
  "version":"14.1.19.0"
 },
 {
  "name":"ESET Internet Security",
  "version":"14.1.19.0"
 },
 {
  "name":"Webroot SecureAnywhere Antivirus",
  "version":"9.0.30.75"
 },
 {
  "name":"Norton AntiVirus",
  "version":"22.20.5.39"
 },
 {
  "name":"F-Secure Antivirus",
  "version":"17.6"
 },
 {
  "name":"Avast Pro Antivirus",
  "version":"21.3.2459"
 },
 {
  "name":"Comodo Antivirus",
  "version":"12.2.2.7098"
 },
 {
  "name":"McAfee Total Protection",
  "version":"23.4"
 },
 {
  "name":"McAfee Security Scan Plus",
  "version":"3.11.2173.1"
 }
]"""

items = json.loads(jsondata)

wl = open('wordlist.txt', 'r')

match = False

c = 0


for lines in wl:
        for smallLine in lines.splitlines():
                data = reset('softLog.log')
                for li in data:
                        li1 = str(data.readline())
                        obj = re.compile(rf"\b((?<=Display Name:\s))\b\b{smallLine}(?:(?!\\r\\n).)*", re.I)
                        res = re.search(obj, li1)
                        obj1 = re.compile(r"\b((?<=Version:\s))\b(?:(?!\\r\\n).)*", re.I)
                        res1 = re.search(obj1, li1)
                        obj2 = re.compile(rf"\b((?<=Regkey:\s))\b\b{smallLine}(?:(?!\\r\\n).)*",re.I)
                        res2 = re.search(obj2, li1)
                        
                        if res:  
                                print("Found Display Name: {}".format(res.group(0)))
                                match = True
                                c+=1
                        elif match:
                                if res1: 
                                        print("Installed Version: {}".format(res1.group(0)))
                                        ver = res1.group(0)
                                        match = False
                                        ver_out(smallLine,ver)
                                
                        if res2: 
                                print("Found Regkey: {}".format(res2.group(0)))
                                ver_out(smallLine, None)
                                c+=1
                data.close()
wl.close()


if c == 0:
        print("Either you have not entered your preferred software in the wordlist and into the jsondata variable as well or you probably would only be having Windows Defender. Try to keep your Windows OS up-to-date.")

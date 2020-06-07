import time
host = "hosts"

host_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
website = ["facebook.com","www.facebook.com"]

while True:

	with open(host_path,'r+') as file:
		content = file.read()
		for w in website:
			if w in content:
				pass
			else:
				file.write(redirect+" "+ w +"\n")

				
	time.sleep(5)
	

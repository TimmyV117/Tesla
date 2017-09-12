import requests
import getpass

gtype = 'password'
clientid = 'e4a9949fcfa04068f59abb5a658f2bac0a3428e4652315490b659d5ab3f35a9e'
clientsecret = 'c75f14bbadc8bee3a7594412c31416f8300256d7668ea7e6e7f06727bfb9d220'
email = input('Enter Tesla owner username... ')
password = getpass.getpass('Enter Tesla owner password... ')


url='https://owner-api.teslamotors.com/oauth/token'
post_fields = {'grant_type':gtype, 'client_id':clientid, 'client_secret':clientsecret, 'email':email, 'password':password}

r = requests.post(url,post_fields)
print('REQUEST SUCCESSFUL')
print(r.text)
with open('./tesla_access_key.txt','w+') as f:
	f.write(r.text)
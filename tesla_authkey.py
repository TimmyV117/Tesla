# Tim Velasquez
# Code to generate Authentication token for Tesla API
# Written in syntax of Python 3.6
# Change in the sections for email and password at end of line 8 in [SQUARE BRACKETS]
# run the script in Python
# send me the response body when it is printed out in the terminal
# client_id_previous 9-6 81527cff06843c8634fdc09e8ac0abefb46ac849f38fe1e431c2ef2106796384
# client_secret_previous 9-6 c7257eb71a564034f9419ee651c7d0e5f7aa6bfbd18bafb5c5c033b093bb2fa3


from urllib import request

with request.urlopen('https://owner-api.teslamotors.com/oauth/token?grant_type=password&client_id=e4a9949fcfa04068f59abb5a658f2bac0a3428e4652315490b659d5ab3f35a9e&client_secret=c75f14bbadc8bee3a7594412c31416f8300256d7668ea7e6e7f06727bfb9d220&email=[ADD IN EMAIL ADDRESS AND GET RID OF THE BRACKETS]&password=[ADD IN PASSWORD AND GET RID OF THE BRACKETS]') as response:
	response_body = response.read()
	print(response_body)
	with open('./tesla_auth_response.txt') as file:
		file.write(str(response_body))
	print('Executed successfully! Access key is also located in tesla_auth_response.txt')


# Written to generate authentication token needed to access Tesla API
# Used to make calls to monitor various metrics + data collection during experimentation
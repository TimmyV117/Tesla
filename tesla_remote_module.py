import requests
import getpass
import ast
import json
import re
from operator import itemgetter

def get_access_token(email,password,*,silent=False,write=True):
	"""Gets access token using Tesla username + password. option arg silent true or false will turn off successful connectio notifications, write = true will write to a file"""
	gtype = 'password'
	clientid = 'e4a9949fcfa04068f59abb5a658f2bac0a3428e4652315490b659d5ab3f35a9e'
	clientsecret = 'c75f14bbadc8bee3a7594412c31416f8300256d7668ea7e6e7f06727bfb9d220'
	email=email
	password=password

	url='https://owner-api.teslamotors.com/oauth/token'
	post_fields = {'grant_type':gtype, 'client_id':clientid, 'client_secret':clientsecret, 'email':email, 'password':password}
	r = requests.post(url,post_fields)

	if write==True:
		with open('./tesla_access_key.txt','w+') as f:
			f.write(r.text)

	if silent==False:
		print('REQUEST SUCCESSFUL')

	access_dict = ast.literal_eval(r.text)
	return(access_dict)

def get_access_token2(silent=False,write=True):
	"""like the original but will prompt user for email and password"""
	gtype = 'password'
	clientid = 'e4a9949fcfa04068f59abb5a658f2bac0a3428e4652315490b659d5ab3f35a9e'
	clientsecret = 'c75f14bbadc8bee3a7594412c31416f8300256d7668ea7e6e7f06727bfb9d220'
	email=input('ENTER TESLA OWNER EMAIL... ')
	password=getpass.getpass('ENTER TESLA OWNER PASSWORD... ')

	url='https://owner-api.teslamotors.com/oauth/token'
	post_fields = {'grant_type':gtype, 'client_id':clientid, 'client_secret':clientsecret, 'email':email, 'password':password}
	r = requests.post(url,post_fields)

	if write==True:
		with open('./tesla_access_key.txt','w+') as f:
			f.write(r.text)

	if silent==False:
		print('REQUEST SUCCESSFUL')

	access_dict = ast.literal_eval(r.text)
	return(access_dict)

def list_vehicles(access_token, *, silent=False,write=True):
	"""Takes access token and lists all vehicles underneath it"""
	url = 'https://owner-api.teslamotors.com/api/1/vehicles'
	headers = {'Authorization':'Bearer ' + access_token}
	r = requests.get(url,headers=headers) #second arg needs to be headers and not params since we are doing authorization
	if write==True:
		with open('./tesla_vehicle_list.txt','w+') as f:
			f.write(r.text)

	if silent==False:
		print('CONNECTION SUCCESSFUL: LISTING ALL VEHICLES UNDER CREDENTIALS')
	conv_step1 = json.loads(r.text) #type: dictionary
	conv_step2 = conv_step1['response'] #type: string list
	ultimate_dictionary = conv_step2[0] #type: dictionary
	list_of_vehicles = ultimate_dictionary['id']
	print(str(list_of_vehicles))
	return(str(list_of_vehicles)) # work on getting the car id's here ---- got it! 9/13/17

def honk_horn(access_token, vehicle):
	"""honk horn once with one call. takes access token and vehicle key in dictionary from list_vehicles"""
	url = 'https://owner-api.teslamotors.com/api/1/vehicles/' + vehicle + '/command/honk_horn'
	headers = {'Authorization':'Bearer ' + access_token}
	r = requests.post(url,headers) #debug to see if you need headers=headers
	response_dict = ast.literal_eval(r.text)
	print('DO YOU HEAR THAT? ')
	return(response_dict['result'])

def battery_level(access_token, vehicle, silent=True):
	"""get charging state information. gives you a bunch more as fict if silent = False"""
	url = 'https://owner-api.teslamotors.com/api/1/vehicles/' + vehicle + '/data_request/charge_state'
	headers = {'Authorization':'Bearer ' + access_token}
	r = requests.get(url,headers=headers)
	conv_step1 = json.loads(r.text) #type: dictionary
	conv_step2 = conv_step1['response'] #type: dictionary
	ultimate_dictionary = conv_step2
	print('Useable Battery Level, Estimated Battery Range (mi)')
	battery_level_data = itemgetter('usable_battery_level','est_battery_range')(ultimate_dictionary)
	if silent==True:
		return(battery_level_data)
	elif silent==False:
		return(ultimate_dictionary)

def velocity(access_token, vehicle):
	"""gets speed of vehicle"""
	url = 'https://owner-api.teslamotors.com/api/1/vehicles/' + vehicle + '/data_request/drive_state'
	headers = {'Authorization':'Bearer ' + access_token}
	r = requests.get(url,headers=headers)
	conv_step1 = json.loads(r.text)
	conv_step2 = conv_step1['response']
	ultimate_dictionary = conv_step2
	velocity = ultimate_dictionary['speed']
	if velocity == None:
		return(0)
	else:
		return(velocity)

def location(access_token, vehicle):
	"""gets speed of vehicle"""
	url = 'https://owner-api.teslamotors.com/api/1/vehicles/' + vehicle + '/data_request/drive_state'
	headers = {'Authorization':'Bearer ' + access_token}	
	r = requests.get(url,headers=headers)
	conv_step1 = json.loads(r.text)
	conv_step2 = conv_step1['response']
	ultimate_dictionary = conv_step2
	print('lat, long')
	coordinates = itemgetter('latitude','longitude')(ultimate_dictionary)
	print(coordinates)
	return(coordinates)











#!/usr/bin/python
import requests
import sys
import configparser
import logging
import xml.etree.ElementTree as ET

# Returns the API key
def get_key():
	return config.get('Params', 'apikey')

# Returns the Alma API base URL
def get_base_url():
	return config.get('Params', 'baseurl')
	
# returns user get/put API URL	
def get_user_url(id):
	url = get_base_url() + '/almaws/v1/users/' + id + '?apikey=' + get_key();
	return url
	

# Calls the individual user API
def get_user_record(id):
	# do some checks on ID
	user_url = get_user_url(id)
	response = requests.get(user_url)
	if response.status_code == 200:
		xml = ET.fromstring(response.content)
		parse_user(xml,id)
	else:
		print ('failed to get user: ' + user_url)
	
# Iterates to user ID field and changes segment_type to Internal	
def parse_user(xml,userid):
	switch = False
	record_type = xml.find('record_type')
	record_type.text = 'STAFF'
	put_user(xml,userid)
			
# Makes a put request to user API with updated ID fields to internal fields
def put_user(xml,id):
	headers = {"Content-Type": "application/xml"}
	print (id)
	user_url = get_user_url(id)
	r = requests.put(user_url,data=ET.tostring(xml),headers=headers)
	print (r.content)
		
	
def read_users(user_file):
	f  = open(user_file,'rt')
	try:
		reader = csv.reader(f)
		header = next(reader) # skip header row
		for row in reader:
			print (row[0])
			get_user_record(row[0])
	finally:
		f.close()
	
	
# parsing configuration file for API information, number of users and the ID type that we are switching to an internal ID type. 	
config = configparser.ConfigParser()
config.read(sys.argv[1]) #reads in parameter file
apikey = config.get('Params', 'apikey')
baseurl = config.get('Params','baseurl')

user_file = sys.argv[2]
read_users(user_file)
		
	
	
	
	
	
	
	
	
	
	
	
	
	

#!/usr/bin/python

import pygeoip
def location_finder(ip):
	ip_adr = pygeoip.GeoIP('/home/socialengineer100/Desktop/GeoLiteCity.dat')                                      #Enter full path to GeoLiteCity.dat
																						
																					  
																		
	loc = ip_adr.record_by_addr(ip)
	for key,value in loc.items():
		print("{} : {} ".format(key,value))


print("Welcome to Geo location finder")
input_user =  raw_input("Enter ip address: ")
location_finder(input_user)

#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import requests


class QueryObject(object):
	"""Dates and hour in format dd.mm.yy, hh:mm"""
	def __init__(self, from_name, to_name, date, hour):
		self.from_name = from_name
		self.to_name = to_name
		self.date = date
		self.hour = hour


	def get_coordinates(self, address):
		parameters = {'address': address, 'sensor': 'false'}
		google_coord = "http://maps.googleapis.com/maps/api/geocode/json"
		response = requests.get(google_coord, params=parameters)
		answer = response.json()
		coord = answer['results'][0]['geometry']['location']
		return str(coord["lat"]) + ":" + str(coord["lng"])


	def query_url(self):
		from_coord = self.get_coordinates(self.from_name)
		to_coord = self.get_coordinates(self.to_name)
		return "http://krakow.jakdojade.pl/index.html?d=" + self.date +\
		"&h=" + self.hour + "&fn=" + from_coord + "&tn=" + to_coord
		
from_name = "TAURON Arena Kraków Al. Pokoju"
to_name = "Stradom"
date = "05.02.17"
hour = "11:24"
qo = QueryObject(from_name, to_name, date, hour)

print qo.query_url()

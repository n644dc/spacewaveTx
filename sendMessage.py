#!/usr/bin/python

from rflib import *

params = []

try:
    with open("params.txt") as f:
        content = f.readlines()
    params = [x.strip() for x in content]
except Exception as e:
    print(e)
    print("A parameters file is necessary.")
    quit()
	
if len(params) < 4:
	print("missing params")
	quit()

config = {}

try:
	for param in params:
		if not '=' in param:
			raise Exception("paramName=paramValue is the format")
		keyValParam = param.split('=')
		if len(keyValParam) < 2:
			raise Exception("paramName=paramValue is the format")
		config[keyValParam[0]] = keyValParam[1]
	print(config)		
except Exception as e:
	print(e)
	print("malformed param")
	quit()


try:
	d = RfCat() 
	d.setFreq(int(config['freq'])) 
	d.setMdmModulation(MOD_2FSK) 
	d.makePktFLEN(int(config['packetSize'])) 
	d.setMdmDRate(int(config['baudRate']))
	d.calculateMdmDeviatn()
	d.calculatePktChanBW() 
	d.setMaxPower()
	d.printRadioConfig()
	d.setModeIDLE()
except Exception as e:
	print(e)
	quit()

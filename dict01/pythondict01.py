#!/usr/bin/env python3

## create a dictionary
switch = {"hostname": "sw1", "ip": "10.0.1.1", "version": "1.2", "vendor": "cisco"}

## display parts of the dictionary
print( switch["hostname"] )
print( switch["ip"] )

## request a 'fake' key
print( switch["ip"] )  



print(switch.get("lynx"))


print(switch.keys())

print(switch.values())

switch["adminlogin"]="karlo04"

switch["password"]="qwerty"

print(switch.keys())
print(switch.values())



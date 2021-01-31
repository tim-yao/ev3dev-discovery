#!/usr/bin/env python3

import requests
import time
from ev3dev2.sound import Sound

spkr = Sound()
spkr.speak('Request is start!')

resp = requests.get('https://api.ipify.org/?format=json')

spkr.speak('Request is end!')
ip = resp.json()["ip"]

spkr.speak('IP address is {}'.format(resp.json()["ip"]))
print('IP: {}'.format(resp.json()["ip"]))

time.sleep(5)

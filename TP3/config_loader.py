import json

f = open('config.json')
config = json.load(f)
v = config['max_speed']
n = config['quantity']
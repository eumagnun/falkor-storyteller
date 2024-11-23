
import json

def load_world(filename):
    with open(filename, 'r') as f:
        return json.load(f)
    


########################################################
#  Database File
########################################################

import requests
import json
import os

#  Definitions
dev = (os.environ['USER'] == 'michael')

base_url_prod = 'http://to_be_determined'
base_url_dev = 'http://localhost:5000/api'
base_url = base_url_dev if dev else base_url_prod

get_inc_url = base_url + '/getIncData/%d'
fetch_inc_url = base_url + '/fetchIncData/'
update_inc_url = base_url +  '/updateIncData/'
fetch_targets_url = base_url +  '/fetchTargets/'
update_targets_url = base_url + '/updateTarget/'

########################################################
#  Helper Functions
########################################################

def send_api_req(url, val=None):
    ## POST\
    if val:
        r = requests.post(url, json=val)
    ## GET
    else:
        r = requests.get(url)
    print r.url
    return r.json()

########################################################
#  Database Class
########################################################

class DB:
    def get_inc_data(self, inc):
        return send_api_req((get_inc_url % inc))
    def get_all_inc_data(self):
        return send_api_req(fetch_inc_url)
    def add_inc_data(self, inc, humidity):
        ## Expects a json object with incNum and humidity
        return send_api_req(update_inc_url, {'incNum': inc,'humidity': humidity})
    def get_targets(self, inc):
        return send_api_req(fetch_targets_url, humidity)
    def update_target(self, inc, target):
        ## Expects a json object with incNum and target
        data = {'incNum': inc, 'target': target}
        return send_api_req(update_targets_url, data)

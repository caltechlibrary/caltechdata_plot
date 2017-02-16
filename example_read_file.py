# myapp.py

import urllib.request
import urllib.parse
import urllib.error
import ssl
import json
import pandas

#CaltechDATA Info
api_url = "https://caltechdata.tind.io/api/records/"

req = urllib.request.Request(api_url)
s = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
response = urllib.request.urlopen(req,context=s)
data = json.JSONDecoder().decode(response.read().decode('UTF-8'))
#This is reading in all recent data files - 
#Terrible workaround because /api/record isn't available

for f in data['hits']['hits']:
    print(f['id'])
    
    if f['id']==208: #Replace
            url = f['metadata']['electronic_location_and_access'][0]['uniform_resource_identifier']
            #Terrible, only looks at first file
            rawdata = pandas.read_csv(url,sep = ',',header=1) 
            print(rawdata[0])
            print(rawdata[1])
            #print(response.read())
            #fu = list(rawdata)
            #print(fu)
            #for fow in rawdata:
            #    print(fow)

# myapp.py

import urllib.request
import urllib.parse
import urllib.error
import ssl
import json,pandas

from bokeh.layouts import column
from bokeh.models import Button
from bokeh.models import ColumnDataSource
from bokeh.models.widgets.inputs import TextInput
from bokeh.palettes import RdYlBu3
from bokeh.plotting import figure, curdoc

# create a plot and style its properties
p = figure(x_range=(0, 1200), y_range=(0, 2))
p.border_fill_color = 'white'
p.background_fill_color = 'white'
p.height = 500
p.outline_line_color = None
p.grid.grid_line_color = None

source = ColumnDataSource(data=dict(x=[], y=[]))
p.circle(x="x",y="y", source=source,size=7, color='blue')
p.title.text = "Plot spectra from CaltechDATA"
p.title.align="center"

# create a callback that will add a number in a random location
def callback():

    #CaltechDATA Info
    api_url = "https://data.caltech.edu/api/record/"

    # BEST PRACTICE --- update .data in one step with a new dict
    new_data = dict()
    
    #Should have validation that input from form is valid
    api_url = api_url + txt.value

    req = urllib.request.Request(api_url)
    s = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
    response = urllib.request.urlopen(req,context=s)
    data = json.JSONDecoder().decode(response.read().decode('UTF-8'))

    erecord = data['metadata']['electronic_location_and_access'][0]
    #Only looks at first file, no validation
    url = erecord['uniform_resource_identifier']

    rawframe = pandas.read_csv(url,sep= ',',header=1) 
    new_data = dict(x=rawframe.index.values,\
            y=rawframe[list(rawframe)[0]])

    p.title.text=erecord['electronic_name'][0]
    #Reads only first column, hard coding

    source.data = new_data

# add a button widget and configure with the call back
txt = TextInput(placeholder="Type 208 or 209")
button = Button(label="Press Me")
button.on_click(callback)

# put the button and plot in a layout and add to the document
column = column(p,txt,button)
curdoc().add_root(column)

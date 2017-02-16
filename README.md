# caltechdata_plot

caltechdata_plot is a demo interactive plotting tool that uses Bokeh server 
to produce an interactive plot by calling the caltechDATA (Invenio 3) API

In development.  This is a minimal working example that ONLY works
with mineral spectra records 208 and 209.  May also break when
new records are added.

## Setup

- Install the Anaconda python distribution
- Install Bokeh by typing 'conda install bokeh'
- bokeh serve --show plot.py 

## Usage

```shell
   python caltechdata_read.py [-h]
```

optional arguments:
  -h, --help  show this help message and exit


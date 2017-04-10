# caltechdata_plot

[![DOI](https://data.caltech.edu/badge/83457930.svg)](http://data.caltech.edu/badge/latestdoi/83457930)
    
caltechdata_plot is a demo interactive plotting tool that uses Bokeh server 
to produce an interactive plot by calling the caltechDATA (Invenio 3) API

This is example is not general and only works with mineral spectra records 208 and 209.

## Setup

- Install the Anaconda python distribution
- Install Bokeh by typing 'conda install bokeh'
- bokeh serve --show plot.py 

### AWS Setup

Instructions for setting up an AWS server that will show plots

- Create a new AWS EC2 instance using one of the Anaconda community images.
You can find the listing of these image names on the Anaconda web site.
You could also install anaconda manually.
- Install Bokeh by typing 'conda install bokeh'
- Install nginx by typing 'sudo apt-get install nginx'
- Remove default and add configuration at 
  '/etc/nginx/sites-enabled/plot'

```shell
server {
    listen 80 default_server;
    server_name plots.caltechlibrary.org;

    access_log  /tmp/bokeh.access.log;
    error_log   /tmp/bokeh.error.log debug;

    location / {
        proxy_pass http://127.0.0.1:5006;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_http_version 1.1;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Host $host:$server_port;
        proxy_buffering off;
    }

}
```

- Restart web server with 'sudo service nginx restart'
- Add this configuration to /etc/init/plot.conf

```shell
# Start bokeh plot

start on stopped rc RUNLEVEL=[2345]
stop on runlevel [!2345]

respawn

script
cd /home/ubuntu/caltechdata_plot/
sudo -u ubuntu /home/ubuntu/anaconda3/bin/bokeh serve plot.py --host plots.caltechlibrary.org > bokeh.log
end script
```

- Reload by typing 'sudo initctl reload-configuration'
- You can start up bokeh with 'sudo initctl start plot'

## Usage

```shell
   python caltechdata_read.py [-h]
```

optional arguments:
  -h, --help  show this help message and exit


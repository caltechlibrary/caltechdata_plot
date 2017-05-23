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

Instructions for setting up an AWS server that will show plots.  This configuration has been tested on Ubuntu 16.04.

- Install Anaconda by downloading the installer below and following the prompts (you can update the links for new versions).

```shell
curl https://repo.continuum.io/archive/Anaconda3-4.3.1-Linux-x86_64.sh > Anaconda3-4.3.1-Linux-x86_64.sh
bash Anaconda3-4.3.1-Linux-x86_64.sh 
```

(You can also use a preconfigured AWS Anaconda community images, but this limits your choice of servers)

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
- Add this configuration to /etc/systemd/system/plot.service

```shell
[Unit]
Description=Bokeh Plot
After=syslog.target network.target remote-fs.target nss-lookup.target

[Service]
Type=simple
WorkingDirectory=/home/ubuntu/caltechdata_plot/
ExecStart=/home/ubuntu/anaconda3/bin/bokeh serve plot.py --allow-websocket-origin plots.caltechlibrary.org
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

- Reload by typing 'sudo systemctl daemon-reload'
- You can start up bokeh with 'sudo systemctl start plot'
- Start the plotting server on reboot with 'sudo systemctl enable plot'

## Command Line Usage

```shell
   python caltechdata_read.py [-h]
```

optional arguments:
  -h, --help  show this help message and exit


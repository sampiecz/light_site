# Kasa light bulb web interface 

## Description 

To allow other people in my home to control our smart lights I created an web frontend that is hosted on a raspberry pi.

## Features

1.) Can turn bulbs on / off

2.) Can change bulbs color

## Deploy

docker build -t light_site . && docker run --network host light_site

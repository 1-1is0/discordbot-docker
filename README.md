# Python Discord Bot

## Description

A simple discord bot that can be run with docker.
This is a personal project and I'm just testing new things. :wink:

## Installation

### Without docker

Without docker you'll need to install the requirements and run the project.  

Make sure you have the token in your env var.

```bash
pip install -r requirements.txt
python main.py
```

### Docker

For building the image  
`docker build -f Dockerfile -t discord-bot .`

it's important to have bot token as env var, so when you want to run the image
you can do  
`docker run -env_file=env_file --name discord-bot discord-bot`.  
so the token will be available to the application.
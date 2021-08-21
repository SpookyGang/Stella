FROM python:3.9.1

WORKDIR /rikudo

RUN chmod 777 /rikudo

#sorry for noob dockerfile


RUN sudo apt-get update
RUN sudo apt install upgrade 
ENV PIP_NO_CACHE_DIR 1

RUN sed -i.bak 's/us-west-2\.ec2\.//' /etc/apt/sources.list

# Installing Required Packages
RUN apt update && apt upgrade -y && \
    apt install --no-install-recommends -y \
    python3-pip \
    python3-requests \
    python3-tz \
    python3-aiohttp \
    curl \
    figlet \
    git \
    bash \
    && rm -rf /var/lib/apt/lists /var/cache/apt/archives /tmp

# Pypi package Repo upgrade
RUN pip3 install --upgrade pip setuptools
RUN sudo apt install python3-pip
RUN pip3 install --no-cache-dir -U -r requirements.txt

#fuck I'm noob in docker 

CMD ["python3", "-m", "Stella"]

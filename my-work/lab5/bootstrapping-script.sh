#!/bin/bash

/usr/bin/apt update -y
/usr/bin/apt upgrade -y
/usr/bin/apt install -y git jq nginx python3 python3-pip
python3 -m pip install boto3

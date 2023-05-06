#!/bin/bash

cd /opt/QR-Code-Generator

python3 -m venv venv
source venv/bin/activate

# install requirements in venv
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade pyqrcode
python3 -m pip install --upgrade pypng

# run the script
python3 /opt/QR-Code-Generator/src/main.py

sleep 1m

deactivate

rm -r venv

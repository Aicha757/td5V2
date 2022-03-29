#!/bin/bash
pip3 install virtualenv --force-reinstall
python3 -m venv .env
source .env/bin/activate
pip install -r requirements.txt
python3 book.py
python3 main.py

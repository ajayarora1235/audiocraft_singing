#!/bin/bash

sudo apt-get update
yes Y | sudo apt install libasound2-dev portaudio19-dev libportaudio2 libportaudiocpp0 ffmpeg
yes Y | sudo apt-get install zip gzip tar libsox-dev
pip install -e .
cd dataset/songsinger
python3 -m new_data_getter
unzip full_dataset.zip -d .
cd ../..
python3 dataset/songsinger/data_checker.py

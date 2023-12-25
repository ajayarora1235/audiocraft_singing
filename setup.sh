#!/bin/bash

pip install -e .
pip install boto3 wandb pydub
pip install "git+https://github.com/CPJKU/madmom.git"
sudo apt-get update
sudo apt install libasound2-dev portaudio19-dev libportaudio2 libportaudiocpp0 ffmpeg
pip install PyAudio BeatNet
wandb init
sudo apt-get install zip gzip tar libsox-dev
conda install -c conda-forge sox
cd dataset/songsinger
python3 -m new_data_getter
unzip full_dataset.zip -d .
python3 -m directory_renamer
cd ../..
python3  dataset/songsinger/data_checker.py

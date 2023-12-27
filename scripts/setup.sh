#!/bin/bash

pip install -e .
pip install boto3 wandb pydub
sudo apt-get update
yes Y | sudo apt-get install zip gzip tar ffmpeg libsox-dev
cd dataset/songsinger
python3 -m new_data_getter
unzip full_dataset.zip -d .
cd ../..
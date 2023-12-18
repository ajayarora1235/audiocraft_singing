import json
import os

def check_files_exist():
    files = ['train.jsonl', 'valid.jsonl', 'test.jsonl']
    suffixes = ("_vo.mp3", "_dv.mp3", "_do.mp3", "_o.mp3", "_d.mp3", "_v.mp3", "_dvo.mp3")

    for file in files:
        with open(file, 'r') as f:
            for line in f:
                data = json.loads(line)
                path = data['path']

                # Check if file exists
                if not os.path.exists(path):
                    print(f"File does not exist: {path}")
                    continue

                # Check if path ends with one of the suffixes
                if not path.endswith(suffixes):
                    print(f"Invalid suffix for file: {path}")
                    continue

                # Generating instrumental path
                for suffix in suffixes:
                    if path.endswith(suffix):
                        instrumental_path = path[:-len(suffix)] + "_b.mp3"
                        break

                # Check if instrumental file exists
                if not os.path.exists(instrumental_path):
                    print(f"Instrumental file does not exist: {instrumental_path}")

check_files_exist()
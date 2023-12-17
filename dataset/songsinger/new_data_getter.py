import boto3
import glob
import os
# from collections import defaultdict

session = boto3.session.Session()
bucket_name, account_id, access_key, secret_key = "songsinger", "813a83e83bed7fcce27f64c0c4880a7a", "574a0223a9d026b58c0c2ec07909bc2b", "c2e35e9203b4379edf4e1e65eb4e7681022015175b07aa09d7b77fd657c3d6db"
s3_client = session.client('s3',
                            aws_access_key_id=access_key,
                            aws_secret_access_key=secret_key,
                            endpoint_url=f"https://{account_id}.r2.cloudflarestorage.com")

directory = 'musicgen_bass/'  # Replace with the directory name

s3_client.download_file(bucket_name, 'musicgen_bass/full_dataset.zip', 'full_dataset.zip')
s3_client.download_file(bucket_name, 'musicgen_bass/train_bass_final.jsonl', 'train.jsonl')
s3_client.download_file(bucket_name, 'musicgen_bass/valid_bass_final.jsonl', 'valid.jsonl')
s3_client.download_file(bucket_name, 'musicgen_bass/test_bass_final.jsonl', 'test.jsonl')
s3_client.download_file(bucket_name, 'musicgen_bass/audio_metadata_norm_fin.zip', 'audio_metadata_norm.zip')

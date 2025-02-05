import boto3
import glob
import os

session = boto3.session.Session()
bucket_name, account_id, access_key, secret_key = "songsinger", "813a83e83bed7fcce27f64c0c4880a7a", "574a0223a9d026b58c0c2ec07909bc2b", "c2e35e9203b4379edf4e1e65eb4e7681022015175b07aa09d7b77fd657c3d6db"
s3_client = session.client('s3',
                            aws_access_key_id=access_key,
                            aws_secret_access_key=secret_key,
                            endpoint_url=f"https://{account_id}.r2.cloudflarestorage.com")

directory = 'musicgen_bass/'  # Replace with the directory name

# Specify the local directory where files will be downloaded
local_directory = './'  # Current directory

# List objects in the S3 directory
paginator = s3_client.get_paginator('list_objects_v2')
pages = paginator.paginate(Bucket=bucket_name, Prefix=directory)

page_num = 0
item_num = 0
dataset_list = []
for page in pages:
    item_num = 0
    page_num += 1
    print(page_num)

    # Download each file from S3 to the local directory
    for obj in page.get('Contents', []):
        item_num += 1
        if page_num == 25 and item_num > 834: 
            key = obj['Key']
            if key[-4:] != "json":
                local_file_path = os.path.join(local_directory, os.path.basename(key))
                if not os.path.isfile(local_file_path):
                    s3_client.download_file(bucket_name, key, local_file_path)
                    print(f"Downloaded: {key} to {local_file_path}")
            else:
                local_file_path = os.path.join('./audio_metadata/', os.path.basename(key))
                if not os.path.isfile(local_file_path):
                    s3_client.download_file(bucket_name, key, local_file_path)
                    print(f"Downloaded: {key} to {local_file_path}")

print("All files downloaded successfully.")

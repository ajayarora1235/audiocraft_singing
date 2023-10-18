import boto3
import glob
import os

session = boto3.session.Session()
bucket_name, account_id, access_key, secret_key = "songsinger", "813a83e83bed7fcce27f64c0c4880a7a", "574a0223a9d026b58c0c2ec07909bc2b", "c2e35e9203b4379edf4e1e65eb4e7681022015175b07aa09d7b77fd657c3d6db"
s3_client = session.client('s3',
                            aws_access_key_id=access_key,
                            aws_secret_access_key=secret_key,
                            endpoint_url=f"https://{account_id}.r2.cloudflarestorage.com")

directory = 'musicgen/'  # Replace with the directory name

# Specify the local directory where files will be downloaded
local_directory = './'  # Current directory

# List objects in the S3 directory
objects = s3_client.list_objects_v2(Bucket=bucket_name, Prefix=directory)

# Download each file from S3 to the local directory
for obj in objects.get('Contents', []):
    key = obj['Key']
    local_file_path = os.path.join(local_directory, os.path.basename(key))
    s3_client.download_file(bucket_name, key, local_file_path)
    print(f"Downloaded: {key} to {local_file_path}")

print("All files downloaded successfully.")
# upload_public.py
import boto3

s3 = boto3.client('s3', region_name="us-east-1")

with open("local_image.png", 'rb') as f:
    s3.put_object(
        Body=f,
        Bucket="ds2002-qgt8xq",
        Key="public_image.png",
        ACL="public-read"
    )

print("Uploaded public file to S3.")

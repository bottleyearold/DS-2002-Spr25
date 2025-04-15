# upload_private.py
import boto3

s3 = boto3.client('s3', region_name="us-east-1")

with open("local_image.png", 'rb') as f:
    s3.put_object(
        Body=f,
        Bucket="ds2002-qgt8xq",
        Key="local_image.png"
    )

print("Uploaded private file to S3.")

import boto3
from datetime import datetime, timezone, timedelta

def lambda_handler(event, context):
    bucket = 'lambda-cleanup-bucket-a5'
    s3 = boto3.client('s3')
    objs = s3.list_objects_v2(Bucket=bucket).get('Contents', [])
    
    for obj in objs:
        age = datetime.now(timezone.utc) - obj['LastModified']
        if age.days > 30:
            s3.delete_object(Bucket=bucket, Key=obj['Key'])
            print(f"Deleted: {obj['Key']}")


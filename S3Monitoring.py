import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    unencrypted_buckets = []

    try:
        # List all S3 buckets in the account
        response = s3.list_buckets()
        buckets = response['Buckets']

        print("🔍 Checking encryption for all S3 buckets...\n")

        for bucket in buckets:
            bucket_name = bucket['Name']
            print(f"🪣 Bucket: {bucket_name}")

            try:
                encryption = s3.get_bucket_encryption(Bucket=bucket_name)
                rules = encryption['ServerSideEncryptionConfiguration']['Rules']
                print(f"✅ {bucket_name} is encrypted with: {rules[0]['ApplyServerSideEncryptionByDefault']['SSEAlgorithm']}\n")
            except s3.exceptions.ClientError as e:
                error_code = e.response['Error']['Code']

                if error_code == 'ServerSideEncryptionConfigurationNotFoundError':
                    print(f"❌ {bucket_name} is NOT encrypted!\n")
                    unencrypted_buckets.append(bucket_name)
                else:
                    print(f"⚠️ Error checking {bucket_name}: {e}\n")

        # Summary
        print("🧾 Summary of Unencrypted Buckets:")
        if unencrypted_buckets:
            for b in unencrypted_buckets:
                print(f"🔴 {b}")
        else:
            print("🎉 All buckets are encrypted.")

    except Exception as e:
        print(f"🚨 Lambda failed due to unexpected error: {str(e)}")

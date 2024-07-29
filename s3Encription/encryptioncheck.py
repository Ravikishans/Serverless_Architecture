import boto3
from botocore.exceptions import ClientError


def lambda_handler(event, context):


    def check_bucket_encryption():
        s3 = boto3.client('s3')
    
        try:
            response = s3.list_buckets()
        except ClientError as e:
            print(f"Failed to list buckets. Error: {e}")
            return
    
        for bucket in response['Buckets']:
            bucket_name = bucket['Name']
            try:
                enc = s3.get_bucket_encryption(Bucket=bucket_name)
                rules = enc['ServerSideEncryptionConfiguration']['Rules']
                print(f"Bucket: {bucket_name}, Encryption: {rules}")
            except ClientError as e:
                error_code = e.response['Error']['Code']
                if error_code == 'ServerSideEncryptionConfigurationNotFoundError':
                    print(f"Bucket: {bucket_name}, no server-side encryption")
                else:
                    print(f"Bucket: {bucket_name}, unexpected error: {e}")

    check_bucket_encryption()
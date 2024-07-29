## Prerequisites

- AWS Account
- IAM permissions to create roles and policies
- Basic understanding of AWS S3 and Lambda

## Steps

### 1. S3 Setup

1. Navigate to the S3 dashboard in the AWS Management Console.
2. Create a few S3 buckets.

### 2. Create Lambda IAM Role

1. Navigate to the IAM dashboard.
2. Create a new role for Lambda:
   - Go to **Roles** and click **Create role**.
   - Select **Lambda** as the trusted entity.
   - Click **Next: Permissions**.
3. Attach the `AmazonS3ReadOnlyAccess` policy to this role:
   - Search for `AmazonS3ReadOnlyAccess`.
   - Select it and proceed.
4. Name the role (e.g., `LambdaS3ReadOnlyRole`) and create it.

### 3. Create Lambda Function

1. Navigate to the Lambda dashboard.
2. Click **Create function**.
3. Configure the function:
   - **Name**: `S3EncryptionChecker`
   - **Runtime**: `Python 3.x`
   - **Role**: Use an existing role
   - **Existing role**: Select the `LambdaS3ReadOnlyRole` created earlier.
4. Click **Create function**.

### 4. Write the Lambda Function Code

1. Write the code which is given in "encryptioncheck.py".
2. Deploy the code and test it.
3. The output should be like 
Bucket: rakshi2107, Encryption: [{'ApplyServerSideEncryptionByDefault': {'SSEAlgorithm': 'AES256'}, 'BucketKeyEnabled': True}]
Bucket: rakshi2508, Encryption: [{'ApplyServerSideEncryptionByDefault': {'SSEAlgorithm': 'AES256'}, 'BucketKeyEnabled': False}] 
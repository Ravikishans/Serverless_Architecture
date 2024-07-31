# DynamoDB Item Change Alert Using AWS Lambda, Boto3, and SNS

This project automates the process of receiving alerts whenever an item in a DynamoDB table is updated. It uses AWS Lambda, Boto3, and SNS to send notifications.

## Objective

Automate the process to receive an alert whenever an item in a DynamoDB table gets updated.

## Components

1. **DynamoDB Table**: Stores the items to be monitored.
2. **SNS Topic**: Sends notifications when items are updated.
3. **Lambda Function**: Processes DynamoDB stream events and sends SNS notifications.
4. **IAM Role**: Grants the necessary permissions for the Lambda function.

## Steps to Setup

### 1. DynamoDB Setup

1. **Navigate to the DynamoDB dashboard**:
   - Go to the AWS Management Console and open the DynamoDB service.

2. **Create a new table**:
   - Click on "Create table".
   - Enter a table name (e.g., `Assignment7`).
   - Define a primary key (e.g., `Name` with type string).
   - Click "Create" to finish the setup.

3. **Add items to the table**:
   - Select your table and click on the "Action" tab.
   - Click on "Create item" and add a few items with the primary key and other attributes.

### 2. SNS Setup

1. **Navigate to the SNS dashboard**:
   - Go to the AWS Management Console and open the SNS service.

2. **Create a new topic**:
   - Click on "Create topic".
   - Choose "Standard" and enter a topic name (e.g., `DynamoDB_alert`).
   - Click "Create topic".

3. **Subscribe your email to the topic**:
   - Select the topic you created.
   - Click on "Create subscription".
   - Set "Protocol" to "Email" and enter your email address.
   - Click "Create subscription".
   - Check your email and confirm the subscription.

### 3. Lambda IAM Role

1. **Create a new IAM role for Lambda**:
   - Go to the AWS Management Console and open the IAM service.
   - Click on "Roles" and then "Create role".
   - Choose "Lambda" as the trusted entity and click "Next: Permissions".

2. **Attach policies**:
   - Attach the following policies:
     - `AWSLambdaDynamoDBExecutionRole`
     - `AmazonSNSFullAccess`
   - Click "Next: Tags" and then "Next: Review".
   - Enter a role name (e.g., `LambdaDynamoDBSNSRole`) and click "Create role".

### 4. Lambda Function

1. **Navigate to the Lambda dashboard**:
   - Go to the AWS Management Console and open the Lambda service.

2. **Create a new function**:
   - Click on "Create function".
   - Choose "Author from scratch".
   - Enter a function name (e.g., `DynamoDB_alert`).
   - Choose **Python 3.x** as the runtime.
   - Under "Permissions", choose "Use an existing role" and select the role you created earlier.

3. **Write the Boto3 Python script**.
   - copy and paste "change.py"
   - depoly and test the code


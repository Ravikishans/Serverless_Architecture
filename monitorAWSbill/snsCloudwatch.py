import json
import boto3
from botocore.exceptions import ClientError
from datetime import datetime, timedelta
import pytz

# Initialize boto3 clients for CloudWatch and SNS
cloudwatch = boto3.client('cloudwatch')
sns = boto3.client('sns')

# Define the threshold and SNS topic ARN
threshold = 5.0  # Threshold in USD
sns_topic_arn = 'arn:aws:sns:ap-south-1:891376926844:awsBilling'

def lambda_handler(event, context):
    # Get the current time and the time 24 hours ago, in UTC
    utc_zone = pytz.utc
    end_time = datetime.now(utc_zone)
    start_time = end_time - timedelta(days=1)

    try:
        # Retrieve the AWS billing metric from CloudWatch
        response = cloudwatch.get_metric_statistics(
            Namespace='AWS/Billing',
            MetricName='EstimatedCharges',
            Dimensions=[
                {
                    'Name': 'Currency',
                    'Value': 'USD'
                }
            ],
            StartTime=start_time,
            EndTime=end_time,
            Period=86400,
            Statistics=['Maximum']
        )

        # Extract the maximum billing amount from the response
        if response['Datapoints']:
            max_billing_amount = response['Datapoints'][0]['Maximum']
        else:
            max_billing_amount = 0.0

        # Print the retrieved billing amount for logging purposes
        print(f"Billing amount for the last 24 hours: ${max_billing_amount}")

        # Compare the billing amount with the threshold
        if max_billing_amount > threshold:
            # Send an SNS notification
            message = f"Alert: Your AWS billing has exceeded the threshold of ${threshold}. Current billing amount is ${max_billing_amount}."
            sns.publish(
                TopicArn=sns_topic_arn,
                Message=message,
                Subject='AWS Billing Alert'
            )
            print("SNS notification sent.")
        else:
            print("Billing is within the threshold.")

    except ClientError as e:
        # Handle the exception and print the error message
        print(f"ClientError: {e}")
    
    return {
        'statusCode': 200,
        'body': json.dumps('Function executed successfully!')
    }

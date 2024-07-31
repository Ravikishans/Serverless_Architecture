import json
import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

sns_client = boto3.client('sns')
topic_arn = 'arn:aws:sns:ap-south-1:891376926844:DynamoDB_alert'  # replace with your SNS topic ARN

def lambda_handler(event, context):
    try:
        # Extract the modified DynamoDB item from the event
        for record in event['Records']:
            if record['eventName'] == 'MODIFY':
                modified_item = record['dynamodb']['NewImage']
                item_details = json.dumps(modified_item, default=str)
                
                # Send an SNS notification
                response = sns_client.publish(
                    TopicArn=topic_arn,
                    Message=f'Item modified: {item_details}',
                    Subject='DynamoDB Item Modified'
                )
                
                logger.info(f'SNS publish response: {response}')
            else:
                logger.info('No modifications detected in the event.')

    except Exception as e:
        logger.error(f'Error processing DynamoDB stream: {str(e)}')
        raise e

    logger.info('Lambda function execution completed successfully')
    return {
        'statusCode': 200,
        'body': json.dumps('Lambda executed successfully')
    }

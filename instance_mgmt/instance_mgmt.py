import boto3
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')

    try:
        # Describe instances with Auto-Stop tag
        stop_instances = ec2.describe_instances(
            Filters=[
                {'Name': 'tag:Action', 'Values': ['Auto-Stop']}
            ]
        )
        
        stop_instance_ids = [
            instance['InstanceId']
            for reservation in stop_instances['Reservations']
            for instance in reservation['Instances']
        ]

        # Stop the instances
        if stop_instance_ids:
            ec2.stop_instances(InstanceIds=stop_instance_ids)
            logger.info(f"Stopped instances: {stop_instance_ids}")
        else:
            logger.info("No instances to stop")

        # Describe instances with Auto-Start tag
        start_instances = ec2.describe_instances(
            Filters=[
                {'Name': 'tag:Action', 'Values': ['Auto-Start']}
            ]
        )
        
        start_instance_ids = [
            instance['InstanceId']
            for reservation in start_instances['Reservations']
            for instance in reservation['Instances']
        ]

        # Start the instances
        if start_instance_ids:
            ec2.start_instances(InstanceIds=start_instance_ids)
            logger.info(f"Started instances: {start_instance_ids}")
        else:
            logger.info("No instances to start")
    
    except Exception as e:
        logger.error(f"Error in managing EC2 instances: {e}")

    return {
        'statusCode': 200,
        'body': 'EC2 instances started/stopped as per tags'
    }

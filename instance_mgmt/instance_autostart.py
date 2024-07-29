import boto3
import json
import time

def launch_ec2_instance(config):

    ec2 = boto3.resource('ec2', region_name=config['region'])
    ec2 = boto3.client('ec2', region_name=config['region'])
    security_group_response = ec2.create_security_group(
        GroupName='default1',
        Description='Security group for instance'
    )
    security_group_id = security_group_response['GroupId']
    print(f"Security Group '{security_group_id}'.")

    # Allow inbound traffic on port 80 (HTTP) and 22 (SSH)
    
    # Define rules
    ingress_rules = [
        {
            'IpProtocol': 'tcp',
            'FromPort': 80,
            'ToPort': 80,
            'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
        },
        {
            'IpProtocol': 'tcp',
            'FromPort': 22,
            'ToPort': 22,
            'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
        },
        {
            'IpProtocol': 'tcp',
            'FromPort': 443,
            'ToPort': 443,
            'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
        }
    ]
    
    egress_rules = [
        {
            'IpProtocol': '-1',  # Represents all protocols
            'FromPort': -1,      # Represents all ports
            'ToPort': -1,        # Represents all ports
            'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
        }
    ]

    # Add ingress rules
    for rule in ingress_rules:
        try:
            ec2.authorize_security_group_ingress(GroupId=security_group_id, IpPermissions=[rule])
            print(f"Ingress rule {rule} added successfully.")
        except ec2.exceptions.ClientError as e:
            if 'InvalidPermission.Duplicate' in str(e):
                print(f"Ingress rule {rule} already exists.")
            else:
                raise

    # Add egress rules
    for rule in egress_rules:
        try:
            ec2.authorize_security_group_egress(GroupId=security_group_id, IpPermissions=[rule])
            print(f"Egress rule {rule} added successfully.")
        except ec2.exceptions.ClientError as e:
            if 'InvalidPermission.Duplicate' in str(e):
                print(f"Egress rule {rule} already exists.")
            else:
                raise

    config.update({
        "security_group_id": security_group_id
    })

    with open('config.json', 'w') as f:
        json.dump(config, f)


    ec2 = boto3.resource('ec2', region_name=config['region'])            
    instances = ec2.create_instances(
        ImageId=config['Imageid'],
        MinCount=1,
        MaxCount=1,
        InstanceType='t2.micro',
        KeyName=config['key_pair_name'],
        SecurityGroupIds=[security_group_id],
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': "ravi_autostart"
                    },
                    {
                        'Key': 'Action',
                        'Value': "Auto-Start"
                    }
                ]
            }
        ]
    )

    instance_id = instances[0].id
    print(f"EC2 instance '{instance_id}' launched successfully.")

    # Wait until the instance is running
    ec2.meta.client.get_waiter('instance_running').wait(InstanceIds=[instance_id])
    print(f"EC2 instance '{instance_id}' is now running.")

    instance = instances[0]
    instance.reload()
    public_ip = instance.public_ip_address
    print(f"Public IP of instance '{instance_id}': {public_ip}")

    return instance_id

if __name__ == "__main__":
    with open('config.json') as f:
        config = json.load(f)

    instance_id = launch_ec2_instance(config)

    config.update({
        "instance_id1": [instance_id]
    })

    with open('config.json', 'w') as f:
        json.dump(config, f)
import boto3
import json
import time

def launch_ec2_instance(config):


    ec2 = boto3.resource('ec2', region_name=config['region'])            
    instances = ec2.create_instances(
        ImageId=config['Imageid'],
        MinCount=1,
        MaxCount=1,
        InstanceType='t2.micro',
        KeyName=config['key_pair_name'],
        SecurityGroupIds=[config['security_group_id']],
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': "ravi_autostop"
                    },
                    {
                        'Key': 'Action',
                        'Value': "Auto-Stop"
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
        "instance_id2": [instance_id]
    })

    with open('config.json', 'w') as f:
        json.dump(config, f)
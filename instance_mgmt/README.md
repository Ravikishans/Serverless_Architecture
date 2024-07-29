---

# EC2 Instance Auto-Launch and Auto-Stop Script

This project provides a Python script to automate the launching of an EC2 instance on AWS, assign a specific security group, and tag it with predefined values. The instance details are stored in a configuration file for further use.

## Prerequisites

Before running the script, ensure you have the following prerequisites:

- **AWS Account**: You need an AWS account to create and manage EC2 instances.
- **AWS CLI**: Install and configure the AWS CLI with your credentials.
- **Python 3.x**: Make sure Python 3.x is installed on your machine.
- **Boto3**: The AWS SDK for Python. Install it using pip if not already installed.

```bash
pip install boto3
```

## Configuration

Create a `config.json` file in the project directory with the following structure:

```json
{
    "region": "region_name",
    "key_pair_name": "keypair",
    "Imageid": "ami-******"
}
```

- **region**: The AWS region where you want to launch the instance.
- **Imageid**: The AMI ID of the image you want to use for the instance.
- **key_pair_name**: The name of the key pair to associate with the instance.

## Usage

1. Clone the repository:

```bash
git https://github.com/Ravikishans/Serverless_Architecture
cd instance_mgmt
```

2. Create and configure the `config.json` file as mentioned above.

3. Run the script:

```bash
python instance_autostart.py
python instance_autostop.py

```

The script will launch an EC2 instance with the specified configuration, wait until the instance is running, and print the public IP address of the instance.

## Script Details

### `launch_ec2_instance(config)`

This function takes a configuration dictionary as input and performs the following steps:

- Creates an EC2 instance with the specified configuration.
- Tags the instance with "Name" and "Action".
- Waits until the instance is in a running state.
- Retrieves and prints the public IP address of the instance.
- Returns the instance ID.

### Configuration Update

After the instance is launched, the script updates the `config.json` file with the instance ID under the key `instance_id1` & 'instance_id2'.

## Example Output

```
EC2 instance 'i-0123456789abcdef0' launched successfully.
EC2 instance 'i-0123456789abcdef0' is now running.
Public IP of instance 'i-0123456789abcdef0': 203.0.113.0
```

## create an IAM role in your in your aws account and give "AmazonEC2FullAccess" policy.

## lambda function

- Navigate to the Lambda dashboard and create a new function.

- Choose Python 3.x as the runtime.

- Assign the IAM role created in the previous step.

- Write the Boto3 Python script i.e. "instance_mgmt.py " to:

 1. Initialize a boto3 EC2 client.

 2. Describe instances with `Auto-Stop` and `Auto-Start` tags.

 3. Stop the `Auto-Stop` instances and start the `Auto-Start` instances.

 4. Print instance IDs that were affected for logging purposes

## Manual Invocation

- After saving your function, manually trigger it.

- Go to the EC2 dashboard and confirm that the instances' states have changed according to their tags.

## Contributing

Feel free to open issues or submit pull requests if you find bugs or have suggestions for improvements.


---
This project sets up an automated alerting mechanism to monitor your AWS billing. If the billing exceeds a specified threshold, an alert is sent via Amazon SNS.

## SNS Setup

1. Navigate to the SNS dashboard in the AWS Management Console.
2. Click on **Create topic**.
   - Choose **Standard** type.
   - Enter a name for your topic.
   - Click **Create topic**.
3. Click on **Create subscription**.
   - Select the topic you just created.
   - For protocol, choose **Email**.
   - Enter your email address.
   - Click **Create subscription**.
4. Check your email and confirm the subscription.

## Lambda IAM Role

1. Navigate to the IAM dashboard in the AWS Management Console.
2. Click on **Roles** and then **Create role**.
3. Choose **Lambda** as the trusted entity and click **Next**.
4. Attach the following policies:
   - **CloudWatchReadOnlyAccess**
   - **AmazonSNSFullAccess**
5. Click **Next**, provide a role name (e.g., `awsBilling`), and create the role.

## Lambda Function

1. Navigate to the Lambda dashboard in the AWS Management Console.
2. Click on **Create function**.
3. Choose **Author from scratch**.
   - Enter a name for your function.
   - Choose **Python 3.12** as the runtime.
   - Under **Permissions**, choose **Use an existing role** and select the IAM role created in the previous step.
   - Click **Create function**.
4. Replace the default code with the "snsCloudwatch.py" Boto3 Python script:

5. Click **Deploy** to save and deploy the function.

## Event Source (Bonus)

1. Navigate to the CloudWatch dashboard in the AWS Management Console.
2. Click on **Rules** under **Events** and then **Create rule**.
3. Under **Event Source**, choose **Event Source** and select **Create rule**.
   - Choose **Event Source**.
   - Select **Create Rule**.
   - Select **Event Source**.
4. Select **Create Rule** and then **Create Rule**.
5. Under **Targets**, click **Add Target** and select **Lambda function**.
   - Choose the Lambda function you created.
   - Click **Configure details**, provide a name and description, and click **Create rule**.

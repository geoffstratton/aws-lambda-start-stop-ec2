Repo Name
=========
aws-lambda-start-stop-ec2

Description
---------------
These are AWS Lambda functions for starting and stopping EC2 instances automatically, using Python (tested with 3.7), Amazon's boto3 SDK, and some method of invoking the Lambda functions at specified times (e.g., a CloudWatch cron job).

Prerequisites
---------------
* The [boto3 SDK](https://aws.amazon.com/sdk-for-python/).
* Ensure that the IAM Role attached to the Lambda function has a policy with ec2. If you want to create a custom policy, include:
    + ec2:DescribeInstances
    + ec2:StartInstances
    + ec2:DescribeRegions
    + ec2:StopInstances
* If using CloudWatch, your Lambda function also needs the usual CloudWatch Logs role.
* Also create a cron job in CloudWatch to invoke the Lambda function at the desired times.

### To set up boto3 for development (Amazon Linux and similar):

```
sudo yum install -y python3 python3-pip python3-setuptools
pip3 install boto3 --user
aws configure [enter your AWS access key and secret key]

python3
>>> import boto3
>>> ec2 = boto3.client('ec2')
>>> response = ec2.run_instances(ImageId='ami-00dc79254d0461090',InstanceType='t2.micro',KeyName='MY KEY',MinCount=1,MaxCount=1)
```

You can also run the included create_ec2.py function to create new EC2 instances.

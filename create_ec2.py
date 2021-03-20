import os
import boto3

AMI = os.environ['ami-00dc79254d0461077']
INSTANCE_TYPE = os.environ['t2.micro']
KEY_NAME = os.environ['MyEC2Pair']
SUBNET_ID = os.environ['subnet-032c5684cad3d81f3']

ec2 = boto3.resource('ec2')

def lambda_handler(event, context):

    instance = ec2.create_instances(
        ImageId=AMI,
        InstanceType=INSTANCE_TYPE,
        KeyName=KEY_NAME,
        SubnetId=SUBNET_ID,
        MaxCount=1,
        MinCount=1
    )

    print("New instance created:", instance[0].id)
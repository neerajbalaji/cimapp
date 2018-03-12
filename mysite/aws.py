import boto3
from boto3 import ec2

#ec2 = boto3.client('ec2')
#response = ec2.describe_instances()
#print(response)

s3 = boto3.resource('s3')
for bucket in s3.buckets.all():
  bucket_list=bucket.name
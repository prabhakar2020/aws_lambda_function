from __future__ import print_function
import boto3
import time, urllib
import json
"""Code snippet for copying the objects from AWS source S3 bucket to target S3 bucket as soon as objects uploaded on source S3 bucket
@author: Prabhakar G
"""
print ("*"*80)
print ("Initializing..")
print ("*"*80)

s3 = boto3.client('s3')

def lambda_handler(event, context):
    # TODO implement
    source_bucket = event['Records'][0]['s3']['bucket']['name']
    object_key = urllib.unquote_plus(event['Records'][0]['s3']['object']['key'])
    target_bucket = 'my-target-bucket'
    copy_source = {'Bucket': source_bucket, 'Key': object_key}
    
    print ("Source bucket : ", source_bucket)
    print ("Target bucket : ", target_bucket)
    print ("Log Stream name: ", context.log_stream_name)
    print ("Log Group name: ", context.log_group_name)
    print ("Request ID: ", context.aws_request_id)
    print ("Mem. limits(MB): ", context.memory_limit_in_mb)
    
    try:
        print ("Using waiter to waiting for object to persist through s3 service")
        waiter = s3.get_waiter('object_exists')
        waiter.wait(Bucket=source_bucket, Key=object_key)
        s3.copy_object(Bucket=target_bucket, Key=object_key, CopySource=copy_source)
        return response['ContentType']
    except Exception as err:
        print ("Error -"+str(err))
        return e

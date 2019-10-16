from __future__ import print_function
import boto3
import time, urllib
import json
"""Code snippet for deleting the objects from AWS S3 bucket as soon as objects uploaded on S3 bucket
@author: Prabhakar G
"""
print ("*"*80)
print ("Initializing..")
print ("*"*80)

s3 = boto3.client('s3')

def lambda_handler(event, context):
    # TODO implement
    bucket = event['Records'][0]['s3']['bucket']['name']
    object_key = urllib.unquote_plus(event['Records'][0]['s3']['object']['key'])
    
    try:
        print ("Using waiter to waiting for object to persist through s3 service")
        # It will till S3 service return the response
        waiter = s3.get_waiter('object_exists')
        waiter.wait(Bucket=bucket, Key=object_key)
        response = s3.head_object(Bucket=bucket, Key=object_key)
        print ("CONTENT TYPE : "+str(response['ContentType']))
        print ('ETag :' +str(response['ETag']))
        print ('Content-Length :'+str(response['ContentLength']))
        print ('KeyName :'+str(object_key))
        print ('Deleting object :'+str(object_key))
        # It will delete the objects/ data from S3 bucket as soon as trigger/ event is invoked
        s3.delete_object(Bucket=bucket, Key=object_key)
        return response['ContentType']
    except Exception as err:
        print ("Error -"+str(err))
        return err

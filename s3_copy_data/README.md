# AWS Lambda Function

In this example, we are going talk about - 
```
AWS lambda function for copy source S3 bucket objects/ data on target S3 bucket as soon as objects/ data uploaded on source bucket.
```
**Note**: First we have to create two S3 buckets one with name my-source-bucket and second one is my-target-bucket

Steps for creating the AWS Lambda function
-------------
 1.  Login to AWS console https://console.aws.amazon.com (If you dont have AWS account, follow AWS console signup options)
 1.  Click on **Services** link on main menu and choose **Lambda** option under **compute** section
 ![alt text](https://github.com/prabhakar2020/aws_lambda_function/blob/master/images/aws_services.PNG)
 1.  Under Lambda functions page, click on **create function** button
 ![alt text](https://github.com/prabhakar2020/aws_lambda_function/blob/master/images/aws_lambda_creation1.PNG)
 1.  You can create lambda function from available pre-defined templates as well as from scratch. In this example, I am creating lambda function from scratch by selecting **Author from scratch**
 ![alt text](https://github.com/prabhakar2020/aws_lambda_function/blob/master/images/aws_lambda_creation2.PNG)
 1. Fill the name of the lambda function and runtime (technology which you can write lambda function)
 ![alt text](https://github.com/prabhakar2020/aws_lambda_function/blob/master/images/aws_lambda_creation3.PNG)
 1. Choose permissions to run/ execute the lambda function. Here I am selecting option as already existing role which I had created earlier. In your case you can choose option **Create a new role with basic Lambda permissions** and create the role accordingly. For demo purpose you can grant administrative role
 ![alt text](https://github.com/prabhakar2020/aws_lambda_function/blob/master/images/aws_lambda_creation4.PNG)
 1. Click on **Create Function** button
 1. Click on **Add Trigger** button, since we want to execute the lambda function for specific triggers/ events.
 ![alt text](https://github.com/prabhakar2020/aws_lambda_function/blob/master/images/aws_lambda_creation5.PNG)
 1. Choose a trigger type and its configuration as bucket, event type and prefix and sufix values. After filling required details, click on **Add** button. As of now these prefix and sufix are not required for this demo, this these prefix and sufix are required for executing the lambda functions based on the filters with file types prefix and sufix. 
 ![alt text](https://github.com/prabhakar2020/aws_lambda_function/blob/master/images/aws_lambda_creation6.PNG)
 1. Now its time to write a code for first lambda function.
 
 As I described earlier, in this example we are going to copy the objects/ data from source S3 bucket to target S3 bucket.
  
The following code snippet (lambda function will be helpful for copying  uploaded objects/ data from source S3 bucket to target S3 bucket.
```python
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
```

Once your lambda function creation is done, now go to your AWS  S3 buckets page and click on my-source-bucket name which you have selected on lambda function **Add triggers** page.  Upload any file on my-source-bucket and then go to my-target-bucket and check. Both the bucket you can see the similar data.

For more details about code examplanation, debugging and testing.
<br/>
Please checkout my youtube video - 
<br/>
[Download source code - S3 Copy data](../code)
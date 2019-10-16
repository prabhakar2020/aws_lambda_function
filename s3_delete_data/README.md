# AWS Lambda Function

In this example, we are going talk about - 
```
AWS lambda function for deleting uploaded objects/ data from S3 bucket as soon as object/ data uploaded on S3 bucket.
```

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
 
 As I described earlier, in this example we are going to delete the data/ objects from S3 bucket as soon as data uploaded on S3 bucket.
  
The following code snippet (lambda function will be helpful for deleting uploaded objects/ data on S3 bucket
```python
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
        # It will wait till s3 service return the output
        waiter = s3.get_waiter('object_exists')
        waiter.wait(Bucket=bucket, Key=object_key)
        response = s3.head_object(Bucket=bucket, Key=object_key)
        print ("Key :"+str(object_key))
        print ("Content Type : "+str(response['ContentType']))
        print ('ETag :' +str(response['ETag']))
        print ('Content-Length :'+str(response['ContentLength']))
        print ('KeyName :'+str(object_key))
        print ('Deleting object :'+str(object_key))
        # Delete the uploaded objects/ data from defined bucket
        s3.delete_object(Bucket=bucket, Key=object_key)
        return response['ContentType']
    except Exception as err:
        print ("Error -"+str(err))
        return err
```

Once your lambda function creation is done, now go to your AWS S3 buckets page and click on the bucket name which you have selected on lambda function **Add triggers** page.  Upload any file and refresh the page once file is uploaded. It will delete the file as soon as upload is completed on S3 bucket.

For more details about code examplanation, debugging and testing.
<br/>
Please checkout my youtube video - 
<br/>
[Download source code - S3 Delete data](../code)
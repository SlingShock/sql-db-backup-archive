from __future__ import print_function
import json
import boto3
import csv
import io
import time, urllib

def lambda_handler(event, context):
    list_uploaded_s3_file(event, context)
    

def list_uploaded_s3_file(event, context):
    s3Client = boto3.client('s3')
    print(event)
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    print(bucket)
    print(key)
    
    if key.endswith('.zip'):
            fileDate = key[-10:]
            #print(fileDate)
    
            if fileDate.startswith('01'):
                print('Object date is 01')
                target_bucket = os.environ["TARGET_S3_BUCKET"]
                copy_source = {'Bucket': bucket, 'Key': key}
                print ("Source bucket : ", bucket)
                print ("Target bucket : ", target_bucket)
                print ("Log Stream name: ", context.log_stream_name)
                print ("Log Group name: ", context.log_group_name)
                print ("Request ID: ", context.aws_request_id)
                print ("Mem. limits(MB): ", context.memory_limit_in_mb)
                try:
                    print ("Using waiter to waiting for object to persist through s3 service")
                    waiter = s3Client.get_waiter('object_exists')
                    waiter.wait(Bucket=bucket, Key=key)
                    response = s3Client.head_object(Bucket=bucket, Key=key)
                    s3Client.copy_object(Bucket=target_bucket, Key=key, CopySource=copy_source)
                    print('Object copied')
                    return response['ContentType']
                except Exception as err:
                    print ("Error -"+str(err))
                    return err

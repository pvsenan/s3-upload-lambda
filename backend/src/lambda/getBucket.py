import json
import boto3
from botocore.exceptions import ClientError
import logging



def getBucket(event, context):
    client = boto3.client('s3')
    response = {}
    try:
        url = client.generate_presigned_url(
                'get_object',
                Params={'Bucket': 'synonyms-ps-test','Key':'synonyms.json'},
                ExpiresIn=300)

        body = {
                'presignedUrl':url
        }        
        response = {
            "statusCode": 200,
             "body": json.dumps(body)
        }   
        return response     
    except ClientError as e:
        logging.error(e)
        return None            


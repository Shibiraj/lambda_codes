import json
import boto3
from pprint import pprint
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb')

def get_data(domain):
    """
    fetches data from dynamo db (based on domain)

    :param domain:  type string
    :return:
    """
    
    table = dynamodb.Table('credential_data')
    # filter based on domain
    response = table.scan(
        FilterExpression=Attr('full_domain').eq(domain)
    )
    return response['Items']
            
def lambda_handler(event, context):
    """

    :param event:  type dict
    :param context: type LambdaContext
    :return:
    """
    domain = 'yahoo.co.in'
    response = get_data(domain)
    pprint(response)
    return {
        'statusCode': 200,
        'body': json.dumps('Data fetched successfully.!')
    }

import json
import boto3


def create_handler(event, context):
    client = boto3.client('dynamodb')
    client.put_item(
        TableName='customer_details',
        Item ={
            'membership_id': {'S': event['membership_id']},
            'address': {'S': event['address']},
            'entry': {'S': event['entry']},
            'exit': {'S': event['exit']},
            'lot_no': {'S': event['lot_no']},
            'name': {'S': event['name']},
            'photo_s3_key': {'S': event['photo_s3_key']},
            'ticket_no': {'S': event['ticket_no']},
            'vehicle_no': {'S': event['vehicle_no']},
            'balance': {'N': event['balance']}
        }
    )
    
def read_handler(event, context):
    client = boto3.client('dynamodb')
    response = client.get_item(
        TableName='customer_details',
        Key ={
            'membership_id': {'S': event['membership_id']}
        }
    )
    return response["name"]
    
def update_balance_handler(event, context):
    client = boto3.client('dynamodb')
    response = client.update_item(
        TableName='customer_details',
        Key ={
            'membership_id': {'S': event['membership_id']}
        },        
        AttributeUpdates={
            "balance": {
                'Value': {'N': str(event['balance'])},
                'Action': 'PUT'
            }
            
        }
    )
    return response
    




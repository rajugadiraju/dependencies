import requests

def lambda_handler(event, context):
    response = requests.get('http://checkip.amazonaws.com/')
    print('IP:', response.text.strip())
    return {
        'statusCode': 200,
        'body': 'Hello from Lambda!'
    }

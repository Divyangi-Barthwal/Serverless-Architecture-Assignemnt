import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    
    # Stop instances with Auto-Stop
    stop_resp = ec2.describe_instances(Filters=[
        {'Name': 'tag:Action', 'Values': ['Auto-Stop']},
        {'Name': 'instance-state-name', 'Values': ['running']}
    ])
    stop_ids = [i['InstanceId'] for r in stop_resp['Reservations'] for i in r['Instances']]
    if stop_ids:
        ec2.stop_instances(InstanceIds=stop_ids)
        print("Stopped instances:", stop_ids)
        
    # Start instances with Auto-Start
    start_resp = ec2.describe_instances(Filters=[
        {'Name': 'tag:Action', 'Values': ['Auto-Start']},
        {'Name': 'instance-state-name', 'Values': ['stopped']}
    ])
    start_ids = [i['InstanceId'] for r in start_resp['Reservations'] for i in r['Instances']]
    if start_ids:
        ec2.start_instances(InstanceIds=start_ids)
        print("Started instances:", start_ids)

    return {"status": "Complete"}

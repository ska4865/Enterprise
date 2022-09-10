import boto3
import simplejson
ec2 = boto3.client('ec2')

def ec2_describe(id=None):
    response = ec2.describe_instances()
    print(response)
    
def ec2_start(id):
    # Do a dryrun first to verify permissions
    try:
        ec2.start_instances(InstanceIds=[id], DryRun=True)
    except ClientError as e:
        if 'DryRunOperation' not in str(e):
            raise

    # Dry run succeeded, run start_instances without dryrun
    try:
        response = ec2.start_instances(InstanceIds=[id], DryRun=False)
        print(response)
    except ClientError as e:
        print(e)

def ec2_stop(id):
    # Do a dryrun first to verify permissions
    try:
        ec2.stop_instances(InstanceIds=[id], DryRun=True)
    except ClientError as e:
        if 'DryRunOperation' not in str(e):
            raise

    # Dry run succeeded, call stop_instances without dryrun
    try:
        response = ec2.stop_instances(InstanceIds=[id], DryRun=False)
        print(response)
    except ClientError as e:
        print(e)
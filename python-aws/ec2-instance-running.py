import boto3

access_key = "AKIASJHHVZ4UWIYTPXBI"
secret_key = "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"

client = boto3.client('ec2', aws_access_key_id=access_key, aws_secret_access_key=secret_key,
                                  region_name='us-east-1')

ec2_regions = [region['RegionName'] for region in client.describe_regions()['Regions']]

for region in ec2_regions:
    conn = boto3.resource('ec2', aws_access_key_id=access_key, aws_secret_access_key=secret_key,
                   region_name=region)
    instances = conn.instances.filter()
    for instance in instances:
        if instance.state["Name"] == "running":
            print (instance.id, instance.instance_type, instance.state, instance.VolumeId,region)
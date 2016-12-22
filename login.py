#  Import the Boto to connect to AWS
import boto3
import os
import time
import sys
from collections import defaultdict

# Set default variables
key_folder = '/Users/jordanwoodard/Desktop/Certificate/'

# Create the Build Functionality
ec2 = boto3.resource('ec2')

# Get information for all running instances
# Optional Filter
active_instances = ec2.instances.filter(Filters=[{
    'Name': 'instance-state-name',
    'Values': ['running']}])

# Establish Default Dictionary
ec2info = defaultdict()
counter = 0

# Loop Through Active Instances
for instance in active_instances:
    # Check for Name Tag
    for tag in instance.tags:
        if 'Name' in tag['Key']:
            name = tag['Value']
        if 'Description' in tag['Key']:
            description = tag['Value']
    # Setup Number Variable for the EC2 Instance Input
    counter += 1
    # Add instance to Default Dictionary by Instance Id as that is Unique
    ec2info[counter] = {
        # Required
        'ID': counter,
        'Name': name,
        'Description': description,
        'Type': instance.instance_type,
        'Private IP': instance.private_ip_address,
        'Key Pair': instance.key_name,
        'Public IP': instance.public_ip_address,
        # Optional Field State Not Required as It is being filtered by Running at the top
        # 'State': instance.state['Name'],
        # 'Launch Time': instance.launch_time,
    }

# Depending on the Listed Fields Above, Modify this listing
# For a long list of options, consider using the following commented out attributes
# sections to list out a full listing of attributes by EC2

# attributes = ['ID', 'Name', 'Description', 'Type', 'Private IP', 'Public IP', 'Key Pair']
# for instance_id, instance in ec2info.items():
# for key in attributes:
#     print("{0}: {1}".format(key, instance[key]))

for instance_id, instance in ec2info.items():
    print(
        "#:{0} Name: {1} Description: {2} Type: {3} ".format(instance['ID'], instance['Name'], instance['Description'],
                                                             instance['Type']))
    print("------")

# Get user Input
instance_selection = raw_input('Select EC2 Instance: ')
instance_user = raw_input('Select Login User: ')

# If selected values are empty, close
if instance_user == '' or instance_selection == '':
    sys.exit()

# If Selected values are equal to exit
if instance_user == 'exit' or instance_selection == 'exit':
    sys.exit()

# Let user know Login is starting
ssh_instance = ec2info[instance_selection]
time.sleep(1)  # delays for 2 seconds
print ("Preparing to SSH into {0} ({1})".format(ssh_instance['Name'], ssh_instance['Public IP']))

# Set Key location
ssh_key = "{0}{1}.pem".format(key_folder, ssh_instance['Key Pair'])
ssh_ip = ssh_instance['Public IP'].replace(".", "-")

time.sleep(1)  # delays for 2 seconds
print ("Using Key {0}".format(ssh_key))
time.sleep(1)  # delays for 2 seconds

os.system('ssh -i "{0}" {1}@ec2-{2}.compute-1.amazonaws.com'.format(ssh_key, instance_user, ssh_ip))

# AWS-EC2-Login-Script
This script in conjunction with AWS CLI will allow users to set a directory to the PEM files and make a direct connection to your EC2 instances via SSH connection. The script uses Boto3 to list out the ec2 instances by a "Name" Tag often given when the box is created.

##Requirements
1. AWS CLI ( for help with this please visit https://aws.amazon.com/cli/)
2. Python 2.7 or higher


##Instructions

Running the file login.py in terminal will prompt you load all of your EC2 instances via the CLI and give you an option to add in two variables
1. EC2 ID
2. SSH Login User

Once both fields have been added, it will verify the information and perform a SSH connection into the EC2 box.

Be sure to add the Key Folder location to the script prior to running.

##Tip

For easy access to the script, you can create a bash script on your desktop to execute to the file location.

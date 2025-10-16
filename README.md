# Serverless-Architecture-Assignemnt

**Assignment 1**

Step 1: Launch 2 Instance and tag 1st instance as Auto-start and 2nd instance as Auto-Stop

![image alt](https://github.com/Divyangi-Barthwal/Serverless-Architecture-Assignemnt/blob/2c146bd128deefe6c5d98cf395db421b2df3db8a/EC2-Autostart.png)
![image alt](https://github.com/Divyangi-Barthwal/Serverless-Architecture-Assignemnt/blob/974186a88d64ebcf9df81ae8c7704744aad607ba/EC2-Autostop.png)

Step 2:  Create IAM role for Lambda and add 2 permissions (i.e AmazonEC2FullAccess, AWSLambdaBasicExecutionRole)
![image alt](https://github.com/Divyangi-Barthwal/Serverless-Architecture-Assignemnt/blob/974186a88d64ebcf9df81ae8c7704744aad607ba/IAM%20role%20permission.png)
![image alt](https://github.com/Divyangi-Barthwal/Serverless-Architecture-Assignemnt/blob/974186a88d64ebcf9df81ae8c7704744aad607ba/IAM%20role%20permission2.png)

Step 3: Create Lambda Function and copy the code 
![image alt](https://github.com/Divyangi-Barthwal/Serverless-Architecture-Assignemnt/blob/21a797c3aa050635ef04e0d37fa4e4c410c6d9b9/Screenshot%202025-10-15%20233356.png)

Step 4: Test the lambda function. while navigating to the console
![image alt](https://github.com/Divyangi-Barthwal/Serverless-Architecture-Assignemnt/blob/d67fb8ed4803cf2ce88fb800abee2d9874a63083/Test%20result.png)



**Assignment 2**
Assignment 2:

Step 1: Create a S3 bucket name: lambda-cleanup-bucket-a5 
and uploaded few files
![image alt](https://github.com/Divyangi-Barthwal/Serverless-Architecture-Assignemnt/blob/90f1c366c4a00075a2f8b642b82dacaf1187445a/S3%20bucket.png)

Step 2: Create an IAM Role for Lambda
Navigating to AWS console and clicking the IAM and select role 
create role ---> Create an IAM Role for Lambda ---> Use case → Lambda ----> Attach policy → Search & select AmazonS3FullAccess
Name--> lambda-s3-cleanup-role-a5

Step 3:
Create the Lambda Function
navigating to AWS console  created a lambda fuction called: Name: S3CleanupFunction
Runtime: Python 3.12 (or latest available) and Permissions: Choose Use existing role → select lambda-s3-cleanup-role
![image alt](https://github.com/Divyangi-Barthwal/Serverless-Architecture-Assignemnt/blob/6caa81f3e130730dae74f62ed21b00f62c1d8d22/boto%203%20code.png)

Step 4: Test
In Lambda--> Click Test ---> create a new test event and name it TestEvent
status code: 200 should be visible
![image alt](https://github.com/Divyangi-Barthwal/Serverless-Architecture-Assignemnt/blob/6caa81f3e130730dae74f62ed21b00f62c1d8d22/Test%20result.png)

**Assignment 3**

Step 1:Create S3 bucket 
Navigate to AWS console and Click on S3 and create 3 S3 bucket
Bucket name1: encrypted-bucket-001
Bucket name2: unencrypted-bucket-002 disable encryption
Bucket name3: encrypted-bucket-003
Bucket name4: unecrypted-bucket-004 disable encryption
![image alt](https://github.com/Divyangi-Barthwal/Serverless-Architecture-Assignemnt/blob/cd8c3f5ac5a14effb58ff7408710a8236e161ff7/S3%20bucket.png)

Step 2: Create IAM Role for Lambda
Go to IAM Dashboard > Roles > Create role 
Trusted entity: Choose Lambda
Permissions--> AmazonS3ReadOnlyAccess
Rolename: LambdaS3ReadOnlyRole1--> Create role
![image alt](https://github.com/Divyangi-Barthwal/Serverless-Architecture-Assignemnt/blob/cd8c3f5ac5a14effb58ff7408710a8236e161ff7/IAM%20permission.png)

Step 3: Create the Lambda Function
Lambda > Click Create function
Function name: DetectUnencryptedS3Buckets
Runtime: Python 3.12
Permissions: Select Use existing role > Choose LambdaS3ReadOnlyRole > Click Create function

Step 4: Add python code to lambda fuction
![image alt](https://github.com/Divyangi-Barthwal/Serverless-Architecture-Assignemnt/blob/119fa5bb699f73e2fde4dd16f30addc52217da3c/A3%20python%20code.png)
Test the fuction.
Error received: 
![image alt](https://github.com/Divyangi-Barthwal/Serverless-Architecture-Assignemnt/blob/119fa5bb699f73e2fde4dd16f30addc52217da3c/error.png)

Root cause: IAM role (DetectUnencryptedS3Buckets-role-4tbbegcg) does not have permission to perform the action
The AmazonS3ReadOnlyAccess policy sometimes does not include this permission when the role was created through the Lambda console wizard (it can depend on AWS defaults).
Navigating back to IAM role --> update the policy --> create custom inline policy 

Under your IAM role page → go to Permissions tab → scroll down and click:
Add permissions → Create inline policy---> Click the JSON tab and paste this
![image alt](https://github.com/Divyangi-Barthwal/Serverless-Architecture-Assignemnt/blob/2b68cbb647d557a3ca7d7554a69762c98901b61d/IAM%20extra%20permission.png)
![image alt](https://github.com/Divyangi-Barthwal/Serverless-Architecture-Assignemnt/blob/2b68cbb647d557a3ca7d7554a69762c98901b61d/IAM%20extra%20permission1.png)

once the permission is updated. navigate to Lambda fuction and test again

![image alt](https://github.com/Divyangi-Barthwal/Serverless-Architecture-Assignemnt/blob/2b68cbb647d557a3ca7d7554a69762c98901b61d/Screenshot%202025-10-16%20AFinal%20result.png)
Success code 200

**Assignment 8**
Step 1: create IAM --> Role--> Create Role
Trusted entity: AWS service → Lambda → Next.
Attach permissions:Check AWSLambdaBasicExecutionRole--> Click Next (we’ll add a small custom policy next).
Name: LambdaComprehendSentimentRole → Create role.
In Add permissions → Create inline policy → JSON and below is the code
![image alt](https://github.com/Divyangi-Barthwal/Serverless-Architecture-Assignemnt/blob/4054a213f24c40e27f58e4ed5cf3c103026c131f/IAM%20access.png)
![image alt](https://github.com/Divyangi-Barthwal/Serverless-Architecture-Assignemnt/blob/4054a213f24c40e27f58e4ed5cf3c103026c131f/IAM%20inline%20access%20permission.png)

Step 2:Create Lambda function
Author from scratch--> Name: analyze-review-sentiment --> Runtime: Python 3.12 --> Architecture: x86_64 --> Permissions → Use an existing role → select LambdaComprehendSentimentRole --> Create function
![image alt](https://github.com/Divyangi-Barthwal/Serverless-Architecture-Assignemnt/blob/4054a213f24c40e27f58e4ed5cf3c103026c131f/lambda%20function.png)

Now test the code 
200 status code 
![image alt](https://github.com/Divyangi-Barthwal/Serverless-Architecture-Assignemnt/blob/b3820f1ae15bf00d3f8f5217308d51161513ca58/200%20status.png)








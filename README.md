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
Navigate to AWS console and Click on S3 and create
Bucket name: encrypted-bucket-001





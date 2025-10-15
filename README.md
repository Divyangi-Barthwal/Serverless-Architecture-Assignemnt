# Serverless-Architecture-Assignemnt
Assignment choosen are 1,2,3 and 4

**Assignment 1**
Step 1: Launch 2 Instance and tag 1st instance as Auto-start and 2nd instance as Auto-Stop

![image alt](https://github.com/Divyangi-Barthwal/Serverless-Architecture-Assignemnt/blob/2c146bd128deefe6c5d98cf395db421b2df3db8a/EC2-Autostart.png)
![image alt](https://github.com/Divyangi-Barthwal/Serverless-Architecture-Assignemnt/blob/974186a88d64ebcf9df81ae8c7704744aad607ba/EC2-Autostop.png)

Step 2:  Create IAM role for Lambda and add 2 permissions (i.e AmazonEC2FullAccess, AWSLambdaBasicExecutionRole)
![image alt](https://github.com/Divyangi-Barthwal/Serverless-Architecture-Assignemnt/blob/974186a88d64ebcf9df81ae8c7704744aad607ba/IAM%20role%20permission.png)
![image alt](https://github.com/Divyangi-Barthwal/Serverless-Architecture-Assignemnt/blob/974186a88d64ebcf9df81ae8c7704744aad607ba/IAM%20role%20permission2.png)

Step 3: Create Lambda Function 

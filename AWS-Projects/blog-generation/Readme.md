# Blog Generator using AWS Lambda & Amazon Bedrock

This project demonstrates a fully serverless workflow where a blog post is generated using **Amazon Bedrock (Llama 3)** and then stored automatically in **Amazon S3** using an **AWS Lambda** function triggered through **API Gateway**.
All logs are tracked with **CloudWatch**, and IAM **policies** ensure secure access to Bedrock and S3.

---

## Features

* Generate blog posts using **Meta Llama3 on Amazon Bedrock**
* Serverless compute using **AWS Lambda**
* Store generated content in **Amazon S3**
* Trigger generation via **API Gateway HTTP endpoint**
* Logging & metrics using **Amazon CloudWatch**
* Secure permissions with **IAM roles & custom policies**

---

## Architecture Overview

1. API Gateway receives a POST request containing the blog topic
2. API Gateway invokes the Lambda function
3. Lambda sends the prompt to Amazon Bedrock (Llama3)
4. Bedrock returns the generated blog content
5. Lambda saves the output to the S3 bucket
6. CloudWatch logs execution details

---

## AWS Services Used

### **AWS Lambda**

* Runs the Python function
* Calls Amazon Bedrock’s `InvokeModel` API
* Saves output to S3

### **Amazon S3**

* Stores the generated blog text files
* Organized by timestamp and blog topic

### **Amazon Bedrock**

* Provides LLM inference using Llama3
* Receives prompt + parameters and returns generated content

### **API Gateway**

* Exposes a public HTTP endpoint
* Sends event payload to Lambda

### **IAM Policies / Roles**

* Lambda execution role includes:

  * Bedrock InvokeModel permissions
  * S3 PutObject permissions
  * CloudWatch logging permissions

### **CloudWatch**

* Captures Lambda logs
* Useful for debugging and monitoring

---

## API Example

POST to your API Gateway URL:

```json
{
  "blogtopic": "AI Security"
}
```

---

## Output

Generated files saved to:

```
s3://your-bucket-name/blogs/<topic>_<timestamp>.txt
```
import json
import boto3 # to invoke foundational model
import botocore.config # to set up the client configuration
from datetime import datetime

# Function to generate blog post using Bedrock
def blog_generate_using_bedrock(blogtopic: str) -> str:
    prompt = f"""<s>[INST] Human: Write a blog post about {blogtopic} in a conversational style. Include an introduction, main points, and a conclusion. Use headings and bullet points where appropriate.
    Assistant: [/INST]</s>"""

    body = {
        "prompt": prompt,
        "max_gen_len": 1024,
        "temperature": 0.7,
        "top_p": 0.95
    }

    try:
        bedrock = boto3.client(
            "bedrock-runtime",
            region_name="us-east-1",
            config=botocore.config.Config(
                read_timeout=60,
                retries={"max_attempts": 10, "mode": "standard"}
            )
        )

        response = bedrock.invoke_model(
            modelId="meta.llama3-8b-instruct-v1:0",
            body=json.dumps(body)
        )

        response_body = response["body"].read().decode("utf-8")
        data = json.loads(response_body)

        print(data)

        return data["generation"]   # 👈 correct output key
    except Exception as e:
        print(f"Error generating blog post: {e}")
        return "Error generating blog post."
    
# Save the generated blog post to S3
def save_blog_to_s3(s3_bucket:str, s3_key:str, generated_blog:str)->bool:
    s3_client = boto3.client('s3')
    try:
        s3_client.put_object(Bucket=s3_bucket, Key=s3_key, Body=generated_blog)
        print(f"Blog post saved to s3://{s3_bucket}/{s3_key}")
        return True
    except Exception as e:
        print(f"Error saving blog post to S3: {e}")
        return False
    
# Lambda handler function
def lambda_handler(event, context): # entry point for AWS Lambda, captures event and context
    event=json.loads(event['body'])
    blogtopic=event['blogtopic'] # extract blog topic from the event

    generate_blog = blog_generate_using_bedrock(blogtopic = blogtopic)
    if generate_blog:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        s3_key = f"blogs/{blogtopic.replace(' ', '_')}_{current_time}.txt"
        s3_bucket = "aws-projects-blog-bucket"  
        save_blog_to_s3(s3_bucket=s3_bucket, s3_key=s3_key, generated_blog=generate_blog)
    else:
        print("Blog generation failed.")
    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Blog generation process completed.'})
    }

    



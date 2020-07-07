AWS LAMBDA Assessment
---------------------

#### Q1. How can you increase the CPU resources for your Lambda?
- Increase the configured CPU value
- Increase the configured timeoutout  value
- Increase the configured memory value <<<<<<--------------- CORRECT
- Increase the configured concurrency value

#### Q2. How can additional code or content be provided for Lambda?
- blocks
- layers <<<<<<--------------- CORRECT
- aliases
- handlers

#### Q3. How can Step Functions call Lambdas?
- in sequence
- both of these answers  <<<<<<------------- CORRECT
- neither of these answers
- in parallel

#### Q4. Which AWS CLI command invokes a function?
- aws lambda invoke --function ReturnBucketName outputfile.txt
- aws lambda execute --function-name ReturnBucketName outputfile.txt
- aws lambda invoke --function-name ReturnBucketName outputfile.txt  <<<<<<<<------ CORRECT
- aws lambda execute --function ReturnBucketName outputfile.txt

#### Q5. What adds tracing capabilities to a Lambda?
- AWS Trace
- CloudStack
- CloudTrail
- AWS X-Ray   <<<<<<----- CORRECT

#### Q6. You need to build a continuous intergration/deployment pipeline for a set of Lambdas. What should you do?
- Create configuration files and deploy them using AWS CodePipeline.
- Create CloudFormation templates and deploy them using AWS CodeBuild
- Create configuration file and deploy using AWS CodeBuild
- Create CloudFormation templates and deploy them using AWS CodePipeline. <<<<<<<<------ CORRECT

#### Q7. What can you use to monitor function invocations?
- API Gateway
- S3
- SAS
- CLoudTrail <<<<<<--------------- CORRECT

#### Q8. It is AWS best practice to enable Lambda logging by which of these methods.
- Use S3 metrics and CloudWatch alarms
- Create custom metrics within your Lambda code.
- Create custom metrics within your CloudWatch code.
- Use Lambda metrics and CloudWatch alarms. <<<<<<--------------- CORRECT

#### Q9. What may be provided for environment variables?
- an SSL certificate
- a bitmask
- an AWS KMS key  <<<<<<---------- CORRECT
- an HTTP protocol 

#### Q10. Lambda allows for running of what other things?
- binaries.
- all of these answers <<<<<-------------- CORRECT
- executables
- Shell scripts

#### Q11. In what style must you write Lambda code?
- MVC
- virtual
- stateless <<<<<<----------- CORRECT
- protocol

#### Q12. How can a developer provide Lambda code?
- by uploading a .zip file
- all of these answers   <<<<<<----------- CORRECT
- by editing inline
- from an S3 bucket

#### Q13. You are performance-testing your Lambda to verify that you set the memory size adequately. Where do you verify the exectuon overhead?
- CLoudWatch logs
- DynamoDB logs
- S3 logs
- Lambda logs. <<<<<<<<------ CORRECT

#### Q14. What facilitates continuous delivery of Lambdas?
- CodeStack
- ElasticStack
- Mobile Hub
- CodeDeploy <<<<<<<<------ CORRECT

#### Q15. How are computing resources allocated to Lambdas?
- proportionally  <<<<<------- CORRECT
- equally
- periodically
- daily

